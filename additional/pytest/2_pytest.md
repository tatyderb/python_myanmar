# pytest

lesson = 1029155

## Ресурсы

Подробнее об использовании pytest смотрите на:

* https://docs.pytest.org/ - официальном сайте
    * [https://pytest-docs-ru.readthedocs.io/ru/latest/fixture.html](перевод на русский) официальной документации
* [Python Testing with pytest](https://habr.com/ru/articles/448782/) - перевод на русский замечательной книги по pytest.
* Статьи на Хабре:
    * [Pytest-фикстуры на человеческом](https://habr.com/ru/articles/716248/)
    * [Эффективное тестирование с помощью Pytest](https://habr.com/ru/companies/otus/articles/580212/)
    * []()

## Инсталляция и настройка pytest

Если вы запускаете python из командной строки, то в командной строке напишите :

`pip install -U pytest`

Если работаете в PyCharm, можно в любом файле написать `import pytest`, нажать правой кнопкой мыши на красную лампочку и выбрать пункт меню install pytest.

Так в PyCharm можно инсталлировать недостающий пакет (на примере пакета pygame):

![install into PyCharm](https://stepik.org/media/attachments/lesson/1029155/install_pygame1.png)

PyCharm позволяет запускать кликом мыши текущий файл или текущую функцию в файле. Это очень удобно для создания тестов. Кроме того, можно задать конфигурацию для запуска всех тестов. Для настройки конфигурации запуска выберите меню `Run / Edit Configuration`

![Run / Edit Configuration](https://stepik.org/media/attachments/lesson/1029155/menu_edit_configuration.png)

**Сначала стоит настроить шаблон, по которому будут создаваться автоматически конфигурации по запуску** тестов или кода из контекстного меню (как это делать, расскажем позже).

Изменение шаблона будет влиять только на вновь создаваемые конфигурации, уже созданные останутся как есть.

Выберите внизу ссылку на `Edit Configuration Template`. 

![Edit Configuration Template](https://stepik.org/media/attachments/lesson/1029155/menu_edit_configuration_template.png)


Нажмите на иконку `+` (Add New Configuration или нажмите клавиши Alt+Insert) и в появившемся меню выберите pytest.

![new pytest](https://stepik.org/media/attachments/lesson/1029155/menu_pytest.png)

Здесь стоит задать все опции и переменные окружения для запуска будующих тестов.

## Запуск теста на коленке

Вы пишете функцию `add(a, b)` и до ее реализации хотите написать тесты. Подход TDD (test-driven development) говорит, что сначала стоит написать тесты, которые описывают поведение функции, а потом переходить к ее реализации.

Представим, что наш проект только начинается и мы пишем первые функции и сразу же их тестируем "здесь и сейчас". Организовывать правильную структуру проекта будем потом.

Файл `test_calc.py` с функцией `add` и ее тестами:
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(12, 8) == 20
    assert add(-12, 8) == -4
    assert add(-12, -8) == -20
```

Запуск тестов этого файла из командной строки:
```python
pytest test_calc.py
```

Выведет отчет о тестировании:
```
>pytest test_calc.py
========================= test session starts ==========================
platform win32 -- Python 3.10.2, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\work\demo_test
collected 1 item

test_calc.py .                                                    [100%]

========================== 1 passed in 0.02s ===========================
``` 

Запуск нескольких тестов и разбор отчета будет в следующих шагах.

Запуск из PyCharm:

* **одной функции** - встаньте курсором внутри функции, правой кнопкой мыши вызовите контекстное меню и выберите в нем пункт запуска данной функции `test_add` с помощью pytest.
    * имя функции должно начинаться с `test_`
    * имя файла должно начинаться или заканчиваться на `test`
* **всех функций одного файла** - или встаньте курсором вне функций, или слева на вкладке Project поставьте курсор на файл, кликните правой кнопкой мыши и в появившемся контекстном меню выберите запуск с pytest.
    * имя файла должно начинаться или заканчиваться на `test`
    * аналогично можно запустить все тесты в директории (все файлы и поддиректории), имя директории должно начинаться или заканчиваться на `test`

Запуск теста:
![run pytest from pycharm](https://stepik.org/media/attachments/lesson/1029155/run_pytest_pycharm.png)


Запуск тестов файла (или директории)
![run pytest for file](https://stepik.org/media/attachments/lesson/1029155/run_pytest_pycharm_file.png)

Смешивать тесты и функции, которые они тестируют, в одном файле - не нормально! Тесты должны быть отделены от кода, который они тестируют.

Писать в файле вспомогательные функции для тестирования (сложная проверка результата) и вызывать ее в ряде тестов - нормально.

## Запуск тестов

В примере на один тест не видно, почему удобнее пользоваться тестовыми фреймворками, а не писать тесты прямо в коде и тут же их запускать.

Пусть в файле `calc.py` реализованы функции `add`, `sub`, `mul`, `div`.

В файле `test_calc.py` тесты разбиты на две группы: тесты с целыми числами и тесты с плавающей точкой. Для этого функции тестов объединены в классы `TestCalcInt` и `TestCalcFloat` (**имя класса начинается с `Test`, в нем НЕТ конструктора, функции `__init__`**), для примера сделана еще отдельная функция:

```python
# test_calc.py
import calc

TOLERANCE = 1e-9

# в файле могут быть вспомогательные функции, не тесты
def float_equal(a: float, b: float, tolerance: float = TOLERANCE):
    return abs(a - b) < tolerance
    
# какой-то отдельный тест
def test_something():
    assert (1, 2, 3) == (1, 2, 3)
    
# отдельный тест, который не должен пройти
def test_failed():
    assert (1, 2, 3) == (4, 5)


class TestCalcInt:
    def test_add(self):
        assert calc.add(2, 3) == 5
        assert calc.add(12, 8) == 20
        assert calc.add(-12, 8) == -4
        assert calc.add(-12, -8) == -20
        
    def test_sub(self):
        ...
        
    ...
    
class TestCalcFloat:
    def test_add(self):
        assert float_equal(calc.add(0.1, 0.2), 0.3)
        ...
        
    def test_sub(self):
        ...
        
    ...
   
```

Запускаем тесты:

* `pytest test_calc.py::test_something` - единственная функция `test_something`,
* `pytest test_calc.py::TestCalcInt::test_add` - единственная функция `test_add` из класса `TestCalcInt`,
* `pytest test_calc.py::TestCalcInt` - все методы с именами `test*` или `*test` из класса `TestCalcInt`,
* `pytest test_calc.py` - все функции и методы с именами `test*` или `*test`, то есть все, кроме `float_equal`.
* `pytest` - от текущей директории, во всех директориях рекурсивно запускаем все файлы с подходящими именами.

Осталось файлы с тестами в вашем проекте организовать в директории и запускать прогон всех нужных тестов одним щелчком мыши.

## Структура отчета о тестировании

Пусть в директории `demo_test` кроме файла из предыдущего шага `test_calc.py` лежат файлы

test_one.py
```python
def test_pass():
    assert (1, 2, 3) == (1, 2, 3)
```

test_two.py:
```python
def test_fail():
    assert (1, 2, 3) == (3, 2, 1)

def test_fail_again():
    assert (1, 2, 3) == (4, 5)
```

test_calc.py:
```python
посмотрите на предыдущем шаге
```

При запуске теста `pytest demo_test` получаем отчет о прохождении теста:
```
========================= test session starts ==========================
platform win32 -- Python 3.10.2, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\work\courses_my\_python_myanmar
collected 10 items

additional\pytest\demo_test\test_calc.py .F......                 [ 80%]
additional\pytest\demo_test\test_one.py .                         [ 90%]
additional\pytest\demo_test\test_two.py F                         [100%]

=============================== FAILURES ===============================
_____________________________ test_failed ______________________________

    def test_failed():
>       assert (1, 2, 3) == (4, 5)
E       assert (1, 2, 3) == (4, 5)
E         At index 0 diff: 1 != 4
E         Left contains one more item: 3
E         Use -v to get more diff

additional\pytest\demo_test\test_calc.py:15: AssertionError
______________________________ test_fail _______________________________

    def test_fail():
>       assert (1, 2, 3) == (3, 2, 1)
E       assert (1, 2, 3) == (3, 2, 1)
E         At index 0 diff: 1 != 3
E         Use -v to get more diff

additional\pytest\demo_test\test_two.py:2: AssertionError
======================= short test summary info ========================
FAILED additional/pytest/demo_test/test_calc.py::test_failed - assert ...
FAILED additional/pytest/demo_test/test_two.py::test_fail - assert (1,...
===================== 2 failed, 8 passed in 0.11s ======================
```

Видно, что результат прохождения одного теста в отчете следующая 
```
additional\pytest\demo_test\test_calc.py .F......                 [ 80%]
additional\pytest\demo_test\test_one.py .                         [ 90%]
additional\pytest\demo_test\test_two.py F                         [100%]
```
и показан итог `2 failed, 8 passed in 0.11s`

Статусы окончания теста:

* `.` - тест успешно пройден,
* `F` - failed, тест провалился, 
* `E` - тест вызвал *непредвиденное* исключение,
* `S` - skip - тест не запускался,
* `` - expected fail - ожидалось, что тест провалится, и он это сделал.

## Параметризация

Посмотрим на тест на сложение. По сути он для набора некоторых значений `a`, `b`, `res` выполняет действие
```python
def test_add(a, b, res):
    assert add(a, b) == res
```
Нам повезло, что тест маленький. Если бы у нас тест состоял из 10 действий, то повторение действий для четырех наборов приведет к увеличению кода с помощью copy-paste в 4 раза. 

Можно тестовые действия вынести в отдельную функцию `do_add(a, b, res)` и вызывать ее для разных наборов:
```python
def do_add(a, b, res):
    assert calc.add(a, b) == res
    
def test_add():
   do_add(2, 3, 5)
   do_add(12, 8, 20)
   do_add(-12, 8, -4)
   do_add(-12, -8, -20)
```

По сути это 4 разных мелких теста, но они у нас показываются как единый. Он или весь PASS или весь FAIL. Мы никак из отчета не видим ситуации, что, например, он падает только на одном наборе. Хочется его учитывать как 4 разных микротеста.

Для этого в pytest используют **параметризацию** тестов с помощью `parametrize`. Перепишем тест на сложение через параметризацию. Не забудьте добавить `import pytest` в начало.

```python
class TestCalcInt:
    @pytest.mark.parametrize("a, b, res", [
        (2, 3, 5),
        (12, 8, 20),
        (-12, 8, -5),     # <---- этот тест должен FAIL  
        (-12, -8, -20)
    ])
    def test_add(self, a, b, res):
        assert calc.add(a, b) == res
```
### Как из теста сделать параметрический тест

* добавить `import pytest` в начало файла, если его еще нет,
* добавить `@pytest.mark.parametrize`,
* первым параметром в строке перечислить аргументы через запятую в виде строки,
* второй аргумент - список из тестовых наборов данных.

Запустим тест и посмотрим, как изменился отчет:
```
>pytest test_calc.py::TestCalcInt::test_add
```
получим отчет:
```
========================= test session starts ==========================
platform win32 -- Python 3.10.2, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\work\courses_my\_python_myanmar\additional\pytest\demo_test
collected 4 items

test_calc.py ..F.                                                 [100%]

=============================== FAILURES ===============================
____________________ TestCalcInt.test_add[-12-8--5] ____________________

self = <demo_test.test_calc.TestCalcInt object at 0x0000026DC52AB490>
a = -12, b = 8, res = -5

    @pytest.mark.parametrize("a,b,res", [
        (2, 3, 5),
        (12, 8, 20),
        (-12, 8, -5),
        (-12, -8, -20)
    ])
    def test_add(self, a, b, res):
>       assert calc.add(a, b) == res
E       assert -4 == -5
E        +  where -4 = <function add at 0x0000026DC52A4820>(-12, 8)
E        +    where <function add at 0x0000026DC52A4820> = calc.add

test_calc.py:26: AssertionError
======================= short test summary info ========================
FAILED test_calc.py::TestCalcInt::test_add[-12-8--5] - assert -4 == -5
===================== 1 failed, 3 passed in 0.08s ======================
```

Заметим, что каждый набор данных считается отдельным тестом, то есть в отчете не один тест, а четыре с разными результатами.

### Пример параметризации теста с одним аргументом

Пусть мы тестируем функцию проверки на палиндром:
```python
def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even")

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?")
    
def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")
```
Перепишем в виде параметризованных тестов с единственным параметром - входной строкой.

```python
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)
```

Можно переписать в виде одного параметризованного теста с двумя параметрами, второй - ожидаемый результат.

```python
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
```

## Вызов параметризованного теста из командной строки

Пусть у нас есть параметризованный тест:
```python
@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'brian', False),
                          ('breathe', 'BRIAN', True),
                          ('eat eggs', 'BrIaN', False),
                          ])
def test_add_3(summary, owner, done):
    # в этом разделе нас не интересует, что делает тест
    pass
```
Если мы запустим весь тест с параметрами `pytest -v test_add_variety.py::test_add_3` , он, как мы уже раньше видели, в отчете отразится как 4 разных теста.
```
test_add_variety.py::test_add_3[sleep-None-False] PASSED                 [ 25%]
test_add_variety.py::test_add_3[wake-brian-False] PASSED                 [ 50%]
test_add_variety.py::test_add_3[breathe-BRIAN-True] PASSED               [ 75%]
test_add_variety.py::test_add_3[eat eggs-BrIaN-False] PASSED             [100%]
```
В отчете подсказка как правильно запускать тест с конкретным набором параметров и как указывать аргументы `None` и `False`. Как пишется в отчете, так дальше и запускаем один набор параметров:

`pytest test_add_variety.py::test_add_3[sleep-None-False]`

**Если в значении параметра есть пробелы, то оберните вызов в двойные кавычки.**

`pytest "test_add_variety.py::test_add_3[eat eggs-BrIaN-False]"`

## Тестирование исключений

Ваш код кидает исключения? Не забудьте это протестировать! Поможет [pytest.raises](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises)

```python
import pytest

def test_passes():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0

def test_fails():
    with pytest.raises(Exception) as e_info:
        x = 1 / 1

def test_fails_without_info():
    with pytest.raises(Exception):
        x = 1 / 1

# Don't do this. Assertions are caught as exceptions.
def test_passes_but_should_not():
    try:
        x = 1 / 1
        assert False
    except Exception:
        assert True

# Even if the appropriate exception is caught, it is bad style,
# because the test result is less informative
# than it would be with pytest.raises(e)
# (it just says pass or fail.)

def test_passes_but_bad_style():
    try:
        x = 1 / 0
        assert False
    except ZeroDivisionError:
        assert True

def test_fails_but_bad_style():
    try:
        x = 1 / 1
        assert False
    except ZeroDivisionError:
        assert True
```
Отчет о прохождении тестов:
```
================== test session starts ===================
platform linux2 -- Python 2.7.6 -- py-1.4.26 -- pytest-2.6.4
collected 7 items 

test.py ..FF..F

======================== FAILURES ========================
_______________________ test_fails _________________________

    def test_fails():
        with pytest.raises(Exception) as e_info:
>           x = 1 / 1
E           Failed: DID NOT RAISE

test.py:13: Failed
______________________ test_fails_without_info ___________

    def test_fails_without_info():
        with pytest.raises(Exception):
>           x = 1 / 1
E           Failed: DID NOT RAISE

test.py:17: Failed
_____________________ test_fails_but_bad_style ___________

    def test_fails_but_bad_style():
        try:
            x = 1 / 1
>           assert False
E           assert False

test.py:43: AssertionError
=========== 3 failed, 4 passed in 0.02 seconds =============
```

Взято отсюда: [https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest](https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest)