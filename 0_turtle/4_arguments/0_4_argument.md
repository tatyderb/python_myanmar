# Аргументы функций

lesson = 479595

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
от 13:25 до 19:10

![задача](https://stepik.org/media/attachments/lesson/479595/03_dash_video.png)

## Аргументы функции

Нужно рисовать цветной треугольник. Каждый треугольник рисуем своим цветом. Красный, зеленый, синий. 

Функциям черепахи можно дать цвет, угол, размер линии. Это **параметры** (или **аргументы** ).

```python
t.color('blue')   # дали функции черепахи color цвет 'blue'
t.lt(45)             # дали функции черепахи lt угол 45
t.width(3)        # дали функции черепахи width размер 3
```
Для новых функций тоже можно указать параметры (аргументы).

Дадим цвет и будем рисовать треугольник.

```python
# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
```

Выполнять команду triangle нужно с цветом:

```python
# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      
```

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Вся программа:
```python
import turtle

# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      

turtle.done()
```

## TASKTEST Задача: квадраты и треугольники

* Возьмите пример.
* Напишите в нем функцию **sq(col)**. Она рисует квадрат цвета col.
* Нарисуйте 2 квадрата - зеленый и желтый. Нарисуйте 2 треугольника - красный и синий. Используйте функции `tri(col)` и `sq(col)`.

![пример](https://stepik.org/media/attachments/lesson/479595/func_t8.png)

Пример: 3 треугольника.
```python
import turtle

# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      

turtle.done()
```

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
от 19:10 до 22:10

## Много аргументов

Надо нарисовать треугольники разного размера и цвета.

Меняется цвет. Меняется размер.

Аргумент *col* называется "**переменная** col" (variable).

![треугольники разного цвета и размера](https://stepik.org/media/attachments/lesson/479595/02_ex.png)

* Плохо: написать 3 функции. Много кода.
* Хорошо: 1 функция. В функцию передаем цвет и размер. 2 аргумента.

**Аргументы пишем через ,  (запятая)**

Функция triangle. Аргументы col (цвет) и size (размер треугольника).
```python
# переменная col запомнит цвет (это текст, нужны ' ')
# переменная size запомнит размер (это число, пишем БЕЗ ' ')
def triangle(col, size):
    
    t.color(col)   # передаем значение col другой команде
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
```

Вызываем функцию. Даем цвет и размер.
```python
# в col записываем 'blue', в size записываем 100    
triangle('blue', 100)  
t.lt(45)

# в col записываем 'red', в size записываем 75    
triangle('red', 75)      
t.lt(45)

# в col записываем 'green', в size записываем 150    
triangle('green', 150)    
```

Вся программа:
```python
import turtle

# переменная col запомнит цвет (это текст, нужны ' ')
# переменная size запомнит размер (это число, пишем БЕЗ ' ')
def triangle(col, size):
    
    t.color(col)   # передаем значение col другой команде
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# в col записываем 'blue', в size записываем 100    
triangle('blue', 100)  
t.lt(45)

# в col записываем 'red', в size записываем 75    
triangle('red', 75)      
t.lt(45)

# в col записываем 'green', в size записываем 150    
triangle('green', 150)   

turtle.done()
```

## TASKTEST Задача: треугольники разных размеров

* Взять пример
* Функцию **triangle(col, size)** не изменять.
* Использовать функцию `triangle(col, size)`. Нарисовать

![треугольники разного цвета и размера](https://stepik.org/media/attachments/lesson/479595/02_task.png)

Пример нужно изменить:
```python
import turtle

# переменная col запомнит цвет (это текст, нужны ' ')
# переменная size запомнит размер (это число, пишем БЕЗ ' ')
def triangle(col, size):
    
    t.color(col)   # передаем значение col другой команде
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)
    t.fd(size)     # передаем значение size другой команде
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# в col записываем 'blue', в size записываем 100    
triangle('blue', 100)  
t.lt(45)

# в col записываем 'red', в size записываем 75    
triangle('red', 75)      
t.lt(45)

# в col записываем 'green', в size записываем 150    
triangle('green', 150)   

turtle.done()
```

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os 
от 22:10 до 27:35

## Изменить значение переменной

Нарисовать:

![отрезки](https://stepik.org/media/attachments/lesson/479595/03_dash_video.png)

* НЕ будем использовать другую переменную. Белая линия это половина цветной линии.
* Размер белой черты `size / 2`
* Новая переменная не нужна.

### Арифметические операции

* `size + 2`    сложить
* `size - 2`    вычесть
* `size / 2`    разделить
* `size * 2`    умножить

```python
# переменная col запомнит цвет
# переменная size запомнит размер линии
def dottedLine(col, size):
    t.color(col)   # передаем значение col другой команде
    
    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде

    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size
    
    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде

    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size
```

Вся программа:
```python
import turtle

# переменная col запомнит цвет
# переменная size запомнит размер отрезка
def dottedLine(col, size):
    t.color(col)   # передаем значение col другой команде
    
    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде

    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size
    
    # рисуем цветную линию
    t.pd()
    t.fd(size)     # передаем значение size другой команде

    # двигаем черепаху на size/2 без рисования
    t.pu()
    t.fd(size/2)   # вычисляем половину size
# Здесь закончилась новая команда dottedLine

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# вызываем dottedLine для разного цвета и размера
dottedLine('red', 30)      
dottedLine('green', 30)      
dottedLine('blue', 50)      
     

turtle.done()
```

## TASKTEST Задача: Треугольник из отрезков

* Написать функцию **dash(size)**. Она рисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/03_1dash.png)

* Использовать **dash(size)**. Нарисовать

![отрезки](https://stepik.org/media/attachments/lesson/479595/03_dash_tri.png)

## TASKTEST Задача: snowline(x)

* Написать функцию **snowline(x)**. Она рисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10.png)

## TASKTEST Задача: снежинки

* Написать функцию **snowline(x)**. Она рисует 1 луч снежинки.

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10.png)

* Написать функцию **snowflake(x)**. Она рисует 1 снежинку.

![snow flake](https://stepik.org/media/attachments/lesson/479594/func_t5.png)

* Использовать функцию `snowflake(x)`. Нарисовать много снежинок разного размера.

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10all.png)

## Квадратный корень

В python есть математические функции. Они собраны в библиотеке `math`.
Можно вычислить **квадратный корень** (square root).

Нарисуем отрезок длиной $\sqrt{200}$

```python
import math              # есть библиотека math

# ... много кода

t.fd( math.sqrt(200) )   # полное имя функции math.sqrt
```
Что нарисует эта программа?

```python
import turtle   # есть библиотека turtle
import math     # есть библиотека math

t = turtle.Turtle()  # вызываем функцию Turtle из библиотеки turtle
t.shape('turtle')
t.width(3)

t.fd(100)
t.lt(90)
t.fd(100)
t.lt(135)
t.fd(100*math.sqrt(2))

turtle.done()
```
## TASKTEST Задача: квадрат в квадрате

* Напишите функцию **sq(size)**. Она рисует 1 квадрат.
* Напишите функцию **sqin(size)**. Она рисует 2 квадрата так:

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t11.png)

## TASKTEST Задача: квадрат в квадрате + цвет

* Напишите функцию **sq(size, col)**. Она рисует 1 квадрат размера `size` цветом `col`.
* Напишите функцию **sqin(size, col)**. Она рисует 2 квадрата так:

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t12.png)
 
## Координаты

 Можно двигать (move) черепаху по указанным координатам. Черепаха не поворачивается.
 
```python
t.setpos(x, y) # двигать в точку с координатами (x,y)
t.goto(x, y)   # двигать в точку с координатами (x,y)
```

Функция **t.write(текст)** рисует текст черепахой. Можно написать координаты черепахи

```python
t.write(t.pos())
```

Что делает пример?
```python
import turtle

t = turtle.Turtle()

t.write(t.pos())    # (0,0)

t.setpos(100, -50)
t.write(t.pos())    # (100,-50)

t.goto(100, 50)
t.write(t.pos())		# (100, 50)
```

## TASKTEST Задача: функция line(x1, y1, x2, y2)

Напишите функцию **line(x1, y1, x2, y2)**. Она рисует линию и пишет координаты.

`line(-200, 50, 100, -50)` нарисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/line.png)

