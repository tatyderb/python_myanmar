# Вариант 6 (декабрь)

lesson = 1157688

## TASKINLINE Задача 1.6

Даны целые числа **a** и **b**. Чему равно значение выражения 
 $$a^{3^b}$$
 
CONFIG
score: 5
TEST
7
2
----
40353607
====
-5
3
----
-7450580596923828125
====

## TASKINLINE Задача 3.6 Пройти в дверь

В Великобритании используются следующие единицы измерения:

![british_units](https://stepik.org/media/attachments/lesson/1157462/british_units.jpg)

Высота двери `ft` футов и `inch` дюймов. Рост человека `m` метров `sm` сантиметров.

* 12 inch = 1 ft
* 1 inch = 2.54 сантиметра

Дано (все числа целые):

* на одной строке через пробел `ft inch` высота двери
* на одной строке через пробел `m sm` рост человека

Напечатать:

* высоту двери в сантиметрах
* рост человека в сантиметрах
* `YES`, если человек пройдет в дверь не нагибаясь. Иначе напечатайте `NO`

TEST
5 4
1 60
----
162.56
160
YES
====
6 0
1 87
----
182.88
187
NO
====

## TASKINLINE arr_mk_sum_1 Вариант 6, Задача 1

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

## TASKINLINE Вариант 6, задача 2

Даны оценки (3 или больше штук), отбросить самую маленькую и самую большую оценку и вычислить среднее арифметическое оставшихся.

Результат напечатать с точностью до 3 десятичных цифр после запятой, никаких других округлений делать не надо.

Печать переменной `х` с 3 десятичными цифрами:
```python
print(f'{x:.3f}')
```

TEST
3 4 5 5 5 2
----
4.250
====
10 9 8 7 6 5 4 3 2
----
6.000
====
5 5 5 5 5
----
5.000
====
7 7 7
----
7.000
====
6 9 7
----
7.000
====
1 4 9 5 4 1 1 5 8 8
----
4.500
====


