# Переменные

lesson = 403872

## Присвоить

В переменную можно записать данные и потом прочитать их.

`=` - это присвоить

```python
x = 7       # в x записать число 7
y = x + 3   # в у записать 10
```

Как работает `y = x + 3`

* прочитать `x` (это 7)
* вычислить `7+3` (это 10)
* записать в `y` число 10

**Нельзя!**
```python
7 = x  # нельзя записать В число
```

## Разные типы

В переменную можно записать разные типы. Тип переменной `x` можно узнать `type(x)`

```python
x = 7
print(x, type(x))   # 7 int

x = 3.14
print(x, type(x))   # 3.14 float

x = "МФТИ"
print(x, type(x))   # МФТИ str
```

## Прочитать строку

**input()** читает 1 **строку**.

```python
s = input() # прочитать строку и записать ее в переменную s
```
Если ввели число, нужно из строки сделать число правильного типа.

Вводим _целое число_.

```python
s = input() # это строка
x = int(s)  # из строки сделали целое число
```
или сразу в одну строку кода, без переменной `s`:
```python
x = int(input())    # прочитали строку, 
                    # из строки сделали целое число 
                    # записали число в переменную х
```

Вводим _дробное число_:
```python
x = float(input())
```

## QUIZ 

Ввели числа:
```cpp
12
3.5
```
Надо прочитать их и вычислить сумму 15.5. Какой код это делает?

A.

```python
x = int(input())
y = int(input())
print(x+y)
```

B.

```python
x = float(input())
y = float(input())
print(x+y)
```

C.

```python
x = int(input())
y = float(input())
print(x+y)
```

D.

```python
x = input()
y = input()
print(x+y)
```

ANSWER: B, C

## TASK Сколько столов?

repo = tasks/1_int/div_table
visible_tst_num = 2

## Несколько чисел на одной строке

Если числа одинакового типа и вводятся через пробел, то используем **split()** и **map()**

Ввели числа так:
```cpp
12 6 -4
```
Хотим прочитать их в переменные x, y, z и вычислить сумму.

```python
s = input()                         # s = "12 6 -4"   это одна строка
s = input().split()                 # s = ['12', '6', '-4'] разбили строку на слова
x, y, z = map(int, input().split()) # к каждому слову применили функцию int, 
                                    # получили много чисел
```

## TASK Сколько стоит обед?

repo = tasks/1_int/sum_4_obed
visible_tst_num = 1
