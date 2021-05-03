# range

lesson = 529581

## range(5) - это числа от 0 до 4

В коде
```python
for i in range(5):
```
Создается переменная i и в нее записываются по очереди числа 0, 1, 2, 3, 4

Напишем число и перейдем к следующему
```python
for i in range(5):
    write(i)
    t.fd(50)
```

![0..4](https://stepik.org/media/attachments/lesson/479602/ex0.png)

Вся программа:

```python
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

for i in range(5):
    write(i)
    t.fd(50)

turtle.done()
```

## TASKTEXT Задача: числа от 0 до 6

Нарисовать так:

![0..6](https://stepik.org/media/attachments/lesson/479602/ex0t.png)

## range(2, 5)

**range(2, 5)** дает числа 2, 3, 4. 

**Числа 5 нет.**

Нарисуем числа
```python
for i in range(2, 5):
    write(i)
    t.fd(50)
```

![2..4](https://stepik.org/media/attachments/lesson/479602/ex0_1.png)

## TASKTEXT Задача: числа от 3 до 7

Нарисовать

![3..7](https://stepik.org/media/attachments/lesson/479602/ex0_1t.png)

## range(0, 200, 50)

**range(0, 200, 50)** дает числа 0, 50, 100, 150

Числа 200 нет.

От 0 до 200, увеличивать на 50.

```python
for x in range(0, 200, 50):
    t.goto(x, 0)
    write(x)
```

* Будем числа записывать в переменную х. 
* Иди черепахой в (x, 0) и пиши x.

Получится
![range(0, 200, 50)](https://stepik.org/media/attachments/lesson/479602/ex0_3.png)

## TASKTEXT -30 .. 170

Нарисовать
![-30..170](https://stepik.org/media/attachments/lesson/479602/ex0_3t.png)
