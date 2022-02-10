# Изменение переменных

lesson = 479597

## Видео

Видео  https://www.youtube.com/watch?v=T0C52MCd8os  
от 42:44 до 50:48

## Изменяем значение переменной

Значение переменной можно изменять.

Напишем функцию **spiral(size, direction)**. Она рисует спираль.

![спираль](https://stepik.org/media/attachments/lesson/479597/01_spi.png)

Спираль похожа на квадрат. Размер стороны size каждый раз больше: 20, 40, 60, 80, 100.

* Передадим в функцию переменную size - размер первой стороны.
* Следующая должна быть на 20 больше.
* Длина следующей стороны size + 20. Это значение для новой стороны запишем опять в переменную size. 

```python
size = size + 20
```
Увеличили старое значение size на 20 и записали новое число в size.

То же самое:
```python
size += 20     # увеличить значение size на 20
```

Напишем функцию. Она рисует спираль:
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
Аргумент **direction** может быть 1 (повороты налево) или -1 (повороты направо).

## TASKTEXT: Задача: Изменяем значение переменной

Аргумент **direction** может быть 1 (повороты налево) или -1 (повороты направо).

**Не меняйте функцию spiral(size, direction)**. Используйте только эту функцию.

Нарисуйте 

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

## TASKTEXT Задача: спираль разные цвета

Напишите функцию spi(size, d). Она рисует спираль. Первый отрезок длины size. Следующие на d больше. 
После 2 линий размер стороны увеличивается на d. Написать длину новой линии.
Цвета могут быть другие.

![цветная спираль](https://stepik.org/media/attachments/lesson/479597/spNa1.png)

## TASKTEXT Задача: солнце

* Написать функцию **sun(r, size, angle, col)**
    * r - радиус круга солнца
    * size - длина луча
    * angle - на anlge повернуть первый луч. Используйте `t.sethand(angle)`
    * col - цвет всех лучей
* Написать функцию **sun3(r, size)**. Она использует `sun(r, size, angle, col)` и рисует 

![солнце](https://stepik.org/media/attachments/lesson/479597/sun.png)

## TASKTEXT Задача: вписанные квадраты

* Напишите функцию **sq(size, ang, col1, col2)**. Она рисует 1 квадрат
    * size - сторона квадрата
    * ang - угол поворота квадрата
    * col1 - цвет линии
    * col2 - цвет заливки
* Напишите функцию **sq3(size, ang)**. Она рисует 3 квадрата.

Так:

![квадраты](https://stepik.org/media/attachments/lesson/479597/kv3.png)

или так:

![квадраты](https://stepik.org/media/attachments/lesson/479597/kv33.png)

## TASKTEXT Задача: 1 спираль 

Напишите функцию **spi(size, d)**.  Сначала длина увеличивается на d, потом уменьшается на d.

![спираль](https://stepik.org/media/attachments/lesson/479597/spNa2.png)

## TASKTEXT Задача: 2 спирали

* Возьмите функцию  spi(size, d)  из предыдущей задачи.
* Напишите функцию size(spi, d), Она рисует 2 спирали.

![2 спирали](https://stepik.org/media/attachments/lesson/479597/spir2.png)

## TASKTEXT Задача: греческий узор

* Возьмите функции из предыдущих задач.
* Напишите функцию spiral(size, d). Она рисует 

![цветная спираль](https://stepik.org/media/attachments/lesson/479597/sps.png)
