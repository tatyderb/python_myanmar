# Изменить переменную в цикле

lesson = 515009

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


## TASKTEXT вложенные квадраты

Написать функцию **sq(size, col1, col2)**. Они рисует 1 квадрат.

* `size` - размер стороны квадрата
* `col1` - цвет линии
* `col2` - цвет внутри

Написать функцию **sqn(size, n)**. Она рисует много квадратов.

* `size` - размер стороны первого квадрата
* `n` - рисовать `2n` квадратов

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

## TASKTEXT Задача: шахматная клетка

Взять функцию **row(n)** из предыдущей задачи.

Написать функцию **chess(n, m)**. 

* `n`  пар квадратов по горизонтали
* `m` пар квадратов по вертикали

```python
сhess(5, 4)
```
Нарисует

![шахматы](https://stepik.org/media/attachments/lesson/479598/chess.png)

## TASKTEXT Задача: узор из снежинок

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


