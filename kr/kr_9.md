# Вариант 9

lesson = 846046

## TASKINLINE arr_mk_sum_3 Вариант 9, Задача 1

Даны числа.

Дано число **k**.

Вычислить сумму **k** первых чисел $S_1$ и сумму **k** последних чисел $S_2$.

Напечатать $S_1 - S_2$.

Для `k = 5`

![рисунок](https://stepik.org/media/attachments/lesson/694801/array_5num.png)

(10 + 2 + 7 + 3 + 0) - (2 + -1 + 4 + 8 + 5) = 22 - 18 = 4

TEST
10 2 7 3 0 2 -1 4 8 5
5
----
4
====
1 2 3 4 5 6 7 8 9 10
1
----
-9
====
-10 1 -7 31 0 -2 0 4 -88 -5
2
----
84
====
-1 -2 -3 4 -5 6 -7 8 -9 3
9
----
-4
====

## TASKINLINE Вариант 9, задача 2

Даны числа. 

* Напечатайте индекс **второго** вхождения числа 7. 
* Если число 7 входит только 1 раз, напечатайте `-1`.
* Если числа 7 нет, то напечатайте `-2`.

TEST
3 7 5 10 -2 7 4
----
5
====
3 7 5 10 -2 17 4
----
-1
====
3 -7 5 10 -2 17 4
----
-2
====
7 7 7 7 7 7 7
----
1
====
7 7 1 2 3 4 5
----
1
====
7 1 2 3 4
----
-1
====
7
----
-1
====
0 5 0 7 8 6 1 5 7 2 5 10 9 9 0 4 9 2 10 7
----
8
====
5 6 4 8 7 4 2 6 3 0 0 8 7 8 10 0 3 0 8 1 3 5 4 2 1 4 6 10 1 6
----
12
====

## TASKINLINE Вариант 9, задача 3

Дана строка. Посчитать чего больше:

* Заглавных латинских букв (напечатать `W`)
* прописных латинских букв (напечатать `q`)
* цифр (напечатать `7`)
* прочих символов (напечатать `!`)

Если каких то групп символов одинаково максимальное количество, печатать все обозначения групп в том порядке, что приведены в списке.

Для тех, кто не помнит алфавит:

* `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
* `abcdefghijklmnopqrstuvwxyz`

TEST
QaZwSx 12
----
Wq
====
AAAsss123 ,.
----
Wq7!
====
Hello, world!
----
q
====

## TASKINLINE Вариант 9, задача 4

Отсортируйте по возрастанию импульсы объектов. Для каждого объекта указана его масса и скорость.

Если импульс одинаковый, то сначала идет объект с большей массой.

Дано число N, далее N строк с числами по формату `m v` (все числа целые).

Напечатать характеристики отсортированных объектов по формату
```python
m v импульс
```
CONFIG
visible_tests: 3
TEST
4
30 1
100 3
1 10
2 5
---
2 5 10
1 10 10
30 1 30
100 3 300
====
1
3 5
--- 
3 5 15
====
4
1000000 10
1000000 0
1000000 1
1 1000000
---
1000000 0 0
1000000 1 1000000
1 1000000 1000000
1000000 10 10000000
====
6
1 10
3 4
10 1
2 6
1 5
5 1
---
5 1 5
1 5 5
10 1 10
1 10 10
3 4 12
2 6 12
====

## TASKINLINE Вариант 9, задача 5

В простых кнопочных телефонах, чтобы набрать нужную букву, нужно было много раз нажимать на одну и ту же кнопку.

![кнопочный телефон](https://stepik.org/media/attachments/lesson/846046/phone.jpg)

1 нажатие кнопки 2 давало букву А, 2 нажатия кнопки 2 давало букву Б и так далее.

Напишите какие клавиши надо нажимать, чтобы получить нужную фразу. После ввода каждой буквы будем делать паузу, чтобы при вводе `БА` у нас не ввелось `В`. Поэтому печатать будем цифры как `11 1` для `БА` и `111` для `B`.

| Кнопка | Символы |
|----|----|
| 1  | `.,?!:`  |
| 2  |  `АБВГ` |
| 3  |  `ДЕЖЗ` |
| 4  |  `ИЙКЛ` |
| 5  |  `МНОП` |
| 6  |  `РСТУ` |
| 7  |  `ФХЦЧ`  |
| 8  |  `ШЩЪЫ` |
| 9  |  `ЬЭЮЯ` |
| 0  |  пробел |

Программа должна обрабатывать одинаково большие и маленькие буквы. Символы, которых нет в таблице - игнорировать.

TEST
Привет, питон!
----
5555 6 4 222 33 666 11 0 5555 4 666 555 55 1111
====
АБВГД
----
2 22 222 2222 3
====
21 век
----
0 222 33 444
====
Александр Сергеевич Пушкин родился в 1799 году.
----
2 4444 33 444 66 2 55 3 6 0 66 33 6 2222 33 33 222 4 7777 0 5555 6666 8 444 4 55 0 6 555 3 4 4444 66 9999 0 222 0 0 2222 555 3 6666 1
====


## TASKINLINE Вариант 9, задача 6

Многочлен состоит из слагаемых. Слагаемое - произведение целого числа (коэффициента) на переменную. Переменная обозначается **одной** латинской буквой. Например `12d или `-7z`. Числа могут быть как положительные, так и отрицательные. Слагаемые в многочлене записываются с учетом алфавитной позиции имен переменных `2a+3b+c...`

Слагаемые в результирующем многочлене записываются также с учетом алфавитной позиции имен переменных. 

Реализуйте подстановку в многочлен чисел вместо переменных. 

(1 балл) Реализуйте класс `Polynomial` для хранения одного многочлена. В нем должны быть функции:

* `__init__`
* `__repr__`
* постановки значений, заданных в виде словаря `{'a': 3, 'b':-2}`
* если нужно, другие функции

(1 балл) Напишите тесты для этих функций.

(1 балл) Дан многочлен и подстановки **всех** переменных на следующих строках. Напечатайте результат подстановки (одно число).

**Если основная проблема у вас не классы, а разбор строки, то сделайте хотя бы с только положительными коэффициентами и при этом всегда пишем множитель** `20b+5c+1r`

CONFIG
visible_tests: 3
TEST
2a+6b-7r
a 5
b -1
r 2
----
-10
====
a+b+c
a 1
b 2
c -3
----
0
====
8b-t+3z
b 7
t 10
z 1
----
49
====
2a+3b+4c+z
a 1
b 2
c 3
z 11
----
31
====
-2a-3b-4c
a 1
b 2
c 3
----
-20
====

