# Рецепты: setup + cleanup

lesson = 1056219

## Рецепты финализаторов

* Различные синтаксические конструкции приведем на примере из официальной документации для установления SMTP соединения. Хочется уточнений? Читайте официальную документацию. По примерам найдете где это описано.

* Selenium web driver.

* Работа с БД с использованием `psycopg` (СУБД Postgres).

## Финализаторы в фикстурах

Ради чего все это писалось. Чтобы не только автоматически получать соединение с БД, но и автоматически его закрывать. То есть финализировать состояние тестов.

pytest поддерживает выполнение фикстурами специфического завершающего кода при выходе из области действия. Если вы используете оператор **yield вместо return**, то весь код после `yield` выполняет роль «уборщика»:

```python
# conftest.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    // открываем smtp соединение
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    
    yield smtp_connection  # возвращает значение фикстуры
    
    // закрываем smtp соединение
    print("teardown smtp")
    smtp_connection.close()
```
Используем фикстуру в тесте:
```python
# файл test_module.py

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0                            # специально, чтобы тест упал


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0                            # специально, чтобы тест упал 
```
Запустим тест:
```
$ pytest -s -q --tb=no
FFteardown smtp

========================= short test summary info ==========================
FAILED test_module.py::test_ehlo - assert 0
FAILED test_module.py::test_noop - assert 0
2 failed in 0.12s
```
Обратите внимание:

* `teardown smtp` было напечатано один раз, после окончания всех тестов; если сменить на `scope=function`, то вы увидите этот текст дважды, то есть он будет вызываться после каждого теста.

### Использование с оператором **with**

```python
@pytest.fixture(scope="module")
def smtp_connection():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection  # возвращает значение фикстуры
```

После выполнения теста соединение `smtp_connection` будет разорвано, поскольку объект `smtp_connection` автоматически закрывается после завершения выполнения оператора `with`.

Больше примеров по корректному завершению нескольких открытых соединений смотрите в [Использование финализатора менеджера контекста contextlib.ExitStack](https://pytest-docs-ru.readthedocs.io/ru/latest/fixture.html#finalization)

## Фикстуры для работы с БД

Предположим, что СУБД Postgres и для работы с ней используем `psycopg` (3).

`conftest.py`:
```python
import psycopg
from psycopg.rows import dict_row
import pytest

@pytest.fixture(scope='session')
def db_conn(env):
    cred = {
        # 'host':   'localhost'
        'hostaddr': '127.0.0.1',
        'port': 5432,
        'dbname': 'users',
        'user': 'pgadmin',
        'password': 'pgpassword'
    }
    with psycopg.connect(**cred, row_factory=dict_row, autocommit=True) as conn:
        yield conn

@pytest.fixture(scope='function')
def db_cur(db_conn):
    with db_conn.cursor() as cur:  # row_factory=dict_row
        yield cur
        cur.connection.commit()
```
Использование в тестах:
```python
def test_use_db(db_cur):
    db_cur.excecute("SELECT * FROM users WHERE login='test@xyz.aa';")
```

Заметим, что:

* Если хост доступается по IP, то адрес указываем как `hostaddr`, если указываем имя хоста, то `host`.
* `row_factory=dict_row` позволяют получать результаты `SELECT` в удобном для дальнейшей обработке виде (список словарей, где ключ - название поля), его можно указать как аргумент для всего соединения, так и для отдельного курсора.
```python
[{'id': 46536242, 'login': 'test@xyz.aa'}, {'id': 46536256, 'login': 'taty@xyz.aa'}]
```
* Соединение устанавливаем и закрываем один раз в сессию, а курсор создаем - каждый тест. Если нужно иное поведение, меняйте `scope`.
* Все, что вы сделали в курсоре, остается в курсоре. Чтобы донести изменения до БД нужно сделать `commit`, а чтобы откатить набор изменений - `rollback`. Подробнее об этом читайте в разделах про БД вообще и ваш пакет в частности. Несколько рецептов. Подробные объяснения, уточнения и опровержения можно написать в комментариях к шагу.
    * Если у вас только SELECT, можете вообще забыть о коммитах.
    * Если изменяете значения в БД и после этого делаете SELECT в том же курсоре - работает.
    * Если изменяете значения в БД и после этого вызываете ендпоинт, который формирует данные, то данные будут без изменений, то есть **не работает** без коммита. Подробнее разберем пример ниже.
    * Если написали`autocommit=True`, то использовать `cur.connection.commit()` не нужно.
    * Если написали`autocommit=True`, то каждый `excecute` будет проходить автоматически с коммитом.
    * Если НЕ написали`autocommit=True`, но с`cur.connection.commit()`, то коммит только после выполнения всех `excecute`.
    
### Регистрация и изменения пользователя в БД

Рассмотрим пример, когда в тесте нужно сделать обязательно нового пользователя и добавить ему некоторые свойства, которые можно добавить строго через БД и никак через ендпоинты. То есть сценарий:

1. Регистрация
2. UPDATE
3. Пополнение баланса

Рассмотрим ситуацию, когда вы не написали `autocommit=True` 
    
`conftest.py`:
```python
import psycopg
from psycopg.rows import dict_row
import pytest

@pytest.fixture(scope='session')
def db_conn(env):
    cred = {...}
    with psycopg.connect(**cred, row_factory=dict_row, autocommit=True) as conn:
        yield conn

@pytest.fixture(scope='function')
def db_cur(db_conn):
    with db_conn.cursor() as cur:  # row_factory=dict_row
        yield cur
        cur.connection.commit()
```
Использование в тестах. НЕ работает:
```python
def test_use_db(db_cur):
    session = registration(login='test@xyz.aa', password="1q2w3e')
    db_cur.excecute("UPDATE users SET isTestUser=true WHERE login='test@xyz.aa';")
    session.deposit(100)
```
Так как `cur.connection.commit()` будет работать после теста, то изменения в БД не будут доступны во время запроса `session.deposit(100)`.

Использование в тестах. Работает:
```python
def test_use_db(db_cur):
    session = registration(login='test@xyz.aa', password="1q2w3e')
    db_cur.excecute("UPDATE users SET isTestUser=true WHERE login='test@xyz.aa';")
    db_cur.connection.commit()
    session.deposit(100)
```

## Selenium web driver

conftest.py:
```python
import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class", autouse=True)
def get_driver(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield
    driver.quit()
```
Использование в тестах:
```python
class TestWeb:
    def test_web(self):
        self.driver.get("https://vk.com")
```

Заметьте, что браузер запускается автоматически, один на все тесты этого класса (вот тут одни тесты могут влиять на другие, например, через заполненные cookies. Эти тесты нельзя будет запускать параллельно.

Если запускать браузер на каждый тест, то сильно увеличит время прогона тестов. Но их можно будет запускать в параллель (и сократить время прогона).