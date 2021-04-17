import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def square(x, y, size):
    t.color('red')
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(10)


    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2


    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()


    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)


    # вычислить длину диагонали
    # результат записать в переменную d
    d = math.sqrt(2) * size


    # нарисовать диагональ
    t.lt(45)
    t.fd(d)         # читаем число из переменной d

    t.rt(135)
    t.fd(size)
    t.rt(135)

    t.fd(d)         # читаем число из переменной d

square(50, -100, 150)


turtle.done()
