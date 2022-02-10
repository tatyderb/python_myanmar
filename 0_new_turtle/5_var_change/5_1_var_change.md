# Изменяем значение переменых

lesson = 511880

## Повторение

Уже знаем:

```python
size = 200      # записать в переменную size значение 200
x = size / 2    # вычислить выражение, записать результат в переменную x
```
Как работает `x = size / 2`

| № | Что делает | Результат |
|----|------|----|
| 1 | читает значение переменной `size` | 200 |
| 2 | вычисляет `200 / 2` | 100 |
| 3 | результат записывает в `x` | 100 |

В `x` записали число 100.

## Математики и программисты

### Математики

Математики решают уравнения. $$x = x + 20$$ Корней нет.

### Программисты

У программистов нет уравнений. 

`куда = что` значит "записать в *куда* значение *что*".

`size = 200` записать в переменную `size` значение "число 200".

## SKIP VIDEO Спираль

Видео  https://www.youtube.com/watch?v=T0C52MCd8os  
от 42:44 до 50:48

https://youtu.be/i_gOwix1aQY

## Рисуем спираль

Значение переменной можно изменять.

Напишем функцию **spiral(size, direction)**. Она рисует спираль.

* **size** - размер первой линии
* **direction** это 1 или -1. <br/> Всегда будем поворачивать на `angel = direction*90`. <br/> Всегда `t.lt(angle)`

![спираль](https://stepik.org/media/attachments/lesson/479597/01_spi.png)

Спираль похожа на квадрат. Размер стороны `size` каждый раз больше: 20, 40, 60, 80, 100.

* Передадим в функцию переменную size - размер первой стороны.
* Следующая должна быть на 20 больше.
* Длина следующей стороны size + 20. Это значение для новой стороны запишем опять в переменную size.
```python
size = size + 20
```
Увеличили старое значение size на 20. Записали новое число в size.

То же самое:
```python
size += 20     # увеличить значение size на 20
```

## Вся функция

![спираль](https://stepik.org/media/attachments/lesson/479597/01_spi.png)

Напишем функцию. Она рисует спираль:

Аргумент **direction** может быть 1 (повороты налево) или -1 (повороты направо).

```python
def spiral(size, direction):
    # угол поворота зависит от direction 
    angle = 90 * direction

    t.fd(size)
    # старое значение size увеличиваем на 20 
    # новое значение записываем в size
    size = size + 20  
    
    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20
    
    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20

    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20

    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20
```

## SKIP VIDEO Вызываем функцию, рисуем 2 спирали

https://youtu.be/5lKFqqmAcBo

## TASKTEXT Задача: Изменяем значение переменной

Аргумент **direction** может быть 1 (повороты налево) или -1 (повороты направо).

**Функцию spiral(size, direction) МЕНЯТЬ НЕЛЬЗЯ**. Можно вызвать функцию с разными аргументами.

Нарисуйте: 

![спирали](https://stepik.org/media/attachments/lesson/479597/01_spi2.png)

```python
import turtle

def spiral(size, direction):
    # direction = 1 поворот на 90 градусов
    # direction = -1 поворот на -90 градусов

    # угол поворота зависит от direction 
    angle = 90 * direction

    t.fd(size)
    # старое значение size увеличиваем на 20 
    # новое значение записываем в size
    size = size + 20  
    
    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20
    
    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20

    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20

    t.lt(angle)
    t.fd(size)          # измененное значение size
    size = size + 20    # увеличиваем size на 20
    
t = turtle.Turtle()
t.width(3)
t.color('red')

spiral(20, 1)
# тут нужно написать код

turtle.done()    
```

## Длинная и короткая запись

Значение переменной можно изменить.

```python
size = size + 20   # увеличить на 20
size += 20         # увеличить на 20

size = size - 20   # уменьшить на 20
size -= 20         # уменьшить на 20

size = size * 3    # увеличить в 3 раза
size += 20         # увеличить в 3 раза

size = size / 2    # уменьшить в 2 раза
size /= 2          # уменьшить в 2 раза
```

## Увеличить и уменьшить

Нарисуем

![увеличиваем и уменьшаем](https://stepik.org/media/attachments/lesson/479597/03_lines_up.png)

Можно изменять переменную на значение другой переменной.

Напишем функцию **lines(size, d)**. Она рисует 4 линии. Первую длиной size. Каждую следующую на d больше.

```python
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

# size - длина первой линии    
# d - на сколько будем изменять size
def lines(size, d):
    t.down()

    t.color("blue")
    write(size)           # пиши размер синей линии
    t.fd(size)
    
    size += d             # увеличили size НА d 
    
    t.color("darkgreen")
    write(size)           # пиши размер зеленой линии
    t.fd(size)
    
    size += d             # увеличили size еще НА d 
    
    t.color("red")
    write(size)           # пиши размер красной линии
    t.fd(size)

    size += d             # увеличили size еще НА d 
    
    t.color("gold")
    write(size)           # пиши размер желтой линии
    t.fd(size)
    

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

t.up()
t.goto(-300, 0)

p = t.pos()
lines(80, 40)   # size будет 80, d будет 40
                # длина линии будет увеличиваться
t.up()                
t.goto(p)       # встанем на 50 выше
t.seth(90)
t.fd(50)
t.seth(0)
                
lines(200, -40) # size будет 200, d будет -40
                # длина линии будет уменьшаться
                
turtle.done()
```
