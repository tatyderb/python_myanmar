# Управление запуском тестов

lesson = 1037731

## Структура проекта с тестами

При развитии любого проекта новая функциональность или фикс бага может поломать работающий код. Чтобы быстро обнаружить это, надо запускать ранее написанные тесты. Тестовые фреймворки позволяют это делать удобно и хранить тесты отдельно от тестируемого кода.

Если не указан конкретный файл, при запуске pytest происходит поиск тестов (test discovery) по [следующим правилам](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#test-discovery):

* От текущей директории с поддиректориями,
* во всех файлах `test_*.py` и `*_test.py`,
* функции, начинающиеся с `test` вне классов,
* внутри классов, начинающихся с `Test`, функции и методы, начинающиеся с `test` (включая статические методы и методы класса). **В этом классе НЕ должно быть функции `__init__`**

То есть в проекте стоит организовать директорию `test` или на одном уровне с директорией `src`, или в пакете предусмотреть отдельную папку `test`:

### Тесты вне приложения

Структура проекта с пакетом `mypkg`, где `test` или на одном уровне с директорией `src`:
```
pyproject.toml
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
    ...
```

В тестах если пишете `import mypkg`, убедитесь, что директория `src` в переменной окружения `PYTHONPATH`, перед директорией с `pytest`. 

*Если у вас что-то не находится, посмотрите значение `sys.path` (он же переменная окружения `PYTHONPATH`).*

Если вы запускаете pytest из командной строки, рекомендуем запускать как 
```python
python -m pytest аргументы как раньше
```
Такой способ запуска добавляет [текущую директорию в путь](https://docs.pytest.org/en/7.4.x/explanation/pythonpath.html#pytest-vs-python-m-pytest)

### Тесты как часть приложения

Структура проекта с пакетом `mypkg`, где `test` отдельной папкой:

```python
pyproject.toml
[src/]mypkg/
    __init__.py
    app.py
    view.py
    tests/
        __init__.py
        test_app.py
        test_view.py
        ...
```

## Структура тестов (раздел для QA)

Если вы тестируете ендпоинты, GUI и тп. стоит разнести отдельно тесты, отдельно описание, как работать с объектом.

Пусть нужно протестировать пополнение банковского счета с помощью ендпоинта `POST /v1/deposit`. Тогда структура директорий может быть следующая:

```
autotest/
    object/
        deposit.py
    test/
        test_deposit.py
```

В `test_deposit.py` записываем собственно тесты: можно пополнить баланс и он изменится; нельзя пополнить меньше какого-то лимита; нельзя пополнить на отрицательное число, незалогированному пользователю и тп.

В `deposit.py` на каждый ендпоинт пишем минимум 3 функции или метода:

* просто вызов эндпоинта и возврат результатов, например, `deposit_request` или `deposit_post`
* проверка, что вернул эндпоинт, `deposit_check`
* *быть может еще одна подробная проверка, что записано в БД, логи и тп - опционально, например `deposit_full_check`*,
* обертка, вызывающая ендпоинт и немного проверяющая результат вызова (как минимум, что вернул 2хх и в теле нет "error")

Тогда тест на вывод средств с баланса пишется с акцентом на проверку именно вывода, но автоматически падает, если не работает логин или пополнение:
```python
def test_withdraw_nomoney():
    login(user, password)
    deposit(amount=100)
    
    response = withdraw_request(amount=150)
    withdraw_check(response, expected_exit_code = 403, expected_error='Недостаточно средств')
```

## Запуск тестовых функций, совпадающих с шаблоном

Вместо этой опции я обычно использую **grep** или поиск по файлам в директории в редакторе. Но почему бы не поискать из командной строки средствами pytest со связками or и and?

Лучше всего сначала проверить, правильно ли отработали условия, не запуская тесты, а только **перечислить тесты, которые будут найдены**. Для этого в командной строке укажите опцию `--collect-only`

`-k выражение` - взять все тесты, суффиксы или префиксы которых совпадают с выражением. Можно использовать `or` и `and`.

Например, `pytest -k "asdict or defaults" --collect-only` даст совпадение как с `test_asdict`, так и с `test_defaults`:

```
=================== test session starts ===================
collected 6 items
<Module 'tasks/test_four.py'>
  <Function 'test_asdict'>
<Module 'tasks/test_three.py'>
  <Function 'test_defaults'>

=================== 4 tests deselected ====================
============== 4 deselected in 0.03 seconds ===============
```

## mark - маркеры

Некоторые тесты идут очень долго, и я их не хочу вставлять в CI/CD. А иногда я вручную запускаю длинные тесты в ночь с пятницы на понедельник.

Некоторые тесты требуют доступ к БД и я их не хочу запускать на сервере, где нет доступа к БД.

Хочется отдельные тесты пометить, что они должны запускаться в начале регрессионного тестирования.

Для всего этого есть маркер `mark`. Пометьте одной или несколькими маркерами тест или тестовый класс и управляйте запуском по меткам из командной строки.

Добавим маркер тестам, которые требуют для выполнения БД. Придумаем ему имя `database_access`.

Напишем перед тестом `@pytest.mark.database_access`

* `pytest -m database_access` - запуск всех тестов с маркером  `database_access`
* `pytest -m "not database_access"` - запуск всех тестов БЕЗ маркера  `database_access`

Связки `or` и `and` тоже работают.

**К одному тесту можно применить несколько маркеров**. Например, это тест веб-GUI и он очень долгий.

### Уже существующие маркеры

Существуют уже определенные маркеры, которые используют, например, для пропуска теста:
```python
@pytest.mark.skip()
@pytest.mark.skip(reason='not supported until version 0.2.0')
@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
@pytest.mark.xfail(tasks.__version__ < '0.2.0',                          
                   reason='not supported until version 0.2.0')    # ожидаю assert False

```
* `skip` - пропустить тест, может иметь аргумент `reason`, в которой можете указать причину пропуска, она будет напечатана в отчете.
* `skipif` - что делать, если вам нужно тестировать новую функциональность, которая появилась у нас только в версии 0.2.0, а при тестировании старых версий, пропускать тесты? поможет маркер skipif.
* `xfail` - expected fail, тест, который ожидается, что упадет. То есть его надо метить не F (упал неожиданно), а тест пройден, если assert выдаст False.

Есть и другие маркеры, о них почитайте в документации по pytest.

Зачем нужен маркер **xfail**? Пусть у вас есть баги В1 и В2, которые ломают некоторые тесты. Вы проверяете, что починили баг В1, но В2 есть и тесты на него FAILED.

* Вариант 1. Оставляем все как есть, глазами каждый раз смотрим какие тесты упали. Все упавшие тесты относятся к В2 или мы что-то недочинили в В1? Особенно неудобно в CI/CD.
* Вариант 2. Идем во все тесты по В2 и костылим assert руками. Очень неудобно, если в каждом тесте несколько assert.
* Вариант 3. В тесты добавляем `@pytest.mark.xfail(reason='B2')`. После фикса В2 эти тесты должны перейти из статуса xfail в pass, о чем напишет pytest. Проходите по списку таких тестов и исправляете, удаляя статус xfail. Дальше поиском ищете в файлах "reason='B2'" и убеждаетесь, что все тесты исправлены и PASS.                        


### Регистрация маркера

Если мы опечатаемся в командной строке при указании маркера, хочется получить об этом диагностику. Для этого маркеры регистрируют. 

* В корне вашего проекта создайте файл `pytest.ini`, если его еще нет.
* Напишите в нем секцию о зарегистрированных маркерах.

```python
# pytest.ini файл
[pytest]
markers =
    webtest: mark a test as a webtest.
    slowtest: very slow test.
```
Проверим весь список зарегистрированных маркеров, запустив

```python
pytest  --markers
```
получим (строки выдачи обрезаны, чтобы поместить текст в курс):
```
@pytest.mark.webtest: mark a test as a webtest.
@pytest.mark.slowtest: very slow test.
@pytest.mark.filterwarnings(warning): add a warning filter to the given test. s
@pytest.mark.skip(reason=None): skip the given test function with an optional r
@pytest.mark.skipif(condition): skip the given test function if eval(condition)
@pytest.mark.xfail(condition, reason=None, run=True, raises=None, strict=False)
@pytest.mark.parametrize(argnames, argvalues): call a test function multiple ti
@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needin
@pytest.mark.tryfirst: mark a hook implementation function such that the plugin
@pytest.mark.trylast: mark a hook implementation function such that the plugin 
```
При использовании `pytest` с опцией `--strict-markers` опечатка в имени маркера или незарегистрированный маркер рассматривается как ошибка.

### Маркируем все

Кроме маркировки отдельного метода можно **маркировать класс или модуль**.

```python
# content of test_mark_classlevel.py
import pytest

@pytest.mark.webtest
class TestClass:
    def test_startup(self):
        pass

    def test_startup_and_more(self):
        pass
```
Эквивалентно написанию декоратора к обеим методам.

Второй способ маркировать класс: назначить в `pytestmark` один маркер или их список:
```python
class TestClass:
    pytestmark = pytest.mark.webtest        # один маркер
```
или
```python
class TestClass:
    pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]    # оба маркера
```

Для маркировки модуля пишем аналогичный код на уровне модуля:
```python
import pytest
pytestmark = pytest.mark.webtest        # один маркер
```
или
```
pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]
```
В этом случае маркеры будут применяться (слева направо) ко всем функциям и методам модуля.

Взято отсюда: [https://pytest-docs-ru.readthedocs.io/ru/latest/example/markers.html](https://pytest-docs-ru.readthedocs.io/ru/latest/example/markers.html) 