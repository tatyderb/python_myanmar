# Циклы: задачи на "подумать"

lesson = 1354327

## TASKINLINE Aknights Рыцари и лжецы

На острове Буяне жили **N** человек, каждый из которых был либо рыцарем либо лжецом, встали в круг. 

Рыцари говорят только правду, лжецы всегда только лгут. Каждому человеку в кругу задали вопрос: «Кто ты и кто твой сосед слева: рыцарь или лжец?» При этом каждый человек сказал, что он – рыцарь. А ответы всех людей о левом соседе были записаны в следующем формате: 1 – рыцарь 0 – лжец. Все ответы записаны в строку через пробел. Последний спрошенный человек отвечал на вопрос о первом.

Написать программу, которая по ответам жителей определяет, какое количество рыцарей заведомо присутствует в круге.

CONFIG
score: 15
visible_tests: 4
TEST
4
1 0 1 0
----
2
====
2
0 0
----
1
====
4
1 1 0 0
----
1
=====
255
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
----
0
====
7
1 1 0 0 1 0 0
----
2
====
8
1 1 1 0 0 1 0 0
----
2
====
10
0 0 1 1 0 0 1 1 0 0 1
----
3
====
6
0 1 1 1 1 0 
----
1
====

## TASKINLINE BookOfBooks: страницы книги

Царь Горох решил напечатать книгу книг. Она была отделана золотом и серебром, а цифры, обозначающие страницы, изготавливались из драгоценных камней. Царь Горох использовал десятичную систему счисления.

Известно количество страниц в этой книге (целое число $0 < N < 10^{12}$)

Необходимо эффективно подсчитать сколько всего нужно изготовить цифр для номеров страниц.

Требуется написать программу, которая вычисляет количество цифр, используя наименьшее количество итераций цикла в программе.

Входные данные. Одно целое число -- количество страниц.

Выходные данные. Два числа, разделенных пробелами: количество итераций циклов Вашей программы и количество цифр для нумерации страниц.

CONFIG
score: 15
visible_tests: 6
TEST
100
----
2 192
====
110
----
2 222
====
1000
----
3 2893
====
1998
----
3 6885
====
1000000
----
6 5888896
====
78453100023
----
10 851872989153
====
10
----
1 11
====

## TASKINLINE Abmyax Сверим часы

Бяксику и Мяксику подарили часы с 12-ти часовым циферблатом. Когда они встретились, часы Бяксика показывали **hb** часов и **minb** минут, часы Мяксика **hm** часов и **minm** минут.

Все часы ходили исправно.

Чтобы часы показывали одинаковое время, Бяксик сразу решил перевести их вперед на **hbf** часов и **minbf** минут и также переводить каждые **nb** минут, в Мяксик также сразу решил перевести назад на **hmb** часов и **minmb** минут и также переводить каждые **nm** минут. Ни Бякиск, ни Мяксик не переводили часы более чем на 11 часов 59 минут за один раз.

Написать программу, которая выясняет могут ли Бяксик и Мяксик добиться одинаковых показаний часов хотя бы за неделю. Если могут, то программа должна напечатать количество дней, часов и минут, за которые им это удалось, если нет, то программы печатает "NO".

### Входные данные

```
hb:minb nb hbf:minbf
hm:minm nm hmb:minmb
```

Первая строка: два целых числа, разделенных ":" (показание часов Бяксика), пробел, целое число не более 60 (через сколько минут он переводит часы), далее два целых числа, разделенных ":" (на сколько часов и минут переводит часы)

Вторая строка: два целых числа, разделенных ":" (показание часов Мяксика), пробел, целое число не более 60 (через сколько минут он переводит часы), далее два целых числа, разделенных ":" (на сколько часов и минут переводит часы)

### Выходные данные

Либо три целых числа в формате `dd hh:mm`, либо слово `NO`.

CONFIG
score: 15
visible_tests: 8
TEST
0:0 1 0:1
0:4 1 0:1
----
0 00:01
====
0:0 30 0:30
0:30 30 0:1
----
4 08:30
====
0:0 12 6:0
6:0 12 6:0
----
NO
=====
6:00 120 1:00
0:00 120 6:00
----
0 10:00
====
2:0 30 1:00
1:0 60 0:10
----
2 17:30
====
2:10 15 0:10
1:0 60 0:10
----
0 12:45
====
0:0 1 0:1
0:4 1 0:1
----
0 00:01
====
0:0 60 0:30
1:0 30 0:30
----
0 00:00
====
0:0 3600 6:00
6:00 3600 0:1
----
NO
=====
1:20 60 6:10
1:30 60 5:50
----
NO
====