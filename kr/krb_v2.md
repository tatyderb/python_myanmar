# Вариант 2 (декабрь)

lesson = 1157684

## TASKINLINE Задача 1.2

Даны числа **a** и **b**. Чему равно значение выражения 
 $$2(\frac{a}{5} - \frac{1}{b})$$
 
CONFIG
score: 5
checker: std_float_seq
TEST
2.3
1.4
----
-0.5085714285714287
====
-1.7
-0.2
----
9.32
====

## TASKINLINE Задача 3.2

В Великобритании используются следующие единицы измерения:

![british_units](https://stepik.org/media/attachments/lesson/1157462/british_units.jpg)

Автомобиль ехал со скоростью `v` **км/ч**. Ограничение по скорости на дороге `vmax` **миль/час**.

Дано: v и vmax на одной строке через пробел.

Напечатайте `YES` если автомобиль превысил скорость, `NO` если скорость не была превышена.

1 миля = 1.609344 км

TEST
150 100
----
150
160.9344
NO
====
100 60
----
100
96.56064
YES
====
33 20
----
33
32.18688
YES 
====
16 10
----
16
16.09344
NO
====

## TASKINLINE arr_mk_4 Вариант 2

Даны целые числа.

Написать программу, которая печатает все числа $ \le 0$.

TEST
10 1 7 -31 0 -2 1 4 88 5
----
-31 0 -2
====
0 -1 2 3 4 5 6 7 8 9
----
0 -1
====
0 0 0 0 0 0 0 0 0 0
----
0 0 0 0 0 0 0 0 0 0
====
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
----
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
====

## TASKINLINE Вариант 2, задача 2

Даны целые числа. Напечатайте наибольшее отрицательное число. Если таких чисел нет, напечатайте NO.

TEST
9 -8 7 -6 1 -2 3 -4
----
-2
====
-9 8 -7 6 -1 2 -3 -4
----
-1
====
4 19 23 7 0
----
NO
====
-3 -3 -3 -3
----
-3
====
-5 6 8 -23 17
----
-5
====
6 8 -23 17 -5
----
-5
====