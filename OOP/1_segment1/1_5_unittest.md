# unittest

lesson = 530843

## Тестирование классов и методов

У нас есть отдельный файл `test_segment1.py`. В нем собраны тесты по методам класса `Segment1`.

Хочу удобно:

* Запускать все или 1 тест.
* Получать статус прохождения теста.
* Легко запускать все тесты по всем классам, которые я напишу в разных файлах.

Для этого существуют специальные библиотеки для тестирования. Одна из них **unittest**. Она сразу устанавливается на компьютер вместе с python. Ничего дополнительно устанавливать не нужно.

* [Официальная документация по unittest](https://docs.python.org/3/library/unittest.html)
* [Тьюториал по unittest](http://devpractice.ru/python-unittest-lessons/) на русском языке. Специально взяты примеры оттуда, чтобы вы могли прочитать подробные объяснения, а не краткий пересказ.


## Что тестируем?

Пусть у нас есть методы. Потом мы их будем тестировать.

Файл **calc.py**
```python
def add(a, b):
    return a + b
    
def sub(a, b):
    return a-b
 
def mul(a, b):
    return a * b
 
def div(a, b):
    return a / b
```

Напишем тесты, используя unittest и сохраним в файле **test_calc.py**

```python
import unittest     # мы используем unittest, не забудьте этот import
import calc         # тестируем calc.py
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main()
```

## Запускаем тесты

* в командной строке все тесты из файла `test_calc.py`
```python
python test_calc.py
```
или запускаем unittest как модуль:
```python
python -m unittest test_calc.py
```
Получили:
```cpp
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```

### Запуск с ключом -v

Очень мало информации. Хочу больше! Запустим с ключом **-v** (verbose)
```cpp
python test_calc.py -v
```
или 
```python
python -m unittest -v test_calc.py
```
Получим
```cpp
test_add (test_calc.CalcTest) ... ok
test_div (test_calc.CalcTest) ... ok
test_mul (test_calc.CalcTest) ... ok
test_sub (test_calc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```

## Выборочный запуск

* файл с тестами должен называться **test**`_имя.py`, например, `test_calc.py` или `test_segment1.py`
* функция должна называться с **test_**, например `test_add`
* Название класса должно оканчиваться на **Tests**, например, `CalcTest`

### Запуск всех функций 1 файла test_calc.py

```cpp
python -m unittest -v test_calc.py
```

### Запуск 1 класса тестов из файла

В файле могут быть 2 класса. Если мы хотим разбить тесты по группам тестов, объедините каждую группу в отдельный класс и запускайте отдельными группами. 

Имя класса должно оканчиваться на `Test` и он должен быть наследником класса TestCase пакета unittest. О наследовании расскажем позже. Пока запомните, что класс нужно писать так:
```python
class CalcTests(unittest.TestCase):
```

Запускаем 1 класс из файла:
```python
python -m unittest test_calc.CalcTest
```

### Запуск 1 теста

Запустим 1 тест `test_sub`. Он находится в классе `CalcTest` в файле `test_calc.py`

```python
python -m unittest test_calc.CalcTest.test_sub
```

### Запускаем всех файлов с тестами

```cpp
python -m unittest
```
или (эквивалентно)
```cpp
python -m unittest discover
```

### Запуск файлов из директории с указанием маски

Запустить все файлы из директории `my_project_directory`, которые оканчиваются на `_test.py`
```cpp
python -m unittest discover my_project_directory "*_test.py"
```

## assert

В unittest используются свои assert.

<table>
<tbody>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual"><span style="font-weight: 400;">assertEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">a == b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual"><span style="font-weight: 400;">assertNotEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">a != b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue"><span style="font-weight: 400;">assertTrue(x)</span></a></td>
<td><span style="font-weight: 400;">bool(x) is True</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse"><span style="font-weight: 400;">assertFalse(x)</span></a></td>
<td><span style="font-weight: 400;">bool(x) is False</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs"><span style="font-weight: 400;">assertIs(a, b)</span></a></td>
<td><span style="font-weight: 400;">a is b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot"><span style="font-weight: 400;">assertIsNot(a, b)</span></a></td>
<td><span style="font-weight: 400;">a is not b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone"><span style="font-weight: 400;">assertIsNone(x)</span></a></td>
<td><span style="font-weight: 400;">x is None</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone"><span style="font-weight: 400;">assertIsNotNone(x)</span></a></td>
<td><span style="font-weight: 400;">x is not None</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn"><span style="font-weight: 400;">assertIn(a, b)</span></a></td>
<td><span style="font-weight: 400;">a in b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn"><span style="font-weight: 400;">assertNotIn(a, b)</span></a></td>
<td><span style="font-weight: 400;">a not in b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance"><span style="font-weight: 400;">assertIsInstance(a, b)</span></a></td>
<td><span style="font-weight: 400;">isinstance(a, b)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance"><span style="font-weight: 400;">assertNotIsInstance(a, b)</span></a></td>
<td><span style="font-weight: 400;">not isinstance(a, b)</span></td>
</tr>
</tbody>
</table>

Сравнения и поиск:

<table>
<tbody>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual"><span style="font-weight: 400;">assertAlmostEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">round(a-b, 7) == 0</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual"><span style="font-weight: 400;">assertNotAlmostEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">round(a-b, 7) != 0</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater"><span style="font-weight: 400;">assertGreater(a, b)</span></a></td>
<td><span style="font-weight: 400;">a &gt; b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual"><span style="font-weight: 400;">assertGreaterEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">a &gt;= b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess"><span style="font-weight: 400;">assertLess(a, b)</span></a></td>
<td><span style="font-weight: 400;">a &lt; b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual"><span style="font-weight: 400;">assertLessEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">a &lt;= b</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex"><span style="font-weight: 400;">assertRegex(s, r)</span></a></td>
<td><span style="font-weight: 400;">r.search(s)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex"><span style="font-weight: 400;">assertNotRegex(s, r)</span></a></td>
<td><span style="font-weight: 400;">not r.search(s)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual"><span style="font-weight: 400;">assertCountEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">a и b имеют одинаковые элементы (порядок неважен)</span></td>
</tr>
</tbody>
</table>

Типо-зависимые assert&#8217;ы, которые используются при вызове assertEqual(). Приводятся на тот случай, если необходимо использовать конкретный метод.

<table>
<tbody>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual"><span style="font-weight: 400;">assertMultiLineEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">строки (strings)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual"><span style="font-weight: 400;">assertSequenceEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">последовательности (sequences)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual"><span style="font-weight: 400;">assertListEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">списки (lists)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual"><span style="font-weight: 400;">assertTupleEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">кортежи (tuplse)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual"><span style="font-weight: 400;">assertSetEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">множества или неизменяемые множества (frozensets)</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual"><span style="font-weight: 400;">assertDictEqual(a, b)</span></a></td>
<td><span style="font-weight: 400;">словари (dicts)</span></td>
</tr>
</tbody>
</table>

Контроль выбрасываемых исключений и warning'ов (да, их тоже нужно проверить!)

<table>
<tbody>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises"><span style="font-weight: 400;">assertRaises(exc, fun, *args, **kwds)</span></a></td>
<td><span style="font-weight: 400;">Функция fun(*args, **kwds) вызывает исключение exc</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex"><span style="font-weight: 400;">assertRaisesRegex(exc, r, fun, *args, **kwds)</span></a></td>
<td><span style="font-weight: 400;">Функция fun(*args, **kwds) вызывает исключение exc, сообщение которого совпадает с регулярным выражением r</span></td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns"><span style="font-weight: 400;">assertWarns(warn, fun, *args, **kwds)</span></a></td>
<td>Функция fun(*args, **kwds)&nbsp;выдает сообщение warn</td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex"><span style="font-weight: 400;">assertWarnsRegex(warn, r, fun, *args, **kwds)</span></a></td>
<td><span style="font-weight: 400;">Функция fun(*args, **kwds)&nbsp;выдает сообщение warn и оно совпадает с регулярным выражением r</span></td>
</tr>
</tbody>
</table>




## Задача

* Перепишите наш файл `test_segment1.py` так, чтобы его можно было запускать с помощью unittest.
* Запустите файл
* Запустите 1 тест
