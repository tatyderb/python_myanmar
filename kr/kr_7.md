# Вариант 7

lesson = 846044

## TASKINLINE arr_mk_sum_2 Вариант 7, Задача 1

Даны числа.

Вычислить сумму чисел с четными номерами $S_1$ и сумму чисел с нечетными номерами $S_2$.

Напечатать $S_1 - S_2$.

![рисунок](https://stepik.org/media/attachments/lesson/694801/10num.png)

(10 + 7 + 0 + -1 + 8) - (1 + 3 + 2 + 4 + 5) = 24 - 15 = 9

TEST
10 1 7 3 0 2 -1 4 8 5
----
9
====
1 2 3 4 5 6 7 8 9 10
----
-5
====
-10 1 -7 31 0 -2 0 4 -88 -5
----
-134
====
-1 -2 -3 4 -5 6 -7 8 -9 3
----
-44
====

## TASKINLINE Вариант 7 задача 2

Даны числа. Поменяйте местами наибольшее четное с наименьшим нечетным. Если одного из чисел нет, то менять ничего не нужно.

Гарантируется, что числа уникальные.

TEST
1 2 3 4 5 6 7 8 9
----
8 2 3 4 5 6 7 1 9
====
-1 2 -3 4 -5 6 -7 8 -9
----
-1 2 -3 4 -5 6 -7 -9 8
====
3 17 5 -31 63
----
3 17 5 -31 63
====
-4 6 -88 0
----
-4 6 -88 0
====
95 -6 7 812 34 -23 45 111
----
95 -6 7 -23 34 812 45 111
====

## TASKINLINE Вариант 7, задача 3

Номер телефона часто пишут в разных форматах. Телефон можно записать так:
```
8-495-123-45-67
+7-495-123-45-67
+7 495 123-4567
+7 (495) 123-4567
```
и так далее.

Прочитайте номер телефона, уберите из него лишние символы (кроме цифр), замените первую цифру 8 на +7, напечатайте результат.

TEST
8(495)123-45-67
----
+74951234567
====
8 495 408-00-20
----
+74954080020
====
7-4912-23-45-67
----
+74912234567
====
+7 495 123-0001
----
+74951230001
====
+7 (4912) 98-13-24
----
+74912981324
====
+74912981324
----
+74912981324
====

## TASKINLINE Вариант 7, задача 4

Семья хочет купить участок земли наибольшей площади и при этом с наименьшей длиной забора.

Все участки в форме прямоугольников, чьи стороны параллельны осям Х и Y. Участки заданы x и y координатой левой верхней и правой нижней вершины.

* Отсортируйте участки, которые им предлагают, по убыванию площади;
* при равной площади - по возрастанию периметра;
* при одинаковых площади и периметре - по убыванию длины стороны параллельной оси Y.

Дано N, далее N строк с данными огородов, по 1 прямоугольнику на строку: через побел `xlt ylt xrb yrb` (целые числа) - координаты левой верхней (left top) и правой нижней (right bottom) вершины прямоугольника.

Напечатать отсортированные прямоугольники, по 1 прямоугольнику на строку, в формате 

`xlt ylt xrb yrb площадь периметр`

CONFIG
visible_tests: 3
TEST
5
1 800 11 700
0 50 20 0
3 17 8 10
0 20 50 0
0 40 30 0
---
0 40 30 0 1200 140
0 50 20 0 1000 140
0 20 50 0 1000 140
1 800 11 700 1000 220
3 17 8 10 35 24
====
1
1 20 10 3 
---
1 20 10 3 153 52
====
2
100 200 1000 17
0 100000 100000 0
---
0 100000 100000 0 10000000000 400000
100 200 1000 17 164700 2166
====
6
100 200 1000 17
0 100000 100000 0
0 99999 99999 0
0 555 100000 553
1000 100000 1001 0
0 100000 100 0
---
0 100000 100000 0 10000000000 400000
0 99999 99999 0 9999800001 399996
0 100000 100 0 10000000 200200
0 555 100000 553 200000 200004
100 200 1000 17 164700 2166
1000 100000 1001 0 100000 200002
====

## TASKINLINE Вариант 7, задача 5

Дан список людей. Вывести в алфавитном порядке список людей, у которых email в домене `example.org`

Если таких людей нет, напишите `NO`.

Прочитать данные можно так:
```python
import json
import sys
d = json.load(sys.stdin)
```

CONFIG
visible_tests: 3
TEST
[{"name": "Timothy Wilson", "job": "Adult guidance worker", "email": "bobby33@example.org"}, 
{"name": "Lisa Martin", "job": "Horticulturist, amenity", "email": "lmartin@gmail.com"}, 
{"name": "Michelle Schroeder", "job": "Dietitian", "email": "russoshannon@example.net"}, 
{"name": "Abigail Arellano", "job": "Animal nutritionist", "email": "anutr@gmail.it"}, 
{"name": "Shelly Holt", "job": "Editor, magazine features", "email": "stephaniepeters@example.org"}, 
{"name": "Don Collins", "job": "Administrator, education", "email": "kevin83@example.net"}, 
{"name": "Valerie Macias", "job": "Government social research officer", "email": "test@example.org"}
]
----
Shelly Holt
Timothy Wilson
Valerie Macias
====
[{"name": "Angela Chavez", "job": "Pharmacologist", "email": "daniel74@example.net"}, {"name": "Brian Fox", "job": "Tour manager", "email": "garciarebecca@example.net"}, {"name": "Christopher Moore", "job": "Musician", "email": "adam12@example.org"}, {"name": "Gerald Wagner", "job": "Psychologist, prison and probation services", "email": "arnoldtracy@example.org"}, {"name": "Darryl Mckinney", "job": "Financial adviser", "email": "atorres@example.org"}, {"name": "Julie Hudson", "job": "Psychologist, occupational", "email": "erin11@example.com"}, {"name": "Melissa Tran", "job": "Careers information officer", "email": "anthonybeltran@example.com"}, {"name": "Jonathan Smith", "job": "Higher education lecturer", "email": "ndurham@example.net"}, {"name": "Joseph Hanson", "job": "Operational researcher", "email": "stephen77@example.org"}, {"name": "Charles Mcdonald", "job": "Health promotion specialist", "email": "juliedeleon@example.com"}]
----
Christopher Moore
Darryl Mckinney
Gerald Wagner
Joseph Hanson
====
[{"name": "Timothy Wilson", "job": "Adult guidance worker", "email": "bobby33@example.com"}, 
{"name": "Lisa Martin", "job": "Horticulturist, amenity", "email": "lmartin@gmail.com"}, 
{"name": "Michelle Schroeder", "job": "Dietitian", "email": "russoshannon@example.net"}] 
----
NO
====
[{"name": "Laura Garcia", "job": "Building surveyor", "email": "shawkatherine@example.org"}, {"name": "Willie Brock", "job": "Copywriter, advertising", "email": "christopherlittle@example.org"}, {"name": "Randy Jones", "job": "Dentist", "email": "craigpayne@example.org"}]
----
Laura Garcia
Randy Jones
Willie Brock
====
[{"name": "Laura Garcia", "job": "Building surveyor", "email": "shawkatherine@example.org"}]
----
Laura Garcia
====
[{"name": "Laura Garcia", "job": "Building surveyor", "email": "shawkatherine@python.org"}]
----
NO
====

## TASKINLINE Вариант ?, задача 6

Возьмите задачу у преподавателя.

CONFIG
visible_tests: 1
TEST
1
----
2
====
5
----
73
====
9
----
11
====

## TASKINLINE Вариант 7, задача 6

Многочлен состоит из слагаемых. Слагаемое - произведение целого числа (коэффициента) на переменную. Переменная обозначается **одной** латинской буквой. Например `12d или `-7z`. Числа могут быть как положительные, так и отрицательные. Слагаемые в многочлене записываются с учетом алфавитной позиции имен переменных `2a+3b+c...`

При сложении двух многочленов коэффициенты при одинаковых именах переменных складываются. Слагаемые в результирующем многочлене записываются также с учетом алфавитной позиции имен переменных. 

Например. `2a+6b-7r` складываем с `20b+5c+r`. Результат: `2a+26b+5c+6r`

(1 балл) Реализуйте класс `Polynomial` для хранения одного многочлена. В нем должны быть функции:

* `__init__`
* `__repr__`
* сложения двух многочленов
* если нужно, другие функции

(1 балл) Напишите тесты для этих функций.

(1 балл) Даны два многочлена. Напишите их сумму. **Гарантируется, что в результирующем многочлене останется хотя бы одна переменная.**

**Если основная проблема у вас не классы, а разбор строки, то сделайте хотя бы с только положительными коэффициентами и при этом всегда пишем множитель** `20b+5c+1r`

CONFIG
visible_tests: 3
TEST
2a+6b-7r
20b+5c+r
----
2a+26b+5c-6r
====
a+b+c
x+y+z+5c
----
a+b+6c+x+y+z
====
a+b+z
-a-z
----
b
====
2a+3b+4c
a+2b+3c
----
3a+5b+7c
====
-2a-3b-4c
-a-2b-3c
----
-3a-5b-7c
====
