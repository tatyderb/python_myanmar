# fixture

lesson = 1037732

## Что такое фикстуры и зачем они нужны

Обычный план теста состоит из:

1. Подготовка тестовых данных. (setup)
2. Действие. 
3. Проверка результатов.
4. Зачистка. (cleanup или teardown в некоторых фреймворках)

Ранее мы рассматривали только действие и проверку результатов. В этом разделе обратим внимание на подготовку к тестам и зачистку.

* setup: открытие браузера, установка соединения с БД, чтение матриц из файлов.
* teardown: закрытие браузера, корректное закрытие соединения с БД.

Действия подготовки к тесту могут быть разными для разных областей:

* Создать БД и наполнить ее данными в начале всех тестов.
* Открыть соединение с БД и закрыть его после тестов.
* Открыть сессию в браузере, отдельно для тестов обычного пользователя, отдельно для администратора в его панели администратора для набора тестов тестирования админ.панели.
* login/logout для теста покупки в магазине в начале и конце одного теста.
* Случайный логин/пароль для регистрации пользователя.

Для этого в pytest используют специальные сущности - **фикстуры** (fixture).

Фикстуры будем объяснять на двух примерах - соединение с БД и генерация логина/пароля.

Если бы мы не знали фикстуры, то мы бы написали функции и вызывали бы их в тесте.

```python
def generate_data():
    login = f"autotest_{time.time()}@hyper.org"     # Генерирует логин
    password = "512" # Назначает пароль
    return {'login': login, 'password': password}   # Возвращает логин и пароль в виде словаря
    
def connection_to_DB():
    # далее в рецептах мы напишем правильную функцию, а пока для демонстрации будем возвращать строку
    connection = "Соединение с БД установлено"
    return connection
```

### Классический подход

Импортируем эти функции и используем их, явно вызывая внутри теста.
```python
# обычные функции
def generate_data():
    login = f"autotest_{time.time()}@hyper.org"     # Генерирует логин
    password = "512" # Назначает пароль
    return {'login': login, 'password': password}   # Возвращает логин и пароль в виде словаря
    
def connection_to_DB():
    # далее в рецептах мы напишем правильную функцию, а пока для демонстрации будем возвращать строку
    connection = "Соединение с БД установлено"
    return connection

# тесты
class TestA:
    def test_my(self):
        conn = connection_to_DB()
        user_data = generate_data()
    
        # использование данных
        print(user_data)    # {'login': 'autotest_1690033771@hyper.org', 'password':
        print(conn)         # Соединение с БД установлено
```
* Плюс:
    * явный вызов функций, можно перейти в IDE к определению функции.
* Минус:
    * код теста разрастается,
    * не забыть в конце вызвать код, который закрывает соединение с БД (легко забыть).
    
### Фикстуры

* Определяем функцию с декоратором `@pytest.fixture()`.
* передаем в аргументы функции-теста **имя** этой фикстуры.

Запишем в одном файле `test_demo.py` определение и использование фикстуры `data` и `db_conn`:

```python
import pytest

# фикстуры
@pytest.fixture()
def data():
    login = f"autotest_{time.time()}@hyper.org"     # Генерирует логин
    password = "512" # Назначает пароль
    return {'login': login, 'password': password}   # Возвращает логин и пароль в виде словаря
    
@pytest.fixture()
def db_conn():
    # далее в рецептах мы напишем правильную функцию, а пока для демонстрации будем возвращать строку
    connection = "Соединение с БД установлено"
    return connection

# тесты
class TestA:
    def test_my(self, db_conn, data):
        # использование данных
        print(data)     # {'login': 'autotest_1690033771@hyper.org', 'password':
        print(db_conn)  # Соединение с БД установлено
```

Как это работает:

* при вызове функции `test_my` вызывается функция 
    * `db_conn`, помеченная как фикстура;
    * `data`, помеченная как фикстура;
* вызывается код `test_my(объект_который_вернула_функция_db_conn, объект_который_вернула_функция_data)`

