# КР, задача 1

lesson = 

## arr_mk_1 TASKINLINE Вариант 3

Даны целые числа.

Написать программу, которая печатает НОМЕРА элементов с числами, которые равны 0.

TEST
10 2 -7 31 0 2 0 -4 88 5
----
4 6
====
0 2 3 4 5 6 7 8 9 10
----
0
====
1 2 3 4 5 6 7 8 9 0
----
9
====
1 2 3 4 0 6 7 8 9 10
----
4
====

## TASKINLINE arr_mk_2 Вариант 4

Даны целые числа.

Написать программу, которая печатает НОМЕРА элементов с **четными** числами.

TEST
10 1 7 31 0 2 1 4 88 5
----
0 4 5 7 8
====
2 1 1 1 1 1 1 1 1 1
----
0
====
1 1 1 1 1 1 1 1 1 0
----
9
====
1 1 1 1 0 1 1 1 1 1
----
4
====

## TASKINLINE arr_mk_3 Вариант 1

Даны целые числа.

Написать программу, которая печатает все четные числа.

TEST
10 1 7 31 0 2 1 4 88 5
----
10 0 2 4 88
====
2 1 1 1 1 1 1 1 1 1
----
2
====
1 1 1 1 1 1 1 1 1 0
----
0
====
1 1 1 1 0 1 1 1 1 1
----
0
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

## TASKINLINE arr_mk_5 Вариант 5

Даны целые числа.

Написать программу, которая печатает все числа $ \le 10$.

TEST
10 -1 7 31 0 23 1 4 88 5
----
10 -1 7 0 1 4 5
====
1 2 3 4 5 10 11 11 11 11
----
1 2 3 4 5 10
====
11 11 11 11 1 2 3 4 5 10
----
1 2 3 4 5 10
====
10 -10 10 -10 10 -10 10 -10 10 -10
----
10 -10 10 -10 10 -10 10 -10 10 -10
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

## TASKINLINE arr_mk_sum_1 Вариант 1, Задача 2

Даны числа.

Вычислить сумму 5 первых чисел $S_1$ и сумму 5 последних чисел $S_2$.

Напечатать $S_1 - S_2$.

![рисунок](https://stepik.org/media/attachments/lesson/694801/array_5num.png)

(10 + 2 + 7 + 3 + 0) - (2 + -1 + 4 + 8 + 5) = 22 - 18 = 4

TEST
10 2 7 3 0 2 -1 4 8 5
----
4
====
1 2 3 4 5 6 7 8 9 10
----
-25
====
-10 1 -7 31 0 -2 0 4 -88 -5
----
106
====
-1 -2 -3 4 -5 6 -7 8 -9 3
----
-8
====

## TASKINLINE arr_mk_sum_2 Вариант 2, Задача 2

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


## TASKINLINE arr_mk_sum_3 Вариант 4, Задача 2

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

## TASKINLINE arr_mk_13 Вариант 3, задача 2

Даны числа.

Напечатать **сколько** четных чисел < 10.

TEST
10 2 -7 31 0 2 0 -4 88 5
----
5
====
0 2 30 4 50 16 7 -8 -90 11
----
5
====
1 2 3 4 5 6 7 8 9 0
----
5
====
1 2 3 4 20 6 7 8 9 11
----
4
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

## TASKINLINE Вариант 1, задача 3

Дана дробь. Напечатайте десятичную дробь с точностью до 3 знаков после .

```python
x = 12.345678
print(f'{x:.3f}')   # 12.345 - печать с точностью до 3 знаков
```
TEST
17/5
----
3.400
====
1/3
----
0.333
====
100/20
----
5.000
====
0/11
----
0.000
====

## TASKINLINE Вариант 1, задача 3

В России не целые числа пишут через запятую ,

Компьютер пишет числа через точку .

Дано число через запятую. Напечатайте его через точку.

TEST
12,345
----
12.345
====
-153,0
----
-153.0
====
1999,9999997
----
1999.9999997
====

## TASKINLINE Вариант 5, задача 3

Дан пример суммы целых чисел. Напечатайте YES, если он решен правильно, иначе напечатайте NO.

TEST
2 + 13 = 77
----
NO
====
2 + 3 = 5
----
YES
====
5 + 13 = 18
----
YES
====
-3 + -1 = -4
----
YES
====
100 + 1 = 200
----
NO
====

## TASKINLINE Вариант 4, задача 3

Дан email. Напечатайте, из России он (YES) или нет (NO). Email из России, если он заканчивается на `.ru`

TEST
ivanov.ii@mipt.ru
----
YES
====
ivanov@phystech.edu
----
NO
====
muller@gmail.de
----
NO
====
smith@gov.ru.org
----
NO
====
smith@support.gov.ru
----
YES
====

## TASKINLINE Вариант 2, задача 3

Номер карты удобно читать с `-`, например, `1234-5678-9023-1266`.

Дан номер карты с `-`. Напечатайте номер карты без лишних символов, только цифры.

TEST
1234-5678-9023-1266
----
1234567890231266
====
5434-5677-3245-1212-44
----
543456773245121244
====
1-2-3-4-5
----
12345
====
1234567890231266
----
1234567890231266
====

##TASKINLINE Вариант 3, задача 3. Дата

Дана дата в формате `dd/mm/yyyy`. Напечатайте дату в формате `yyyy.mm.dd`.

TEST
06/04/2022
----
2022.04.06
====
31/12/2000
----
2000.12.31
====
1/2/734
----
734.2.1
====