# elif

lesson = 1160426

## Вложенные ветвления

Что делать, если вариантов выбора не один (когда считали $|x|$) и не два (четное или нечетное), а больше? Например, число положительное, отрицательное, ноль? Оценка "отлично", "хорошо", "удовлетворительно", "неудовлетворительно"?

Попробуем обойтись уже имеющимися знаниями про `if` и `else`.

### Положительное, отрицательное, ноль 

Вложенным может быть так же `if` .. `else`. 

Проверим, число положительное, отрицательное или ноль.

```python
x = int(input())

if x > 0:
    print('положительное')
else:
    # x <= 0
    if x == 0:
        print('ноль')
    else:
        print('отрицательное')
```
Хорошо, что только три варианта одного признака (положительное, отрицательное, ноль). Если так же писать разбор на признак из 8 вариантов, то лесенка кода будет уходить за другой край экрана. Что делать?

### elif

Записать проверку из многих вариантов можно проще с помощью оператора `elif` (сокращение от else if). 

**elif** - иначе если. 

* в `elif` обязательно должно быть **условие**, после него `:`;
* `elif` можно написать **много раз** с разными условиями;
* **выполнится только один вариант** из многих;
* условия проверяются **сверху вниз**;
* часть с `else` **не обязательная** (можно не писать).

```python
x = int(input())

if x > 0:
    print('положительное')
elif x == 0:
    print('ноль')
else:
    print('отрицательное')
```

**Код с `elif` читается проще, чем с многими уровнями вложенных `else` и `if`**

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

### Короче

Можно переписать код ещё короче. Теперь при изменении разбалловки не надо одну границу менять в двух условиях. Но теперь код чувствителен к порядку проверок.
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

**Выполняется только одна ветка из возможных**. Если часть с `else` нет, то может не выполниться ни одна ветка, потому что не подойдет условие.

![блок-схема elif](https://stepik.org/media/attachments/lesson/1160426/elif.drawio.svg)

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

## TASKINLINE билет на поезд

На поезде ребенок до 5 лет едет бесплатно. С 10 лет включительно покупает полный билет. С 5 включительно до 10 лет, покупает детский билет за 35% стоимости.

Дана цена полного билета и возраст на следующей строке. Напечатайте цену билета для этого человека в рублях. Для округления используйте функцию `round()`.

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
432
====

## Разбираем строку вида 12:34 на числа 12 и 34

Мы знаем как напечатать значение переменных `h` и `m` по формату `часы:минуты` с ведущими нулями.
```python
h = 3
m = 5
print(f'{h:02}:{m:02}')     # 03:05
```
Как *прочитать* такой ввод и разобрать его на числа?

Чтобы разделить строку на слова по `:`, напишите этот символ в `split`. Разделим строку `12:31` на часы h и минуты m:
```python
h, m = input().split(':')  # введем 12:31, тогда h='12', m='31'
                           # h и m не числа, а строки
# преобразуем строки к числам                           
h = int(h)
m = int(m)
```
То есть мы делаем почти то же самое, что в разборе входной строки `12 31`, но сначала разделяем не по пробелу, а по подстроке `:`. Можно написать короче, как мы привыкли писать раньше, используя `map`.

```python
h, m = map(int, input().split(':')) # указываем ':' в split и читаем строку вида 12:31
```
*Запишите этот пример в конспект.*

## TASKINLINE футбол-1

Матч Волгарь - Крылья Советов окончился со счетом `a:b`.

Команда Волгарь получает:

* 2 очка, если победила (`a > b`)
* 1 очко, если ничья (`a = b`)
* 0 очков, если проиграла (`a < b`)

Дан счет матча. Напечатать сколько очков получила команда Волгарь.

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

Первый период футбольного матча Волгарь - Крылья Советов окончился со счетом `a1:b1`, 
второй со счетом `a2:b2`.

Голы за два периода складываются, получаются голы за весь матч. По счету матча определяется победитель.

Дан счет первого и второго периодов. Напечатать сколько очков получила команда Волгарь.

Команда получает:

* 2 очка, если победила (`a > b`)
* 1 очко, если ничья (`a = b`)
* 0 очков, если проиграла (`a < b`)

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