Очевидны плюсы и минусы такого подхода:

* Плюс:
    * меньше кода.
    * далее покажем как писать фикстуры, чтобы закрытие происходило автоматически в любом случае, не зависимо от того, прошел тест или упал, выбросив исключение.
* Минус:
    * легко написать код с запутанной структурой.
    
**Список доступных фикстур** в файле `test_demo.py`:
```python
pytest --fixtures test_demo.py
```

Пока не ясно как повторно использовать фикстуры в разных файлах (и сделать все еще короче и запутаннее).

## conftest.py

Если собираетесь использовать фикстуру в нескольких файлах, то: 

* объявите ее в файле **conftest.py** (в корне проекта, в подкаталогах - где определите, там фикстура из файла и видна),
* `import` **не нужен**! pytest сам найдет где фикстура определена, в текущем файле или в ближайшем вверх по дереву каталогов.

Это смущает на первых порах. Имя `data` есть, а ни в каких импортируемых модулях такого объекта нет! Поэтому старайтесь придерживаться правила:

* `conftest.py` один и лежит в корне проекта,
* в файле тестов фикстуры, кроме фабрик данных, не создаете; даже фабрики данных стараетесь вынести в одно место.
* Работа в IDE позволяет перейти от вызова к определению фикстуры (имя фикстуры - это "гиперссылка" в PyCharm, на которую можно кликнуть и провалиться в объявление фикстуры).

## Зависимости фикстур

Одна фикстура может вызывать в аргументах другую фикстуру.

```python
import import pyaml_env

@pytest.fixture()
def where():
    # где запускаются тесты, на dev, local или stage окружении, 
    # позже покажем как задавать это в аргументах командной строки и разбирать в conftest.py
    # пока будем возвращать всегда, что мы работаем в dev окружении
    return 'dev'
    
@pytest.fixture()
def evn(where):
    """ Возвращает конфигурацию для dev, local или stage сервера в виде словаря. """
    config = pyaml_env.parse_config('environment.yml')
    return config[where]
```
Очень удобно все параметры запуска на разных серверах свести в один файл конфигурации, например, в файл по формату YAML, который будем разбирать пакетом `pyaml_env`:
```python
# файл environment.yml
dev:
    host: vdi.mipt.ru
    port: 51490
    login: student
    password: 1q2w3e4r
    
stage:
    host: acm.mipt.ru
    port: 22
    login: derbyshevatn
    password: !ENV ${ACM_PASSWORD}  # можно взять значение из переменной окружения ACM_PASSWORD
    
local:
    host: 127.0.0.1
    port: 80
    login: test
    password: test
```
У нас есть первый рецепт. **Чтение тестовой конфигурации** с помощью фикстур.

## Использование фикстур в тестовом классе через usefixtures

`@pytest.mark.usefixtures('data', 'db_conn')` - вызываем фикстуры для всего класса.

```python
# Этот код не работает, смотрите объяснение почему.

# тесты
@pytest.mark.usefixtures("db_conn", "data")
class TestA:
    def test_my(self):
        # использование данных
        print(data)     # {'login': 'autotest_1690033771@hyper.org', 'password': 512}
        print(db_conn)  # Соединение с БД установлено
```
Код одного теста стал еще короче (нет параметров) и еще запутаннее (откуда мы взяли db_conn и data?)

**Кроме того, этот код не работает. Тест, использующий фикстуру через `usefixtures`, не может использовать возвращаемое значение фикстуры.**

Зачем тогда нужны фикстуры уровня класса (набора тестов)? Помним, фикстуры - это setup/teardown функции. Если нужно что-то сделать до всех тестов в классе и после всех тестов, то используйте фикстуру через `usefixtures`. Например, создать тестовые данные в БД и удалить их после тестов.

**Если нужно возвращаемое фикстурой значение, пишем имя фикстуры как параметр тестовой функции или используем `request.cls` (расскажем позже)**.

## QUIZ Фикстура

Чтобы функция была фикстурой, у нее пишут декоратор

