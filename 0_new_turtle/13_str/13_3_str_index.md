# Значения и индексы

lesson = 730288

## Новые слова

В скобках пишу термин по-английски.

* Строка - это **последовательность** (sequence) символов.

* Последовательность состоит из **элементов** (element).

* Каждый **элемент** строки имеет **значение** (value) и **номер** (index).

* **Длина** строки - это сколько элементов в строке.

* `[ ]` - обратиться к элементу строки с номером 

Язык программирования python назван в честь группы [Monty Python](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BD%D1%82%D0%B8_%D0%9F%D0%B0%D0%B9%D1%82%D0%BE%D0%BD). Покажем новые термины на этой строке.

![](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'     
print(s[0])				# M
print(s[1])				# o
print(s[-1])			# y
i = 2
print(s[i])				# n
						# ...
print(s[11])			# n

print(s)				# Monty Python
n = len(s)				# длина строки
print(n)				# 12
```

| Элемент | Значение | Номер | Называем |
|----|----|----|------|
| `s[0]` | M | 0 | Первый элемент строки. Элемент с номером 0. |
| `s[1]` | o | 1 | Элемент с номером 1. |
| `s[2]` | n | 2 | Элемент с номером 2. |
| `s[-1]` | n | -1 | Последний элемент строки. Элемент с номером -1. Элемент с номером 11. |

### Считаем на пальцах

Тяжело  считать с 0? Считаем на пальцах! Большой палец в стороне, это 0.

* 0 - большой палец,
* 1, 2, 3, 4 - остальные пальцы.

Пальцы 0, 1, 2, 3, 4. Всего пальцев 5. Номер последнего пальца 5-1=4.

```python
s = 'Tanya'
print(0, s[0])		# T
print(1, s[1])		# a
print(2, s[2])		# n
print(3, s[3])		# y
print(4, s[4])		# a
print(len(s))		# 5
```
![ладонь]()

### Считаем с конца

Можно считать номер с конца. Начинаем с -1.

```python
s = 'Tanya'
print(-1, s[-1])	# a
print(-2, s[-2])	# y
print(-3, s[-3])	# n
print(-4, s[-4])	# a
print(-5, s[-5])	# T
print(len(s))		# 5
```

## STRING Какое значение?

![Monty Python](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
print(s[9])
```
Какое значение (символ) имеет элемент с **номером** 9?

ANSWER: h

## QUIZ Какой номер?

![Monty Python](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
```
Какой номер имеет элемент со **значением** `P`?

A. 5
B. 6
C. 7
D. 0
E. 11

ANSWER: B

## STRING Считаем с конца

![Monty Python](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

```python
s = 'Monty Python'
print(s[-4])
```
Какое значение (символ) имеет элемент с **номером** `-4`?

ANSWER: t

## STRING Складываем

![Monty Python](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

В питоне один символ - это **строка** длиной 1. Строки можно складывать.

Что напечатает?
```python
s = 'Monty Python'
print(s[6] + s[1] + s[-1] + s[4])
```
Большие буквы остаются большими. Маленькие буквы остаются маленькими.
 
ANSWER: Pony

## STRING Складываем и умножаем

![Monty Python](https://stepik.org/media/attachments/lesson/418189/string_slicing.png)

В питоне один символ - это **строка** длиной 1. Строки можно складывать и умножать.

Что напечатает?

```python
s = 'Monty Python'
print(s[2] + s[-2] * 3) 
```
 
ANSWER: nooo

## TASKINLINE Фамилия, имя, отчество

В русском языке сначала пишут фамилию, потом имя, потом отчество.

```
Дербышева Татьяна Николаевна
```

* Дербышева - фамилия.
* Татьяна - имя.
* Николаевна - отчество.

Коротко имя и фамилия (инициалы) записывают так:

```
Дербышева Т.Н.
```
* только первые буквы, 
* после них ставится точка `.`,
* без пробела (no space)

Даны фамилия, имя, отчество так:
```
Дербышева 
Татьяна 
Николаевна
```
Надо напечатать так:
```
Дербышева Т.Н.
```
TEST
Дербышева 
Татьяна 
Николаевна
----
Дербышева Т.Н.
====
Ломоносов
Махаил
Васильевич
----
Ломоносов М.В.
====
Пушкин
Александ
Сергеевич
----
Пушкин А.С.
====