# Логические операторы

lesson = 411389

## Сложные условия

Задача: проверить високосный год или нет. Год является високосным, если он 

* делится на 4, 
* но не делится на 100, 
* если год делится на 400, то он все равно високосный.

Напишем функцию, `is_leap_year(year)`, которая по аргументу `year` возвращает истину (`True`) или ложь (`False`).

```python
def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False
```

## return и else

```python
if условие:
	return N1
else:
	return N2
```
работает так же, как
```python
if условие:
	return N1

return N2
```
Либо _условие_ верно и мы вышли функции с N1 в обоих случаях.

**После `return` жизни нет** и не интересно, что дальше в функции.

Либо _условие_ ложно, и тогда

* в первом случае выполняется оператор в else (`return N2`) - вернули N2
* во втором, условие ложно, if не выполняется, идем дальше. Будет выполнен следующий за if оператор. `return N2` - вернули N2.

Перепишем функцию:
```python
def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
    return False
```

Можно ли в этой функции менять местами блоки if или функция станет работать неправильно?

## QUIZ Поменяем местами

Студент написал: 
```python
def is_leap_year(year):
	if year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	elif year % 400 == 0:   # потом
		return True
    return False
```
Что вернет при `year=2000`?

A. True

B. False

ANSWER: B

## Логические операторы

Можно решить ту же задачу с високосным годом с помощью логических операторов.

* `and` - логическое **И** (конъюнкция)
* `or` - логическое **ИЛИ** (дизъюнкция)
* `not` - логическое отрицание

Таблицы истинности для логического И и логического ИЛИ.