A. `@fixture`
B. `@pytest.fixture`
C. `@pytest.fixture()`
D. `@pytest.usefixture()`

ANSWER: C

## QUIZ Зависимости

Пусть определена фикстура `env`. Фикстура `db_connection`, которая зависит от `env` пишут так:

A.
```python
@pytest.fixture()
def db_connection(env):
    ...
```

B.
```python
@pytest.fixture(env)
def db_connection():
    ...
```

C.
```python
@pytest.fixture('env')
def db_connection():
    ...
```

ANSWER: A


## QUIZ Фикстуры

Какой код приведет к печати
```
{'login': ''mytest@gmail.com', 'password': '512'}
Соединение с БД установлено
```
Если в этом же файле выше определены фикстуры:
```python
import pytest, time

# фикстуры
@pytest.fixture()
def data():
    return {'login': 'mytest@gmail.com', 'password': '512'}
    
@pytest.fixture()
def db_conn():
    connection = "Соединение с БД установлено"
    return connection
```
### Вариант А

```python
class TestA:
    def test_my(self, db_conn, data):
        print(data)
        print(db_conn)
```

### Вариант B

```python
@pytest.mark.usefixtures("db_conn", "data")
class TestA:
    def test_my(self):
        print(data)
        print(db_conn)
```

### Вариант С

```python
class TestA(db_conn, data):
    def test_my(self):
        print(data)
        print(db_conn)
```

### Вариант D

```python
@pytest.mark.usefixtures("db_conn", "data")
class TestA:
    def __init__(self):
        self.db_conn = db_conn
        self.data = data
        
    def test_my(self):
        print(self.data)
        print(self.db_conn)
```

A. Вариант A

B. Вариант B

C. Вариант С

D. Вариант D

E. Все варианты рабочие.

F. Ни один из вышеперечисленных.


SHUFFLE: False
ANSWER: A

## Использование фикстур через request.cls и ее вызов с помощью маркера (декоратора)

Класс с конструктором `__init__` не рассматривается, как "набор тестов, даже если его имя начинается с `Test`. Что делать, если хочется написать конструктор и определить в нем поля `self.login` и `self.password` и использовать дальше во всех тестах данного класса?

Еще больше сделать код неочевидным может использование фикстур через `request.cls`

