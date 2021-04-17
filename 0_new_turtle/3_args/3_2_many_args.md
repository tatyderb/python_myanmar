# Несколько аргументов

lesson = 505565

## SKIP VIDEO 

[youtube](https://youtu.be/a3HhXItMEPs)

## Аргументы цвет и размер

[youtube](https://youtu.be/VrGHxeBnKqY)

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

## TASKTEXT Задача: треугольники разных размеров

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

## TASKTEXT нужна задача

на закрепление функции с 2 аргументами

## SKIP VIDEO dashed line

[youtube](https://youtu.be/VrGHxeBnKqY)

## Изменить значение переменной

[youtube](https://youtu.be/VrGHxeBnKqY)

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

## TASKTEXT Задача: Треугольник из отрезков

* Написать функцию **dash(size)**. Она рисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/03_1dash.png)

* Функция **dtri(size)**
    * **size** - длина стороны **треугольника**
    * использовать **dash**(size)

![отрезки](https://stepik.org/media/attachments/lesson/479595/03_dash_tri.png)

## TASKTEXT Задача: snowline(x)

* Написать функцию **snowline(x)**. Она рисует 

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10.png)

## TASKTEXT Задача: снежинки

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

## TASKTEXT Задача: квадрат в квадрате

* Напишите функцию **sq(size)**. Она рисует 1 квадрат.
* Напишите функцию **sqin(size)**. Она рисует 2 квадрата так:

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t11.png)

## TASKTEXT Задача: квадрат в квадрате + цвет

* Напишите функцию **sq(size, col)**. Она рисует 1 квадрат размера `size` цветом `col`.
* Напишите функцию **sqin(size, col1, col2)**. Она рисует 2 квадрата так:

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t12.png)
 
