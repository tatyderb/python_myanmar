# speed, stamp, sethead

lesson = 505710

## Скорость черепахи

Черепаха может двигаться с разной скоростью.

`t.`**speed(n)** - скорость черепахи, n от 0 до 10.

* `t.speed(1)` - самая медленная(slowest)
* `t.speed(3)` - медленная (slow)
* `t.speed(6)` - нормальная (normal)
* `t.speed(10)` - быстрая (fast)
* `t.speed(0)` - самая быстрая (fastest)

## след

Мы оставляем следы. Черепаха тоже может оставить след.

`t.`**stamp()** - оставить след. Отпечаток черепахи.

![stamped_line](https://stepik.org/media/attachments/lesson/505710/stamped_line.png)

Нарисуем

![stamped_line](https://stepik.org/media/attachments/lesson/505710/stamped_line_description.png)

```python
import turtle

def stamped():
    t.color('red')
    t.stamp()           # отпечаток
    t.fd(100)           # линия

    t.color('green')
    t.stamp()           # отпечаток
    t.fd(100)           # линия

    t.color('gold')
    t.stamp()           # отпечаток
    t.fd(100)           # линия

    t.color('blue')
    t.stamp()           # отпечаток
    t.fd(100)           # линия

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

stamped()

turtle.done()
```

![следы](https://stepik.org/media/attachments/lesson/505710/pngwing.com.png)

## setheading - повернуть черепаху

* **right** и **left** - относительные команды
* **setheading** - абсолютная команда

![компас](https://stepik.org/media/attachments/lesson/505710/kompas1.jpg)

* `t.`**right(ang)** - повернуть черепаху на `ang` градусов **относительно положения черепахи**
* `t.`**left(ang)** - повернуть черепаху на `ang` градусов **относительно положения черепахи**
* `t.`**setheading(ang)** - поставить черепаху на `ang` градусов (относительно оси Х и Y)
* `t.`**seth(ang)** - короткая форма команды `t.setheading(ang)`

![крест](https://stepik.org/media/attachments/lesson/505710/seth.png)

### left, right

Относительные команды. 0 градусов, +90 градусов, +90 градусов, +90 градусов.

```python
import turtle

def line():
    t.fd(100)
    t.bk(100)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
            
line()    # 0 градусов

t.lt(90)    # +90 градусов = 90 градусов
line()

t.lt(90)    # +90 градусов = 180 градусов
line()

t.lt(90)    # +90 градусов = 270 градусов
line()

turtle.done()
```

### seth

Абсолютные команды. 0 градусов, 90 градусов, 180 градусов, -90 градусов.

```python
import turtle

def line():
    t.fd(100)
    t.bk(100)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
            
line()      # 0 градусов

t.seth(90)  # 90 градусов
line()

t.seth(180) # 180 градусов
line()

t.seth(-90) # -90 градусов = 270 градусов
line()

turtle.done()
```

## Где 0 градусов?

В разных системах может быть разный `t.seth(0)`. Или обычный. Или как в черепахе лого.

| код | Обычно | Как в черепахе logo |
|----|----|----|
| `t.seth(0)` | 0 - восток (east) | 0 - север (north) |
| `t.seth(90)` | 90 - север (north) | 90 - восток (east) |
| `t.seth(180)` | 180 - запад (west) | 180 - юг (south) |
| `t.seth(270)` | 270 - юг (south) | 270 - запад (west) |


## TASKTEXT ромашка

* Написать функцию **petal()**. Она рисует:

![лепесток](https://stepik.org/media/attachments/lesson/505710/petal.png)

* Написать функцию **flower()** Нарисовать:

![цветок](https://stepik.org/media/attachments/lesson/505710/flower.png)

Цвета red, orange.

Углы 0, 20, 45, 90, -20, -45, -90 градусов.
