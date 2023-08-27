# Рецепты: фабрика данных

lesson = 1056220

## Фабрика данных

Простейшая фабрика данных, выдает логин и пароль. Логин зависит от текущего времени, что делает его достаточно уникальным.

```python
@pytest.fixture
def generate_data():
    login = f"autotest_{time.time()}@hyper.org"     # Генерирует логин
    password = "512" # Назначает пароль
    return {'login': login, 'password': password}   # Возвращает логин и пароль в виде словаря
```

## Фабрика-фикстура

Шаблон **фабрика-фикстура** может помочь в ситуациях, когда результат, возвращаемый фикстурой используется много раз в отдельном тесте. Суть в том, что вместо того, чтобы напрямую возвращать данные, **фикстура возвращает функцию, которая генерирует данные**. И затем эта функция может быть неоднократно вызвана в тесте.

```python
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
```
Если нужно, добавляем финализатор, который удалит данные после окончания тестов.

```python
@pytest.fixture
def make_customer_record():

    created_records = []

    def _make_customer_record(name):
        record = models.Customer(name=name, orders=[])
        created_records.append(record)
        return record

    yield _make_customer_record

    for record in created_records:
        record.destroy()


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
```