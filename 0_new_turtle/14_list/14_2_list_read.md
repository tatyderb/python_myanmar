# Читаем список

lesson = 733757

## QUIZ Подробная печать

```python
a = ['Alex', 'Oleg', 'Tanya', 'Boris']
n = 34
print(n, a)
```
Что напечатает код?

A. `34 Alex Oleg Tanya Boris`
B. `34 [Alex Oleg Tanya Boris]`
C. `34 ['Alex' 'Oleg' 'Tanya' 'Boris']`
D. `34 ['Alex', 'Oleg', 'Tanya', 'Boris']`

SHUFFLE: False
ANSWER: D


## Печать списка без печати `[ ]`

Даны списки
```python
a = [7, -3, 12]
b = ['red', 'blue', 'white']
```
Можно печатать так:
```python
print(a)				# [7, -3, 12]
print(b)				# ['red', 'blue', 'white']
```
Можно печатать значения через пробел.
```python
print(a[0], a[1], a[2])	# 7 -3 12
print(b[0], b[1], b[2])	# red blue white
```
Оператор `*` распаковывает список в его элементы через запятую. Можно написать так (тот же результат):
```python
print(*a)	# 7 -3 12
print(*b)	# red blue white
```

## QUIZ Красивая печать

```python
a = ['Alex', 'Oleg', 'Tanya', 'Boris']
n = 34
print(n, *a)
```
Что напечатает код?

A. `34 Alex Oleg Tanya Boris`
B. `34 'Alex' 'Oleg' 'Tanya' 'Boris'`
C. `34 'Alex', 'Oleg', 'Tanya', 'Boris'`
D. `34 [Alex Oleg Tanya Boris]`
E. `34 ['Alex' 'Oleg' 'Tanya' 'Boris']`
F. `34 ['Alex', 'Oleg', 'Tanya', 'Boris']`

SHUFFLE: False
ANSWER: A

## TASKINLINE ФИО

Дано на одной строке имя, отчество, фамилия через пробел (всегда 3 слова)!

Напечатать фамилию и инициалы.

TEST
Татьяна Николаевна Дербышева
----
Дербышева Т.Н.
====
Александр Сергеевич Пушкин
----
Пушкин А.С.
====
Михаил Васильевич Ломоносов
----
Ломоносов М.В.
====


## TASKINLINE Сколько лет?

В России в магистратуре учатся 3 года (подфак, 5 курс, 6 курс).

Дана строка: 

* Сколько лет студенту, когда он приехал в Россию. 
* Как зовут студента.

Пример, как могут звать студента:

* Дербышева Татьяна Николаевна
* Мье Аунг
* Мадхусудан Раджам Саи Прасад
* Липстер да Коста Мотта Силва Фелиппе

Напечатать сколько лет будет студенту через 3 года и как его зовут.

TEST
20 John Smith
----
23 John Smith
====
16 She Suong
----
19 She Suong
====
22 Ву Тхи Ба
----
25 Ву Тхи Ба
====
17 Липстер да Коста Мотта Силва Фелиппе
----
20 Липстер да Коста Мотта Силва Фелиппе
====

## TASKINLINE Сколько лет - 2?

В России учатся 3 года (подфак, 5 курс, 6 курс).

Дана строка: 

* Как зовут студента. Студенты разные. Разное количество слов.
* Сколько лет студенту, когда он приехал в Россию.

Напечатать сколько лет будет студенту через 3 года в том же формате.

TEST
Мье Аунг 20 
----
Мье Аунг 23 
====
She Suong 16
----
She Suong 19
====
Ву Тхи Ба 22
----
Ву Тхи Ба 25
====
Мадхусудан Раджам Саи Прасад 27
----
Мадхусудан Раджам Саи Прасад 30
====
Липстер да Коста Мотта Силва Фелиппе 17
----
Липстер да Коста Мотта Силва Фелиппе 20
====


## Много чисел

### Много целых чисел 

читаем так:
```python
a = [int(x) for x in input().split()]
print(a)
```

Дано:
```python
20 100 -5
```
напечатает
```python
[20, 100, -5]
```
В этом курсе мы не будем разбирать как это работает. Мы будем пользоваться этим кодом. Если нужно прочитать нецелые числа, то заменяем функцию `int()` на `float()`.

### Прочитать два числа

Дано два целых числа на одной строке через пробел. Напечатать сумму этих чисел.

```python
n, k = [int(x) for x in input().split()]
print(n + k)
```
Этот код мы тоже будем только использовать. Понимать его мы будем в следущем курсе.


## TASKTEXT Бусы

* Дано $n$ - число прямоугольников, которые надо нарисовать.
* На следующей строке даны цвета прямоугольников через пробел.
* На следующей строке даны высоты прямоугольников через пробел.

Нарисовать  $n$ прямоугольников заданного цвета и высоты, узор повторяется.

Дано:
```python
8
gold red green
30 60 90
```
Нарисует

![8 бусинок](https://stepik.org/media/attachments/lesson/723108/t2_7_1.png)