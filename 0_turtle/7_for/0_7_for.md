# for

lesson = 479598

## Пример: квадрат

Функция **sq(size)** рисует квадрат стороной **size**

![квадрат](https://stepik.org/media/attachments/lesson/479598/01_sq.png)

```python
def sq(size):
    t.fd(size)  
    t.lt(90)

    t.fd(size)  
    t.lt(90)

    t.fd(size)  
    t.lt(90)

    t.fd(size)  
    t.lt(90)
```

В функции этот код повторяется 4 раза:

```python
    t.fd(size)  
    t.lt(90)
```

## for i in range(n)

Повторить код `n` раз. Это **цикл**.

```python
for i in range(n):
    код
```

* for - специальное слово
* in - специальное слово
* i - переменная. Имя любое. Она считает 0, 1, 2, .. n-1.
* range(4) - повторить 4 раза, пишем 4 в ( ) - это функция
* после range(4) пишем : (column)
* код пишем с отступом (TAB). Закончились отступы - закончился цикл.

Функция с циклом:
```python
def sq(size):
    for i in range(4):  # повторить 4 раза
        t.fd(size)  
        t.lt(90)
```

Вся программа:
```python
import turtle

def sq(size):
    for i in range(4):  # повторить 4 раза
        t.fd(size)  
        t.lt(90)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

sq(100)

turtle.done()
```

## TASKTEXT Задача: треугольник

Напишите функцию **tri(size)**. Она рисует треугольник. 

**В функции использовать for.**

![треугольник](https://stepik.org/media/attachments/lesson/479598/01_tri.png)

## Лестница - до и после цикла

Как написать цикл

* Найдите код, который повторяется **много** раз. Напишите его В цикле.
* 1 раз ДО повторения кода  - напишите это ДО цикла.
* 1 раз ПОСЛЕ повторения кода - напишите ПОСЛЕ цикла.

![ступеньки](https://stepik.org/media/attachments/lesson/479598/02_stairs.png)

Рисуем лестницу. **n** ступенек. Функция **stairs(size, n)**. Размер ступеньки **size**
* до цикла 1 раз: направо и запомнить точку в переменной `p`
* в цикле много раз: *рисуем 1 ступеньку*
* после цикла 1 раз: цвет красный и вернуться в точку `p`

```python
def stairs(size, n):
    # до цикла 
    p = t.pos()         # запомнили точку старта
    t.lt(90)
    
    # цикл - повторить много раз
    for i in range(n):  # повторить n раз
        t.fd(size)  
        t.rt(90)
        t.fd(size)  
        t.lt(90)
        
    # закончились отступы - закончился цикл
    # после цикла возвращаемся назад
    t.color('red')
    t.goto(p)           # вернулись в точку старта
```

Вся программа:
```python
import turtle


def stairs(size, n):
    # до цикла 
    p = t.pos()         # запомнили точку старта
    t.lt(90)
    
    # цикл - повторить много раз
    for i in range(n):  # повторить n раз
        t.fd(size)  
        t.rt(90)
        t.fd(size)  
        t.lt(90)
        
    # закончились отступы - закончился цикл
    # после цикла возвращаемся назад
    t.color('red')
    t.goto(p)           # вернулись в точку старта

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

stairs(50, 3)

turtle.done()
```

## TASKTEXT Задача: отрезки

Написать функцию **dash(col, n)**. Она рисует `n` линий цветом `col`.

Использовать ее и нарисовать

![отрезки](https://stepik.org/media/attachments/lesson/479598/fdash.png)

## TASKTEXT Задача: полигон

Написать функцию **poli(size, n, col)**. Она рисует правильный многоугольник. 

* n - сколько углов
* size - длина стороны
* col - цвет

Нарисовать:

![многоугольники](https://stepik.org/media/attachments/lesson/479598/spoly.png)

## TASKTEXT Задача: равнобедренный треугольник

В этой задаче **for не нужен**.

Напишите функцию **tri(size, ang)**. Она рисует равнобедренный треугольник с двумя сторонами size и углом ang между ними.

![треугольник](https://stepik.org/media/attachments/lesson/479598/tr20.png)

Подумайте, как решить задачу.

Эта функция будет нужна в следующей задаче.

Подсказка:

* запомнить точку старта в p0
* нарисовать первую сторону длиною size и запомнить точку p1
* вернуться в p0
* повернуться на ang
* нарисовать вторую сторону длиною size
* перейти в p1
* перейти в p0

## TASKTEXT Задача: правильные многоугольники

Возьмите функцию **tri(size, ang)** из предыдущей задачи.

![треугольник](https://stepik.org/media/attachments/lesson/479598/tr20.png)

Напишите функцию **poli(size, n)**. Она рисует правильный n-угольник из **n** равнобедренных треугольников со сторонами **size**.

Нарисовать

![многоугольники](https://stepik.org/media/attachments/lesson/479598/for3.png)

## Запомнить и изменить переменные в цикле

Запомнить и изменить переменные в цикле

Нарисуем веер из `n` линий размера `size` цвета `col`.
Напишем функцию **veer(n, size, col)**. С ее помощью нарисуем

![веер](https://stepik.org/media/attachments/lesson/479598/06_veer1.png)

```python
import turtle           

def veer(n, col, size):
                        # 1 раз ДО повторения
    t.color(col)        # установить цвет

    for i in range(n):  # повторяем n раза рисунок 1 линии
        t.fd(size)        
        t.fd(-size)        
        t.left(30)     


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

t.lt(15)
veer(6, 'yellow', 100)
t.rt(195)
veer(7, 'red', 120)

turtle.done()
```

## Пример: изменять длину отрезков

Нарисуем 

![веер2](https://stepik.org/media/attachments/lesson/479598/06_veer2.png)

Для этого будем в цикле (много раз) менять size. **Каждый раз увеличим size на d**
```python
        size = size + d # в цикле изменяем значение size
```
Вся программа:
```python
import turtle           

def veer(n, col, size, d):
                        # 1 раз ДО повторения
    t.color(col)        # установить цвет

    for i in range(n):  # повторяем n раза рисунок 1 линии
        t.fd(size)        
        t.fd(-size)        
        t.left(30) 
        size = size + d # в цикле изменяем значение size


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

t.lt(15)
veer(6, 'yellow', 60, 20)
t.rt(195)
veer(7, 'red', 50, 20)

turtle.done()
```

## TASKTEXT Задача: спираль

Написать функцию **spi(n, col)**. Она рисует спираль из `n` линий цвета `col`.

Использовать функцию и нарисовать

![спирали](https://stepik.org/media/attachments/lesson/479598/fsp1.png)

## TASKTEXT Задача: двойная спираль

Написать функцию **spiral2(n, start_size, delta)**. Она рисует n отрезков спирали.

* `n` - количество отрезков в спирали
* `start_size` — длина первой линии,
* `delta` — на сколько меняется длина следующей линии

Использовать функцию и нарисовать

![спирали](https://stepik.org/media/attachments/lesson/479598/fsp2.png)


## TASKTEXT: вложенные квадраты

Написать функцию **sq(size, col1, col2)**. Они рисует 1 квадрат.

* `size` - размер стороны квадрата
* `col1` - цвет линии
* `col2` - цвет внутри

Написать функцию **sqn(size, n)**. Она рисует много квадратов.

* `size` - размер стороны первого квадрата
* `n` - сколько квадратов

Функция `sqn(size, n)` в цикле вызывает функцию `sq(size, col1, col2)`.

Нарисовать:

![квадраты](https://stepik.org/media/attachments/lesson/479598/kvin22.png)

## TASKTEXT Задача: ковер в полоску

Пара - это 2 предмета.

Написать функцию **row(n)**. Она рисует **n** раз по 2 квадрата ("n пар квадратов").

```python
row(5)
```
нарисует

![ряд](https://stepik.org/media/attachments/lesson/479598/lp1.png)

Написать функцию **carpet(n,m)**.

* `n` — размер (сколько пар квадратов) по горизонтали,
* `m` — размер по вертикали.

```python
carpet(5, 4)
```
нарисует

![ковер](https://stepik.org/media/attachments/lesson/479598/lines1.png)

Написать функцию и нарисовать картинку.

## TASKTEXT: Задача: шахматная клетка

Взять функцию **row(n)** из предыдущей задачи.

Написать функцию **chess(n, m)**. 

* `n`  пар квадратов по горизонтали
* `m` пар квадратов по вертикали

```python
сhess(5, 4)
```
Нарисует

![шахматы](https://stepik.org/media/attachments/lesson/479598/chess.png)

## TASKTEXT: Задача: узор из снежинок

Можно изменить скорость черепахи:
```python
t.speed(1)      # очень медленно
t.speed(10)     # быстро

t.speed(0)      # самая большая скорость в repl.it
```

Написать функцию **ray(size, n)**. Она рисует луч снежинки.

* `size` — размер луча,
* `n` -  количество веток в луче.
* `sizeOfRay=size/(3*n)` - размер самой маленькой ветки
* `sizeOfRay *= 2` - размер следующей ветки

![луч снежинки](https://stepik.org/media/attachments/lesson/479598/snowRay.png)

Написать функцию **snowflake(size, n)**. Она рисует 1 снежинку.

* `size` — размер луча снежинки,
* `n` — количество ветвей на луче.

![снежинка](https://stepik.org/media/attachments/lesson/479598/snow.png)

Написать функцию **snow** и нарисовать

![снежинка](https://stepik.org/media/attachments/lesson/479598/snowr.png)

Подсказка: сначала напишите функцию `snow`, которая рисует квадрат или крест вместо снежинки. Исправьте ошибки. Замените квадрат или крест на снежинку.


