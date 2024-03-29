# Вариант 5 (декабрь)

lesson = 1157687

## TASKINLINE Задача 1.5

Даны целые числа **a** и **b**. Чему равно значение выражения 
 $$a^3 + 7^b$$
 
CONFIG
score: 5
TEST
2
7
----
823551
====
-5
11
----
1977326618
====

## TASKINLINE Задача 3.3

В Великобритании используются следующие единицы измерения:

![british_units](https://stepik.org/media/attachments/lesson/1157462/british_units.jpg)

В Америке принято расход бензина автомобилем измерять в `mpg` (miles per gallon). В Европе - сколько км проедет на 1 литре бензина `kml`. 

Дано: `mpg` первого автомобиля на одной строке и `kml` второго автомобиля на другой строке.

Напечатайте по одному числу на строке:

* расход первого автомобиля в км/л
* расход второго автомобиля в км/л
* 1 или 2 - какой автомобиль расходует бензина меньше (экономичнее).

Таблица перевода

* 1 миля (mile) = 1.609344 км
* 1 галлон (gallon) = 4.4 литра

CONFIG
checker: std_float_seq
TEST
22.6
8.3
----
8.266176
8.3
1
====
25.2
11.1
----
9.217151999999999
11.1
1
====
15
4.25
----
5.4864
4.25
2
====
33
12
----
12.07008
12.0
2
====

## TASKINLINE arr_mk_6 Вариант 6

Даны целые числа.

Написать программу, которая печатает все числа $0 \le x \le 10$.

TEST
10 -1 7 31 0 23 1 4 88 5
----
10 7 0 1 4 5
====
11 0 2 3 4 5 6 7 8 9
----
0 2 3 4 5 6 7 8 9
====
1 2 3 4 5 6 7 8 9 0
----
1 2 3 4 5 6 7 8 9 0
====
1 2 3 4 0 6 7 8 9 11
----
1 2 3 4 0 6 7 8 9
====

## TASKINLINE Вариант 5, задача 2

Последовательность называется **палиндром**, если последовательность одинаковая справа налево и слева направо.

Даны числа. Напечатайте YES, если последовательность палиндром, иначе напечатайте NO.


* Палиндром:
    * 1 42 5 42 1
    * 1 9 2 8 3 7 7 3 8 2 9 1
    * 82 (одно число всегда палиндром)
* Не палиндром:
    * 1 37 4 1 37 4 
    * 1 7 -4 16

TEST
1 42 5 42 1
----
YES
====
1 9 2 8 3 7 7 3 8 2 9 1
----
YES
====
82
----
YES
====
1 37 4 1 37 4 
----
NO
====
1 7 -4 16
----
NO
====

