# Вариант 6

lesson = 846043

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

## TASKINLINE Вариант 6, задача 3

Дана строка. Большие буквы замените на маленькие, а маленькие на большие. Остальные символы оставьте без изменений.

TEST
VAriAnt 6, tasK 3.
----
vaRIaNT 6, TASk 3.
====
aBCdeFg
----
AbcDEfG
====
12345
----
12345
====
SIMPLE iS bEttEr tHan COmPlEx.
----
simple Is BeTTeR ThAN coMpLeX.
====

## TASKINLINE Вариант 6, задача 4

Семья хочет купить участок земли наибольшей площади и при этом с наименьшей длиной забора.

Отсортируйте участки, которые им предлагают, по убыванию площади. При равной площади сначала идет меньший периметр. При одинаковой площади и периметре - сначала большей ширины.

Дано число N, далее N строк, по 1 строке на участок. Задана длина и ширина участка.

Напечатать отсортированные участки, по 1 строке на участок. Печатать через пробел длину, ширину, площадь и периметр участка.

CONFIG
visible_tests: 3
TEST
5
10 100
50 20
3 7
20 50
40 30
---
40 30 1200 140
50 20 1000 140
20 50 1000 140
10 100 1000 220
3 7 21 20
====
1
1 2
---
1 2 2 6
====
2
100 200
100000 100000
---
100000 100000 10000000000 400000
100 200 20000 600
====
20
82930 89160
28339 16794
90802 76892
29303 81846
20162 91698
35324 1025
81246 10649
5544 21482
58121 99266
79562 24920
20362 82249
73137 92878
45842 66533
70343 2525
37230 55936
51684 15621
99701 61185
34706 10242
44597 7860
90766 31185
----
82930 89160 7394038800 344180
90802 76892 6981947384 335388
73137 92878 6792818286 332030
99701 61185 6100205685 321772
58121 99266 5769439186 314774
45842 66533 3050005786 224750
90766 31185 2830537710 243902
29303 81846 2398333338 222298
37230 55936 2082497280 186332
79562 24920 1982685040 208964
20162 91698 1848815076 223720
20362 82249 1674754138 205222
81246 10649 865188654 183790
51684 15621 807355764 134610
28339 16794 475925166 90266
34706 10242 355458852 89896
44597 7860 350532420 104914
70343 2525 177616075 145736
5544 21482 119096208 54052
35324 1025 36207100 72698
====

## TASKINLINE Вариант 6, задача 5

Дана информация о людях. Вывести по алфавиту все имена, у которых не указан email или указан пустой. Если у всех указан email, вывести `OK` (латинские заглавные буквы!!!).

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
{"name": "Lisa Martin", "job": "Horticulturist, amenity"}, 
{"name": "Michelle Schroeder", "job": "Dietitian", "email": "russoshannon@example.net"}, 
{"name": "Abigail Arellano", "job": "Animal nutritionist", "email": ""}, 
{"name": "Shelly Holt", "job": "Editor, magazine features", "email": "stephaniepeters@example.org"}, 
{"name": "Don Collins", "job": "Administrator, education", "email": "kevin83@example.net"}, 
{"name": "Valerie Macias", "job": "Government social research officer"}
]
----
Abigail Arellano
Lisa Martin
Valerie Macias
====
[{"name": "Angela Chavez", "job": "Pharmacologist", "email": "daniel74@example.net"}, {"name": "Brian Fox", "job": "Tour manager", "email": "garciarebecca@example.net"}, {"name": "Christopher Moore", "job": "Musician", "email": "adam12@example.org"}, {"name": "Gerald Wagner", "job": "Psychologist, prison and probation services", "email": "arnoldtracy@example.org"}, {"name": "Darryl Mckinney", "job": "Financial adviser", "email": "atorres@example.org"}, {"name": "Julie Hudson", "job": "Psychologist, occupational", "email": "erin11@example.com"}, {"name": "Melissa Tran", "job": "Careers information officer", "email": "anthonybeltran@example.com"}, {"name": "Jonathan Smith", "job": "Higher education lecturer", "email": "ndurham@example.net"}, {"name": "Joseph Hanson", "job": "Operational researcher", "email": "stephen77@example.org"}, {"name": "Charles Mcdonald", "job": "Health promotion specialist", "email": "juliedeleon@example.com"}]
----
OK
====
[{"name": "Danny Moss", "job": "Magazine features editor"}, 
{"name": "David Knapp", "job": "Toxicologist"}, 
{"name": "Cody Morrison", "job": "Oceanographer"}]
----
Cody Morrison
Danny Moss
David Knapp
====
[{"name": "Laura Garcia", "job": "Building surveyor", "email": "shawkatherine@example.com"}, {"name": "Willie Brock", "job": "Copywriter, advertising", "email": "christopherlittle@example.net"}, {"name": "Randy Jones", "job": "Dentist", "email": "craigpayne@example.org"}]
----
OK
====
[
{"name": "Laura Garcia", "job": "Building surveyor", "email": ""}, {"name": "Willie Brock", "job": "Copywriter, advertising", "email": ""}, 
{"name": "Randy Jones", "job": "Dentist"}
]
----
Laura Garcia
Randy Jones
Willie Brock
====


## TASKINLINE Вариант 6, задача 6

Смесь состоит из веществ. Каждое вещество обозначается одной латинской большой буквой. Для каждого вещества указана доля в смеси по формату `A-10 D-85 B-5`. Через `:` указан объем вещества.

Например:
```python
12:A-10 D-85 B-5
```
12 литров смеси, вещества A 10%, вещества D 85%, вещества B 5%.

(1 балл) Реализуйте класс `Mixture` для хранения информации об одной смеси. В нем должны быть функции:

* `__init__`
* `__repr__` (компоненты печатать в алфавитном порядке)
* сложение двух смесей
* если нужно, другие функции

(1 балл) Напишите тесты для этих функций.

(1 балл). Используя класс `Mixture` решите задачу:

При смешивании двух смесей никаких реакций не происходит. Объемы компонент остаются без изменений. В результирующей смести появляются все вещества в соответствующих пропорциях.

Например, при сложении 1 литра первой смеси и 2 литров второй смеси 
```python
1:A-30 B-70
2:B-25 C-75
```
получим 3 литра результирующей смеси
```python
3:A-10 B-40 C-50
```

Гарантируется, что в тестах в результирующей смеси доли будут целочисленные.

CONFIG
visible_tests: 3
TEST
1:A-30 B-70
2:B-25 C-75
----
3:A-10 B-40 C-50
====
10:G-90 K-10
10:W-100
----
20:G-45 K-5 W-50
====
4:A-50 B-50
2:A-50 B-50
----
6:A-50 B-50
====
1:A-30 B-70
10:A-30 B-70
----
11:A-30 B-70
====
1:A-50 B-50
1:A-50 G-50
----
2:A-50 B-25 G-25
====