![](https://stepik.org/media/attachments/lesson/411389/logical.png)

** `x and y` истина, только когда оба аргумента - истина. В остальных случаях - ложь. **

В теории множеств конъюнкция - это пересечение множеств.

Я хочу выпить чай. У меня есть чашка воды `x` и пакет чая `y`. Могу выпить чай, только если у меня есть и чашка, и пакетик **одновременно**.

** `x or y` ложь, только когда оба аргумента - ложь. В остальных случаях - истина. **

В теории множеств дизъюнкция - это объединение множеств.

К чаю я хочу сладкого. У меня есть печенье (cookie) `x` и конфета `y`. Сладкое у меня будет, если есть печенье или конфета или и печенье и конфета. **Хоть что-нибудь**. Только если у меня нет ни печенья, ни конфеты, я сижу без сладкого.

** `not x` - превращает ложь в истину и истину в ложь. **

Myanmar - страна, not Myanmar - все вне этой страны.

![](https://stepik.org/media/attachments/lesson/411389/myanmar-border-crossing-map.jpg)

## Логические операторы и математические задачи

Диапазоны значений, записанные через логические операторы:

![](https://stepik.org/media/attachments/lesson/411389/equal.png)

![](https://stepik.org/media/attachments/lesson/411389/notequal.png)

![](https://stepik.org/media/attachments/lesson/411389/between.png)

![](https://stepik.org/media/attachments/lesson/411389/out.png)

## Порядок вычислений

* **not** раньше **and** (как минус в `2 + -5`)
* **and** раньше **or**  (как умножить в `1+2*3`)
* **or** самый последний (как плюс)
* скобки изменяют порядок (как в `(1+2)*(2+3)`)

## QUIZ Чему равно значение выражение

Столовая работает с 8 до 22 часов. Сейчас `h` часов.

Какая запись правильно проверяет, что сейчас столовая работает?

A. `8 <= h <= 22`

B. `8 <= h and h <= 22`

C. `8 <= h or h <= 22`

D. `8 <= h not h <= 22`

ANSWER: A, B

## QUIZ Чему равно значение выражение

| Номер месяца | Месяц | Время года |
|----|----|----|
| 1 | январь | зима |
| 2 | февраль | зима |
| 3 | март | весна |
| 4 | апрель | весна |
| 5 | май | весна |
| 6 | июнь | лето |
| 7 | июль | лето |
| 8 | август | лето |
| 9 | сентябрь | осень |
| 10 | октябрь | осень |
| 11 | ноябрь | осень |
| 12 | декабрь | зима |

Сейчас месяц номер `m`.

Какая запись правильно проверяет, что сейчас зима?

A. `m == 1 and m == 2 and m == 12`

B. `m == 1 or m == 2 or m == 12`

C. `not (2 < m < 12)`

D. `2 < not m < 12`

ANSWER: B, C


## QUIZ Чему равно значение выражение

Понедельник - это 1, вторник - это 2, воскресенье - это 7.

Врач принимает с понедельника по пятницу с 8 до 16, а в субботу с 10 до 14.

Сейчас день d час h. Какое выражение правильно проверяет, принимает ли сейчас врач?

A. `1 <= d <= 5 and 8 <= h < 16 or d == 6 and 10 <= h < 14`

B. `1 <= d <= 5 or 8 <= h < 16 and d == 6 or 10 <= h < 14`

C. `1 <= d <= 5 or 8 <= h < 16 or d == 6 or 10 <= h < 14`

D. `1 <= d <= 5 and 8 <= h < 16 and d == 6 and 10 <= h < 14`

E. `1 <= d <= 5 or d == 6 and 8 <= h < 16 or 10 <= h < 14`

ANSWER: A


## x, y = y, x

Поменять значение переменных x и y легко:

```python
x = 3
y = 5
print(x, y)     # 3 5
x, y = y, x     # меняем значения x и y
print(x, y)     # 5 3
```

Напишем функцию sort2(x, y), которая возвращает 2 аргумента по возрастанию:

```python
def sort2(x, y):
    if x > y:
        return y, x
    else:
        return x, y

a, b = map(int, input().split())
a, b = sort2(a, b)
print(a, b)
```

| Input | Output |
|----|----|
| 5 3 | 3 5 |
| 2 10 | 2 10 |
| 7 7 | 7 7 |

## TASKINLINE sort3

Есть функция `sort2`. Напишите функцию `sort3(x, y, z)`, которая возвращает 3 числа по возрастанию.

```python
def sort2(x, y):
    if x > y:
        return y, x
    else:
        return x, y

def sort3(x, y, z):
    # тут нужно написать код

a, b, c = map(int, input().split())
a, b, c = sort3(a, b, c)
print(a, b, c)
```

CODE
def sort2(x, y):
    if x > y:
        return y, x
    else:
        return x, y

def sort3(x, y, z):
    # тут нужно написать код

a, b, c = map(int, input().split())
a, b, c = sort3(a, b, c)
print(a, b, c)

TEST
3 10 2
----
2 3 10
====
9 6 1
----
1 6 9
====
7 1 3
----
1 3 7
====
1 7 3
----
1 3 7
====
2 4 8
----
2 4 8
====
4 2 8 
----
2 4 8
====
7 7 7
----
7 7 7
====
9 9 3
----
3 9 9
====
9 9 11
----
9 9 11
====
1 4 1
----
1 1 4
====
4 7 4
----
4 4 7
====
7 1 1
----
1 1 7
====
2 2 9
----
2 2 9
====

## TASKINLINE Холодильник и дверь

Нужно пронести холодильник в дверь. Размер двери **w h** сантиметров, размер холодильника **a, b, c** сантиметров.

Холодильник можно поворачивать и класть на бок.

Даны размеры двери через пробел на одной строке и
размеры холодильника через пробел на другой строке.

Напечатайте YES, если холодильник можно пронести в дверь. Иначе напечатайте NO.

Читаем, что если ширина двери 60, то холодильник шириной 60 в него пройдет (если пройдет по высоте).

В дверь 80х180 холодильник 60х90х200 пройдет (YES). Надо развернуть так, чтобы в 80х180 проходило 60х90.

В дверь 80х180 холодильник 60х190х200 не пройдет (NO). Никак не повернуть, чтобы в 80х180 проходило 60х190.

TEST
180 80
200 60 120
----
YES
====
180 80
200 60 190
----
NO
====
80 150
90 90 90
----
NO
====
30 40
50 65 100
----
NO
====
30 40
170 35 25
----
YES
====

## TASKINLINE Тип треугольника

Даны стороны треугольника - целые числа.

Напишите функцию `triangle_len_type(a, b, c)`, где a, b, c - стороны треугольника.

Функция должна вернуть:

* 2 - если треугольник равносторонний (все стороны одинаковой длины)
* 1 - если треугольник равнобедренный (2 стороны одинаковые, третья другая)
* 0 - все стороны разные
* -1 - такой треугольник не может быть.

<img src="https://stepik.org/media/attachments/lesson/411389/triangle_len_type.JPG"></img>

TEST
3 3 3
---
2
====
3 4 3
---
1 
====
3 4 5
---
0
====
4 4 3
----
1
====
9 10 10
----
1
====
2 17 2
----
-1
====


## TASKINLINE Делится на 3 или 5, но не на 15

Напишите программу, которая печатает YES, если число делится на 3 или 5, но не делится на 15. Иначе напечатайте NO.

| Число | Напечатать | Почему |
|----|----|----|
| 6 | YES | делится на 3 |
| 10 | YES | делится на 5 |
| 150 | NO | делится на 15 |
| 4 | NO | не делится ни на 3, ни на 5 |

TEST
6
---
YES
====
10
---
YES
====
30
---
NO
====
11
---
NO
====
3
---
YES
====
5
---
YES
====
15
---
NO
====
150
---
NO
====
45
---
NO
====


## Ленивый питон

Правило: как только значение всего выражения можно определить, **дальше не считаем**.

```python
x < 5 and y != 3 or z == 0
```
Порядок вычислений при x = 10, y = 10, z = 0:

* `x < 5` False, значит `x < 5 and y != 3` все False
* поэтому `y != 3` не проверяем
* `z == 0` True
* `x < 5 and y != 3 or z == 0` это `False or True` равно `True`

```python
z == 0 or x < 5 and y != 3
```
Порядок вычислений при x = 10, y = 10, z = 0:

* `z == 0` True, значит все выражение True и дальше не считаем.

## XOR

Пишем про xor

