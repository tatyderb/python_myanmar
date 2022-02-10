# Разработка программы

lesson = 505711

## Задача

Как решать большую задачу? Нужно сделать из 1 большой задачи много маленьких задач.

Есть задача. Как решать? Напишем функцию **uzor()**

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10all.png)

Маленькие задачи:

* нарисовать 1 снежинку. Напишем функцию **snowflake(size)**
    * 1 снежинка = 6 лучей снежинки. Напишем функцию **snowline(x)**
* где рисовать снежинки, какого размера. Напишем функцию **uzor()**. Вместо снежинки будем рисовать `+`.
    * Напишем функцию **cross()**. Она рисует `+`.

![snow flake](https://stepik.org/media/attachments/lesson/479594/func_t5.png)

1 снежинка = 6 лучей снежинки.

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10.png)

Разбили задачу на маленькие задачи. Будем писать функции.

## Шаг 1. Функция slowline(x)

![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10.png)

Потом будет 6 лучей.

Хорошо: старт и финиш совпадают.

Написали программу. Запустили программу. Исправили ошибки.
```python
import turtle

def snowline(x):
        t.fd(2*x)       # --

        t.lt(45)        #   /
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   -
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   \
        t.fd(x)
        t.bk(x)

        t.lt(45)        # --
        t.bk(2*x)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

snowline(50)

turtle.done()
```

## Шаг 2. Функция snowflake(size)

* **snowflake(size)**, где **size** - радиус снежинки или длина луча.
* **snowline(x)**, где 3x - радиус снежинки.

Надо:

* определить новую функцию **snowflake(size)**
* вызвать **snowflake(50)**, проверить функцию.

```python
import turtle

def snowline(x):
        t.fd(2*x)       # --

        t.lt(45)        #   /
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   -
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   \
        t.fd(x)
        t.bk(x)

        t.lt(45)        # --
        t.bk(2*x)

def snowflake(size):
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

# snowline(50) уже работает, не удаляем, а ставим #
snowflake(150)

turtle.done()
```

## Шаг 3. Где рисовать? Какого размера?

Надо найти:

* где рисовать снежинки
* размер снежинки

Снежинку рисовать долго. Будем пока рисовать крест `+`. Функция **cross(size)**

![cross](https://stepik.org/media/attachments/lesson/505710/seth.png)

```python
import turtle

# тут функции snowline(x) и snowflake(size)
# ...

def cross(size):
        t.fd(size)
        t.bk(size)
        t.lt(90)
        
        t.fd(size)
        t.bk(size)
        t.lt(90)

        t.fd(size)
        t.bk(size)
        t.lt(90)

        t.fd(size)
        t.bk(size)
        t.lt(90)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

# snowline(50) уже работает, не удаляем, ставим # в начале
# snowflake(150) уже работает, не удаляем, ставим # в начале
cross(150)

turtle.done()
```

## Шаг 4. Узор из +

Нарисуем где и какого размера.

У вас может быть другой размер и угол.

* t.**speed(0)** - рисуем быстро
* t.**stamp()** - где стоит черепаха
* красный путь. Потом будет up() и down().

![черновик](https://stepik.org/media/attachments/lesson/505711/snow_draft.png)

```python
import turtle

# тут функции snowline(x) и snowflake(size) и cross(size)
# ...

def uzor_draft():
        t.color('blue')
        cross(150)
        
        t.color('red')
        t.rt(150)
        t.fd(150+75)
        t.seth(0)
        
        t.color('blue')
        cross(75)

        t.color('red')
        t.lt(90)
        t.fd(150+75)
        t.seth(0)
        
        t.color('blue')
        cross(40)


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
t.speed(0)

uzor_draft()

turtle.done()
```

## Шаг 5. Рисуем снежинки

Заменим в uzor_draft:

* cross на snowflake
* `t.color('blue')` на `t.pd()`
* `t.color('red')` на `t.pu()`


![отрезки](https://stepik.org/media/attachments/lesson/479595/func_t10all.png)

Вся программа:
```python
import turtle

def snowline(x):
        t.fd(2*x)       # --

        t.lt(45)        #   /
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   -
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   \
        t.fd(x)
        t.bk(x)

        t.lt(45)        # --
        t.bk(2*x)

def snowflake(size):
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)
        snowline(size/3)
        t.lt(60)

def cross(size):
        t.color('blue')
        t.fd(size)
        t.bk(size)
        t.lt(90)
        
        t.fd(size)
        t.bk(size)
        t.lt(90)

        t.fd(size)
        t.bk(size)
        t.lt(90)

        t.fd(size)
        t.bk(size)
        t.lt(90)

def uzor_draft():
        cross(150)
        
        t.color('red')
        t.rt(150)
        t.fd(150+75)
        t.seth(0)
        
        cross(75)

        t.color('red')
        t.lt(90)
        t.fd(150+75)
        t.seth(0)
        
        cross(40)

def uzor():
        snowflake(150)
        
        t.pu()
        t.rt(150)
        t.fd(150+75)
        t.seth(0)
        t.pd()
        
        snowflake(75)

        t.pu()
        t.lt(90)
        t.fd(150+75)
        t.seth(0)
        t.pd()
        
        snowflake(40)


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
t.speed(0)

# snowline(50) уже работает, не удаляем, ставим # в начале
# snowflake(150) уже работает, не удаляем, ставим # в начале
# cross(150)
uzor()

turtle.done()
```
