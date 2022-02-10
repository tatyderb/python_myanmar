import turtle
import math

def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)
    
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
    
    p1 = t.pos()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    p2 = t.pos()

    
    t.lt(90)
    t.fd(size)
    p3 = t.pos()
    
    t.lt(90)
    t.fd(size)
    p4 = t.pos()
    
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # нарисовать диагональ
    t.goto(p3)        # прочитаем точку из переменной p3
    # перейти в точку p2
    t.goto(p2)        # прочитаем точку из переменной p2
    # нарисовать вторую диагональ
    t.goto(p4)        # прочитаем точку из переменной p4    
    
t = turtle.Turtle()
t.width(3)
t.color('red')

square(-100, -50, 100)

turtle.done() 
