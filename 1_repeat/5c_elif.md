# elif

lesson = 1112177

## Вложенные if

Внутри одного `if` или `else` можно написать еще один `if .. else`.

Проверим, число положительное (positive) или отрицательное (negative) или 0 (zero).

```python
x = int(input())

if x > 0:
    print('positive')
else:
    if x == 0:
        print('zero')
    else:
        print('negative')
```

## elif

Проверить положительное число или нет можно проще. 

**elif** - иначе если.

```python
x = int(input())

if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')
```

## TASKINLINE билет на поезд

На поезде ребенок до 5 лет едет бесплатно. С 10 лет включительно покупает полный билет. С 5 включительно до 10 лет, покупает детский билет за 35% стоимости.

Дана цена полного билета и возраст через пробел. Напечатайте цену билета для этого человека в рублях. Для округления используйте функцию `round()`.

TEST
1000
34
----
1000
====
3275
4
----
0
====
2000
9
----
700
====
1500
5
----
525
====
1234
7
----
431
====

## TASKINLINE футбол-1

Матч Shan United - Yadanarbon окончился со счетом `a:b`.

Команда Shan United получает:

* 2 очка, если победила (`a > b`)
* 1 очко, если ничья (`a = b`)
* 0 очков, если проиграла (`a < b`)

Дан счет матча. Напечатать сколько очков получила команда Shan United.

Чтобы разделить строку на слова по `:`, напишите этот символ в `split`. Разделим строку `12:31` на часы h и минуты m:
```python
h, m = input().split(':')  # введем 12:31, тогда h='12', m='31'
                           # h и m не числа, а строки
```
CODE
a, b = map(int, input().split(':'))
TEST
5:4
----
2
====
4:5
----
0
====
0:0
----
1
====
10:3
----
2
====
3:3
----
1
====
0:1
----
0
====

## TASKINLINE футбол-2

1 период матча Shan United - Yadanarbon окончился со счетом `a1:b1`, 
второй со счетом `a2:b2`.

Голы за два периода складываются, получаются голы за весь матч. По счету матча определяется победитель.

Команда получает:

* 2 очка, если победила (`a > b`)
* 1 очко, если ничья (`a = b`)
* 0 очков, если проиграла (`a < b`)

Дан счет первого и второго периодов. Напечатать сколько очков получила команда Shan United.

TEST
3:0
1:2
----
2
====
1:2
3:0
----
2
====
1:0
1:2
----
1
====
2:1
0:3
----
0
====
0:3
2:1
----
0
====
4:5
0:0
----
0
====
0:0
3:3
----
1
====
1:3
3:1
----
1

## Аргументы print

Если в `print` написать `end=''`, то после `print` не будет писать с новой строки.

```python
print('a', end='')
print('b', end='')
```
Напечатает `ab` вместе.

**end** - что писать в конце.

Если в `print` написать `sep='-'`, то между значениями будет стоять не пробел, а `-`.
```python
x = 3
y = 7
print(x, y, sep=':')    # 3:7
```

## NUMBER 

Что будет напечатано?

```python
x = 8
if x > 4:
    print(4, end='')
    if x > 9:
        print(9, end='')
        if x == 8:
            print(8, end='')
```

ANSWER: 4


## elif может быть много

Оценки 

* 8, 9, 10 - отлично
* 5, 6, 7 - хорошо
* 3, 4 - удовлетворительно
* 1, 2 - неудовлетворительно

Студент получил оценку `x`. Напечатать значение оценки.

```python
x = int(input())

if x == 10:
    print('отлично')
elif x == 9:
    print('отлично')
elif x == 8:
    print('отлично')
elif x == 7:
    print('хорошо')
elif x == 6:
    print('хорошо')
elif x == 5:
    print('хорошо')
elif x == 4:
    print('удовлетворительно')
elif x == 3:
    print('удовлетворительно')
else:
    print('неудовлетворительно')
```

Подумайте, как можно написать короче.

## Короче

```python
x = int(input())

if x >= 8 :
    print('отлично')
elif x >=5:
    print('хорошо')
elif x >= 3:
    print('удовлетворительно')
else:
    print('неудовлетворительно')
```

## QUIZ Оценка

Что напечатает программа?

```python
x = 7

if x >= 8 :
    print('отлично')
elif x >= 3:
    print('удовлетворительно')
elif x >=5:
    print('хорошо')
else:
    print('неудовлетворительно')
```

A. отлично
B. хорошо
C. удовлетворительно
D. неудовлетворительно

SHUFFLE:false
ANSWER: C

## Разные признаки

Если признаки разные (четность и знак числа), то их стоит писать в разных блоках if..else.

```python
// проверка четности
if x % 2 == 0
	print("четное");
else	
	print("нечетное");

// проверка знака числа
if x == 0:
	print("zero");
elif x < 0:
	print("negative");
else:
	print("positive");
```