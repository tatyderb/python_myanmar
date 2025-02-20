# Матрицы

lesson = 443935

## Строки и столбцы

Матрица (matrix) или таблица (table) это список из списков.

В матрице есть **строка** (row):

![](https://stepik.org/media/attachments/lesson/443935/ar2d1.png)


В матрице есть **столбец** (column):

![](https://stepik.org/media/attachments/lesson/443935/ar2d2.png)

## Создадим матрицу

В математике часто используют матрицы. Матрицы можно сделать в python как список из списков.

Хотим задать матрицу

$$\begin{bmatrix}
1 & 2 & 3 \\\\
4 & 5 & 6 \\\\
7 & 8 & 9 
\end{bmatrix}$$

Каждая строка матрицы - это список.

Вся матрица - это список из списков:
```python
m = [
    [1, 2, 3],       # m[0]
    [4, 5, 6],       # m[1]
    [7, 8, 9]        # m[2]
    ]
```

Печать:
```python
print(m) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
Число 8 находится в списке `m[2]`. В этом списке его номер 1. Значит `m[2][1]` это число 8.

Заменим 8 на 100. 
```python
m[2][1] = 100
```

## Список списков

*Здесь должен быть рисунок, который показывает, как хранится список списков в памяти*

*Здесь должно быть объяснение, что m - это список ссылок на списки.*

## Печать матрицы

Печать красиво (по строкам):
```python
for row in m:   # для каждой строки
    print(*row) # печатать все элементы строки через пробел
```
или используем цикл для печати каждого элемента строки матрицы:
```python
for row in m:               # для каждой строки
    for x in row:           # для каждого элемента этой строки
        print(x, end=' ')   # печатай элемент и ставь пробел
    print()                 # закончилась строка - печатай символ "новая строка"
```

получим
```cpp
1 2 3
4 5 6
7 8 9
```

Сделаем функцию, которая печатает матрицы. Будем потом ее использовать:
```python
def print_matrix(m):
    for row in m:   # для каждой строки
        print(*row) # печатать все элементы строки через пробел
```

## Чтение матрицы

Мы умеем читать 1 строку чисел
```python
a = [int(x) for x in input().split()]
```

Прочитать сначала n (сколько строк), потом прочитать матрицу:
```python
n = int(input())
m = []
for i in range(n):
    a = [int(x) for x in input().split()]
    m.append(a)
```
Даны числа:
```cpp
3           # сколько строк
1 2 3 4     # первая строка матрицы
5 6 7 8     # вторая строка матрицы
9 10 11 12  # третья строка матрицы
```
Напишем отдельную функцию, которая читает числа и возвращает матрицу. 
```python
def read_matrix():
    n = int(input())
    m = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        m.append(a)
        
    return m
```

## TASKINLINE Читать и печатать

Прочитать матрицу. Напечатать ее.

TEST
3
5 -3 17 4
12 8 -1 10
-7 11 6 9
----
5 -3 17 4
12 8 -1 10
-7 11 6 9
====
2
1 2 3 4 5
6 7 8 9 10
----
1 2 3 4 5
6 7 8 9 10
====

## TASKINLINE Увеличить в 10 раз

Дана матрица 3х3. Увеличить число в этой ячейке матрицы в 10 раз. Напечатать полученную матрицу.

![](https://stepik.org/media/attachments/lesson/443935/ar2d4.png)

TEST
4 7 9
1 6 8
3 2 0
---
4 7 9
1 6 80
3 2 0
====
1 2 3
4 5 6
7 8 9
---
1 2 3
4 5 60
7 8 9
====
-11 -12 -13
24 25 26
-101 -110 -111
---
-11 -12 -13
24 25 260
-101 -110 -111
====

## TASKINLINE Сумма ряда

Дана матрица. Дан номер ряда. Напечатать сумму чисел этого ряда.

Для вычисления суммы ряда написать функцию **sum_row(m, i)**, где **m** - матрица, **i** - номер ряда.

![](https://stepik.org/media/attachments/lesson/443935/ar2dmagic_sum.png)

Матрица 3х3, ряд 1, сумма 3+5+7=15

TEST
3
4 7 9
1 6 8
3 2 0
0
---
20
====
3
1 2 3
4 5 6
7 8 9
2
---
24
====
4
-11 -12 -13
-2 -7 -4
24 25 26
-101 -110 -111
1
---
-13
====

## TASKINLINE Сумма столбца

Дана матрица. Дан номер столбца. Напечатать сумму чисел этого столбца.

Для вычисления суммы столбца написать функцию **sum_col(m, i)**, где **m** - матрица, **i** - номер столбца.

![](https://stepik.org/media/attachments/lesson/443935/ar2dmagic4.png)

Матрица 3х3, столбец 2, сумма 6+7+2=15

TEST
3
4 7 9
1 6 8
3 2 0
2
---
17
====
3
1 2 3
4 5 6
7 8 9
0
---
12
====
4
-11 -12 -13
-2 -8 -4
24 25 26
-101 -110 -111
1
---
-105
====


## TASKINLINE Сумма диагонали

Дано `N` и дана матрица NxN. Напечатать сумму чисел на ее диагонали.

Для вычисления суммы диагонали написать функцию **sum_diag(m)**, где **m** - матрица.

![](https://stepik.org/media/attachments/lesson/443935/ar2dmagic2.png)

Матрица 3х3, сумма 8+5+2=15

TEST
3
8 1 6
3 5 7
4 9 2
---
15
====
3
1 2 3
4 5 6
7 8 9
---
15
====
3
-11 -12 -13
24 25 26
-101 -110 -111
---
-97
====
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
----
34
====

## TASKINLINE Сумма обратной диагонали

Дано `N` и дана матрица NxN. Напечатать сумму чисел на ее диагонали (как на рисунке).

Для вычисления суммы диагонали написать функцию **sum_diag2(m)**, где **m** - матрица.

Нужно придумать формулу.

![](https://stepik.org/media/attachments/lesson/443935/ar2dmagic3.png)

Матрица 3х3, сумма 6+5+4=15

TEST
3
8 1 6
3 5 7
4 9 2
---
15
====
3
1 2 3
4 5 6
7 8 9
---
15
====
3
-11 -12 -13
24 25 26
-101 -110 -111
---
-89
====
4
1 2 3 14
5 6 7 8
9 10 11 12
13 14 15 16
----
44
====

## TASKINLINE Магический квадрат

Дано `n`. 

* Прочитать матрицу nxn.
* вычислить суммы всех ее строк, столбцов и диагоналей
* если они все равны, то это магический квадрат и надо напечатать MAGIC
* иначе напечатать NO

Напишите функцию **magic(m)**, которая возвращает `True`, если это магический квадрат, и `False`, если нет.

![](https://stepik.org/media/attachments/lesson/443935/ar2dmagic_s.png)


TEST
3
8 1 6
3 5 7
4 9 2
----
MAGIC
====
3
0 1 6
3 5 7
4 9 2
----
NO
====
3
18 11 16
13 15 17
14 19 12
----
MAGIC
====
4
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
----
MAGIC
====
4
16 13 2 13
5 10 11 8
9 6 7 12
4 5 14 1
----
NO
====
3
1 0 0
0 -1 0
1 0 0
----
NO
====

## TASKINLINE Сложение матриц

Дано n. Даны 2 матрицы `a` и `b` из n строк. Напишите функцию **add(a, b)**, которая складывает полученные матрицы. Напечатайте полученную матрицу.

![](https://stepik.org/media/attachments/lesson/443935/matrix_add.png)

Скопируйте нужные функции из предыдущих задач. Напишите функцию `add`.

```python
a = read_matrix()
b = read_matrix()
c = add(a, b)
print_matrix(c)
```

TEST
2
1 2
3 5
2
4 -6
2 1
----
5 -4
5 6
====
3
1 2 3 4
5 6 7 8
9 10 11 12
3
10 20 30 40
50 60 70 80
90 100 110 120
----
11 22 33 44
55 66 77 88
99 110 121 132
====
3
1 2
3 4
5 6
3
-10 -9
-8 -7
-6 -5
----
-9 -7
-5 -3
-1 1
====

## TASKINLINE Транспонировать матрицу

Дано n. Дана матрица из n строк. Напишите функцию **trans(m)**, которая транспонирует матрицу. Напечатайте полученную матрицу.

![](https://stepik.org/media/attachments/lesson/443935/matrix_trans.png)

TEST
2
1 2 3
4 5 6
----
1 4
2 5
3 6
====
2
1 2
3 5
----
1 3
2 5
====
3
0 1
2 -1
4 0
----
0 2 4
1 -1 0
====
