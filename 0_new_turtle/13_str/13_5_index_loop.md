# Цикл с индексом

lesson = 730290

## Циклы

Умеем в цикле перебирать **значения** элементов строки:
```python
s = 'Tanya'
for x in s:
	print(x)
```
напечатает
```python
T
a
n
y
a
```

Напишем цикл, используя **номер** элемента.

Строка `'Tanya'`, её длина 5, номера элементов от 0 до 4.

```python
s = 'Tanya'
i = 0
n = len(s)
while i < n:
	print(i, s[i])
	i += 1
```
напечатает
```python
0 T
1 a
2 n
3 y
4 a
```
Лучше использовать `range`:
```python
s = 'Tanya'
for i in range(len(s)):
	print(i, s[i])
```
напечатает 
```python
0 T
1 a
2 n
3 y
4 a
```

## TASKINLINE Номер символа w

Дана строка. 
На следующей строке дана буква.

Написать функцию **find(text, letter)**, она возвращает **номер** элемента с символом **letter**.

В строке есть эта буква. Эта буква одна.

CODE
def find(text, letter):
	# тут нужно написать код
	
	
s = input()			# читаем строку
letter = input()	# читаем символ
where = find(s, letter)
print(where)

TEST
Tanya
n
----
2
====
Hello, world!
r
----
9
====
MIPT
M
----
0
====

## TASKINLINE Первый номер символа w

Дана строка. 
На следующей строке дана буква.

Написать функцию **find_first(text, letter)**, она возвращает **номер** элемента с символом **letter**.

В строке есть эта буква. **Если букв в строке несколько, вернуть номер первого вхождения.**

CODE
def find_first(text, letter):
	# тут нужно написать код
	
	
s = input()			# читаем строку
letter = input()	# читаем символ
where = find_first(s, letter)
print(where)

TEST
Tanya
a
----
1
====
Tanya
n
----
2
====
Hello, world!
w
----
7
====
Hello, world!
o
----
4
====
MIPT
M
----
0
====
qqqqqqqqqqqq
q
----
0
====

## TASKINLINE Первый номер символа w или -1

Дана строка. 
На следующей строке дана буква.

Написать функцию **find(text, letter)**, она возвращает **номер** элемента с символом **letter**.

Если букв в строке несколько, вернуть номер первого вхождения. **Если буквы в строке нет, вернуть -1**

CODE
def find_first(text, letter):
	# тут нужно написать код
	
	
s = input()			# читаем строку
letter = input()	# читаем символ
where = find_first(s, letter)
print(where)

TEST
Tanya
g
----
-1
====
Tanya
a
----
1
====
Tanya
n
----
2
====
Hello, world!
w
----
7
====
Hello, world!
o
----
4
====
MIPT
M
----
0
====
qqqqqqqqqqqq
q
----
0
====
qqqqqqqqqqqq
w
----
-1
====

## TASKINLINE Последний номер символа w или -1

Дана строка. 
На следующей строке дана буква.

Написать функцию **find_last(text, letter)**, она возвращает **номер** элемента с символом **letter**.

Если букв в строке несколько, вернуть номер **последнего** вхождения. Если буквы в строке нет, вернуть -1.

CODE
def find_last(text, letter):
	# тут нужно написать код
	
	
s = input()			# читаем строку
letter = input()	# читаем символ
where = find_last(s, letter)
print(where)

TEST
Tanya
a
----
4
====
Tanya
g
----
-1
====
Tanya
n
----
2
====
Hello, world!
w
----
7
====
Hello, world!
o
----
8
====
MIPT
M
----
0
====
qqqqq
q
----
4
====
qqqqqqqqqqqq
w
----
-1
====

## TASKINLINE Убрать буквы между h

Дана строка. В строке 2 или больше букв **h**. Убрать текст от первой до последней буквы h включительно.

TEST
abchrrrfghhhxyz
----
abcxyz
====
hello, helen!
----
elen!
====
abcheh
----
abc
====
ahhb
----
ab
====
hi! hello! arghhhh!
----
!
====

## TASKINLINE Убрать буквы между h

Дана строка. Убрать текст от первой до последней буквы **h** включительно. 

Если в тексте 1 буква h, ее нужно убрать.

Если в тексте нет буквы h, оставьте его без изменений.

Возможно, ваше решение предыдущей задачи, решает эту задачу тоже.

TEST
hello
----
ello
====
Good bye!
----
Good bye!
====
while
----
wile
====
abch
----
abc
====
abchrrrfghhhxyz
----
abcxyz
====
hello, helen!
----
elen!
====
abcheh
----
abc
====
ahhb
----
ab
====
hi! hello! arghhhh!
----
!
====