```python
import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')

def line(x1, y1, x2, y2):
    # тут нужно написать код функции
    
line(-200, 50, 100, -50)
    
turtle.done()
```

## TASKTEST Задача: треугольник по координатам

Напишите функцию **tri(x1, y1, x2, y2, x3, y3)**. 

Она рисует треугольник с вершинами в точках (x1, y1), (x2, y2), (x3, y3) и пишет их координаты.

`tri(-200, 200, 100, 0, -200, 0)` нарисует 

![треугольник](https://stepik.org/media/attachments/lesson/479595/coord_tri.png)

```python
import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

def tri(x1, y1, x2, y2, x3, y3):
    # тут нужно написать код функции
    
tri(-200, 200, 100, 0, -200, 0)
    
turtle.done()
```

## TASKTEST Задача: прямоугольник по координатам

Напишите функцию **rect(x1, y1, x2, y2, rect_col, text_col)**. Она рисует прямоугольник.

* x1, y1, x2, y1 - координаты противоположных вершин
* rect_color - цвет внутри
* text_color - цвет текста и линий.


`rect(-10, -20, 200, 150, "green", "red")` нарисует 

![треугольник](https://stepik.org/media/attachments/lesson/479595/coord_rect.png)

```python
import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def rect(x1, y1, x2, y2, rect_col, text_col):
    # тут нужно написать код функции
    
rect(-10, -20, 200, 150, "green", "red")
    
turtle.done()
```