[request](https://docs.pytest.org/en/7.1.x/reference/reference.html#request) - специальная фикстура, которая дает информацию о вызывающей функции.

Разберем пример про генерацию логина и пароля, сделаем их доступными для всех тестов класса `TestExample`.

* **request** - специальный объект (фикстура),
* **cls** - аттрибут, ссылающийся на класс, которому принадлежит тестовая функция.
* *переменная* - переменную с таким именем мы создадим в нашем классе.

Фикстура в файле `conftest.py`:
```python
import pytest
import time

@pytest.fixture
def data(request):
    request.cls.login = f"autotest_{time.time()}@hyper.org" # Генерирует логин
    request.cls.password = "512" # Назначает пароль
```
В каком классе будут определены эти переменные? В том классе, для которого будет указана фикстура `data` в виде параметра, в примере это `TestExample`.

```python
# файл test_example.py
import pytest

@pytest.mark.usefixtures("data") # Вызываем фикстуру над классом, много 
class TestExample:

    def test_1(self):
        # можем ИСПОЛЬЗОВАТЬ переменные self.login и self.password
        print(self.login)       # cюда передастся логин
        print(self.password)    # сюда пароль
```
Что делает данная фикстура? Она **создает** в классе поля и инициирует их. То есть делает то же самое, что такой код (*этот код работать не будет, потому что в Test классах не должно быть функции `__init__`*):
```python
class TestExample:
    # Данный кусок кода = requst.cls.login и request.cls.password в фикстуре
	def __init__(self):
        self.login = f"autotest_{time.time()}@hyper.org"
        self.password = "512"
```

* Плюсы:
    * фикстуру `data` можно повторно использовать в разных классах.
* Минусы:
    * понижается читаемость кода, вы внезапно при чтении кода встречаете поля объекта, которые нигде явно не присваивали.
    
Используйте подобный подход только когда польза (повторное использование) превышает вред (понизилась читаемость).

Итого: **создать внутри объектов класса переменную login** это `request.cls.login`. Конструктор не нужен.


## Области действия фикстуры: function, class, module, package или session.

Пусть в тесте устанавливается SMTP соединение, по которому передаются данные.

Напишем фикстуру `smtp_connection`, которая будет возвращать объект - открытое smtp соединение пакета smtplib. Этот объект нужен в каждом тесте одного файла (модуля с точки зрения питона). Но открывать и закрывать его - процедура длительная. Хочется открыть соединение один раз, провести все тесты, описанные в данном файле.

Для простого решения таких задач у фикстуры есть параметр **scope**. Где фикстура **вызывается** и исполняется код фикстуры. Полученный объект передается как аргумент во все тестовые функции.

```python
# файл conftest.py

import pytest
import smtplib

# обратите внимание на аргумент scope
@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
```
Файл с тестами (имя фикстуры указываем аргументом в **каждой функции**, но вызывается фикстура **один раз** на файл и в обе функции передан один и тот же объект, который вернул вызов фикстуры в этом файле):
```python
# файл test_module.py

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg

def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
```

### Области действия (уровни, scope) фикстур

* function (по умолчанию), 
* class, 
* module, 
* package,
* session.

### autouse=True

scope определяет **когда** будет вызвана фикстура. Параметр фикстуры `autouse=True` может изменить **в каком случае** будет вызвана фикстура. Эта фикстура **будет обязательно вызвана**.

Фикстуры, у которых определено `autouse=True` вызываются на том же уровне, что определены в `scope`, но они будут вызываться всегда, не зависимо от того, где написан их код.

Пусть в файле `a.py` определена фикстура
```python
@pytest.fixture(scope="function", autouse=True)
def pokemon_everywhere():
    print('Gotta catch them all!')
```
В файле `b.py` все тестовые функции получат эту фикстуру, даже если они не писали ее в качестве аргумента и не использовали `usefixtures`. *И все напечатают этот текст.*

Используйте этот параметр с осторожностью. Лучше расположите фикстуру в файле `conftest.py` и передавайте ее явно в аргументах. Хуже вопроса "почему моя фикстура не вызывается" только проблема "какой код это делает и где он написан?!"

Пример использования этого параметра будет разобран в рецепте [begin-rollback транзакций каждого теста]().


### Порядок создания фикстур

* Сначала создаются структуры более общего уровня. Порядок по убыванию общности: session, module, class, function.
* Сначала будут созданы `autouse=True` фикстуры, потом остальные фикстуры этого же уровня.
* Если `fix1(fix2)`, то сначала будет вызвана `fix2`, потом `fix1`:
    * `fix2` **не может быть меньшего уровня общности**, только того же или более общего.
* При прочем равном фикстуры будут выполняться в том порядке, что описаны в файле `conftest.py`

Давайте не будем писать код так, чтобы нам приходилось понимать в каком порядке применяются фикстуры одного scope в разных файлах. Лучше определите все в едином `conftest.py`.

Попробуйте сами разобраться, в каком порядке будут вызваны фикстуры (и добавлены строки в список `order`:
```python
import pytest

# fixtures documentation order example
order = []

@pytest.fixture(scope="session")
def s1():
    order.append("s1")

@pytest.fixture(scope="module")
def m1():
    order.append("m1")

@pytest.fixture
def f1(f3):
    order.append("f1")

@pytest.fixture
def f3():
    order.append("f3")

@pytest.fixture(autouse=True)
def a1():
    order.append("a1")

@pytest.fixture
def f2():
    order.append("f2")

def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]
```

* Сначала будут идти фикстуры более общего scope: session: s1
* Хоть это и не описано явно, вызовется фикстура уровня module (вызов фикстуры s1 мы тоже могли опустить): m1.
* Потом из фикстур одинакового scope сначала выполнятся с `autouse=True`, мы их не писали, а они есть: a1.
* Если одна фикстура зависит от другой, то сначала разрешатся зависимости: f3, f1.
* Далее фикстуры в том порядке, что описаны: f2.

## QUIZ Какие фикстуры будут вызваны?

Отметьте, какие фикстуры будут вызваны.

Обратите внимание, что по сравнению с примером из предыдущего шага:

* Изменилась одна из фикстур.
* Изменился тест.

```python
import pytest

# fixtures documentation order example
order = []

@pytest.fixture(scope="session")
def s1():
    order.append("s1")

@pytest.fixture(scope="module", autouse=True)
def m1():
    order.append("m1")

@pytest.fixture
def f1(f3):
    order.append("f1")

@pytest.fixture
def f3():
    order.append("f3")

@pytest.fixture(autouse=True)
def a1():
    order.append("a1")

@pytest.fixture
def f2():
    order.append("f2")

def test_order(f1, f2):
    pass
```

A. s1
B. m1
C. a1
D. f1
E. f2
F. f3

SHUFFLE: False
ANSWER: B, C, D, E, F

## SKIP SORT 

Расставьте, в каком порядке будут вызываться фикстуры в тесте:

Обратите внимание, что по сравнению с предыдущим заданием:

* Фикстуры не изменились.
* Изменился тест.

```python
import pytest

# fixtures documentation order example
order = []

@pytest.fixture(scope="session")
def s1():
    order.append("s1")

@pytest.fixture(scope="module", autouse=True)
def m1():
    order.append("m1")

@pytest.fixture
def f1(f3):
    order.append("f1")

@pytest.fixture
def f3():
    order.append("f3")

@pytest.fixture(autouse=True)
def a1():
    order.append("a1")

@pytest.fixture
def f2():
    order.append("f2")

def test_order(f2, f1, s1):
    pass
```

ANSWER:     assert order == ["s1", "m1", "a1", "f2", "f3", "f1"]

## Возвращаемое значение

Модифицируем этот пример. Пусть каждая фикстура печатает `call имя фикстуры` и возвращает строку *имя фикстуры*. В тестовую функцию добавим печать `Run имя функции`.

Если у вас "ничего не печатает", сделайте тест Fail, дописав в него `assert False` (эту версию мы приведем ниже). Или поищите, с какими аргументами запускать pytest, чтобы stdout не перехватывался тестами, а выводился на печать (будет в рецептах).

```python
import pytest

@pytest.fixture(scope="session")
def s1():
    print('call s1')
    return 's1'

@pytest.fixture(scope="module", autouse=True)
def m1():
    print('call m1')
    return 'm1'

@pytest.fixture
def f1(f3):
    print('call f1')
    return 'f1' + f3

@pytest.fixture
def f3():
    print('call f3')
    return 'f3'

@pytest.fixture(autouse=True)
def a1():
    print('call a1')
    return 'a1'

@pytest.fixture
def f2():
    print('call f2')
    return 'f2'

def test_value(s1, f1, f2):
    print('Run test_value')
    print(f'{s1=} {m1=} {a1=} {f1=} {f2=}')
    assert False
```
Напечатает
```python
------------------------- Captured stdout setup --------------------------
call s1
call m1
call a1
call f3
call f1
call f2
-------------------------- Captured stdout call --------------------------
Run test_value
s1='s1' m1=<function m1 at 0x00000222BF9AD480> a1=<function a1 at 0x00000222BF9ADCF0> f1='f1f3' f2='f2'
======================== short test summary info =========================
FAILED test_fixture/test_fixture_order_print.py::test_value - assert False
```

* Разделен вывод при инициализации фикстур (Captured stdout setup) и собственно работы теста (Captured stdout call)
* Все фикстуры, которые вызывались как аргументы функции, имеют возвращаемое значение - строка с именем функции.
* `autouse=True` фикстуры доступны как функции-объекты, а не возвращаемое ими значение (хм, может эти функции можно явно вызывать?)

Изменим только тестовую функцию. Добавим в нее вызов функций `m1` и `a1`:
```python
def test_value(s1, f1, f2):
    print('Run test_value')
    print(f'{s1=} {m1=} {a1=} {f1=} {f2=}')
    res = m1()
    print('result of m1 = {res}')
    res = a1()
    print('result of a1 = {res}')
    assert False

```
Это не очень хорошая идея. Так нам написали при запуске этого кода. **Не надо явно запускать фикстуры**. Они работают по-другому.
```
_______________________________ test_value _______________________________
Fixture "m1" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
```

## usefixtures

Раньше мы упоминали, что фикстуры, вызванные через `@pytest.mark.usefixtures` не возвращают "правильное" значение. Проверим это утверждение.

Добавим в фикстуры фикстуру класса:
```python
@pytest.fixture(scope="class")
def c1():
    print('call c1')
    return 'c1'
```
и вызовем её для набора тестов
```python
@pytest.mark.usefixtures('c1')
class TestReturnValue:
    def test_method(self, f1):
        print(f'test_method: f1={f1}')
        print(f'test_method: m1={m1}')
        print(f'test_method: c1={c1}')
        assert False
```
Видно, что `с1`, как и `m1` доступны не как возвращаемые значения, а как фукнции-объекты:
```
------------------------- Captured stdout setup --------------------------
call m1
call c1
call a1
call f3
call f1
-------------------------- Captured stdout call --------------------------
test_method: f1=f1f3
test_method: m1=<function m1 at 0x000001BB6A76D7E0>
test_method: c1=<function c1 at 0x000001BB6A76DCF0>
```

Еще раз подчеркнем, что только для явно передаваемых в аргументах функции фикстур доступны возвращаемые значения. Остальные фикстуры неявно вызываются для побочного результата (setup/cleanup).

## Область видимости

В директории `return_value` разделим код на файл `conftest.py` с фикстурами и файл `test_return_value.py` с тестовыми функциями и классами.

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def s1():
    print('call s1')
    return 's1'

@pytest.fixture(scope="module", autouse=True)
def m1():
    print('call m1')
    return 'm1'
    
@pytest.fixture(scope="class")
def c1():
    print('call c1')
    return 'c1'

@pytest.fixture
def f1(f3):
    print('call f1')
    return 'f1' + f3

@pytest.fixture
def f3():
    print('call f3')
    return 'f3'

@pytest.fixture(autouse=True)
def a1():
    print('call a1')
    return 'a1'

@pytest.fixture
def f2():
    print('call f2')
    return 'f2'
```
В файле оставим только тесты:
```python
# test_return_value.py
import pytest

def test_value_implict(s1, f1, f2):
    print('Run test_value_implict')
    print(f'{s1=} {a1=} {f1=} {f2=}')
    assert False

def test_value_explict(s1, f1, f2, m1, a1):
    print('Run test_value_explict')
    print(f'{s1=} {m1=} {a1=} {f1=} {f2=}')
    assert False
    
@pytest.mark.usefixtures('c1')
class TestReturnValue:
    def test_method(self, f1):
        print(f'test_method: f1={f1}')
        assert False
```

Будем запускать тест за тестом и смотреть на результат.

`pytest retrun_value\test_return_value.py::test_value_implict`

Хотя фикстура `a1` выполнилась, даже упоминание о ней в другом файле привело к `NameError`.
```python
------------------------- Captured stdout setup --------------------------
call s1
call m1
call a1
call f3
call f1
call f2
-------------------------- Captured stdout call --------------------------
Run test_value_implict
======================== short test summary info =========================
FAILED retrun_value/test_return_value.py::test_value_implict - NameError: name 'a1' is not defined
```
Правильно, мы уже знаем, что только явно передаваемые в аргументах **функции** фикстуры доступны по возвращаемому значению. Все остальное - от лукавого. Фикстура `a1` была выполнена, как и фикстура `m1` (потому что `autouse=True`). 

Нужны значения фикстур? Не ленись, пиши их в аргументах! *Фикстуры, которые прописывают `request.cls.имя_переменной` мы одобряем только для глобальных вещей: запущенного браузера, соединения с БД и тп, остальное лучше явно запишите в аргументах. Помните, тесты пишутся не только для тестировщиков. Если тест упал, то дайте разработчику ваш тест, пусть он запускает его локально и фиксит баг. Быть может ваш проект написан не на питоне и программист не знает питон. Как не знает фикстур. Появление посреди чистого поля переменных класса без конструктора, который не от чего не наследован, ввергает программиста в недоумение. Пожалейте его мозг. Ему ещё баг фиксить.*

Тут мы видим, что все переданные в аргументах фикстуры доступны (даже `с1` c `scope=class`, хотя функция вне класса).

```python
def test_value_explict(s1, f1, f2, m1, a1, c1):
    print('Run test_value_explict')
    print(f'{s1=} {m1=} {c1=} {a1=} {f1=} {f2=}')
    assert False
```
Вызов `pytest retrun_value\test_return_value.py::test_value_explict` приведет к:
```python
------------------------- Captured stdout setup --------------------------
call s1
call m1
call c1
call a1
call f3
call f1
call f2
-------------------------- Captured stdout call --------------------------
Run test_value_explict
s1='s1' m1='m1' c1='c1' a1='a1' f1='f1f3' f2='f2'
```
Все доступно. 

Вывод: если при использовании фикстуры в функции у вас возник `NameError`, может быть это использование фикстуры, которую вы не указали в аргументах (т.е. проблема не в "не видно", а "не может быть доступно возвращаемое значение").

## Фикстура получает значение из переменной модуля или класса

Пусть наша фикстура может устанавливать соединение с сервером, которое мы потом тестируем. В разных модулях мы хотим тестировать соединения с разными серверами. Как это сделать? Один из вариантов - в модуле указывать значение переменной, а в фикстуре использовать его значение. Если переменной нет, устанавливаем значение по умолчанию.

```python
# conftest.py
@pytest.fixture(scope='module')
def module_variable(request):
    current_host = getattr(request.module, "host", "gmail.com")
    # тут мы можем установить соединение current_host
    print(f'connect to {current_host=}')
```
Файл `test_default.py`, в нем нет переменной `host` и используется значение по умолчанию:
```python
# test_one.py
def test_default_value(module_variable):
    assert False
```
Получаем при запуске `pytest test_one.py`сообщение:
```
connect to current_host='gmail.com'
```
В файле `test_two.py` установим значение переменной `host`:
```python
# test_two.py
# не изменять имя переменной! Используется в фикстуре module_variable
host = 'mipt.ru'

def test_default_value(module_variable):
    assert False
```
Получаем при запуске `pytest test_one.py`сообщение:
```
connect to current_host='mipt.ru'
```

Этот прием понижает читаемость кода, не злоупотребляйте им. Обязательно комментируйте использование таких переменных.

## Итоги

* Фикстура - это функция с декоратором `@pytest.fixture`

* Одна фикстура может в аргументах вызвать другую фикстуру.

* Имя фикстуры передается в аргументах тестовой функции. Значение фикстуры - что вернула функция-фикстура.

* Для класса или модуля для вызова фикстуры используют `@pytest.mark.usefixtures("имя фикстуры")`. Возвращаемое значение недоступно.

* Аргумент `scope` (`function`, `class`, `module`, `session`) - определяет когда **исполняется** код функции-фикстуры.

* Аргумент `autouse=True` позволяет вызывать фикстуры неявно, без передачи ее в аргументы или `usefixtures`.

* В тестовом классе не должно быть конструктора. `request.cls.имя_переменной` в фикстуре класса позволяет без конструктора создать переменную класса и инициализировать ее. Дальнейшее использование в классе как `self.имя_переменной` или `cls.имя_переменной`. `request` передаем аргументом в фикстуру.

* Использование в фикстуре переменных модуля через `request.module.имя_переменной`