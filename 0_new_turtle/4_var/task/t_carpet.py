import turtle
import math

def line(p1, p2):
    t.pu()
    t.goto(p1)
    t.pd()
    t.goto(p2)

def part(w, h):
    a = w / 5

    # запоминаем нижние точки
    t.pu()
    b1 = t.pos()
    t.fd(a)
    b2 = t.pos()
    t.fd(a)
    b3 = t.pos()
    t.fd(a)
    b4 = t.pos()
    t.fd(a)
    b5 = t.pos()
    t.fd(a)
    b6 = t.pos()

    # проходим наверх
    t.lt(90)
    t.fd(h)
    t.lt(90)

    # запоминаем верхний ряд
    t6 = t.pos()
    t.fd(a)
    t5 = t.pos()
    t.fd(a)
    t4 = t.pos()
    t.fd(a)
    t3 = t.pos()
    t.fd(a)
    t2 = t.pos()
    t.fd(a)
    t1 = t.pos()
    t.lt(180)

    # рисуем линии - - - внизу
    line(b1, b2)
    line(b3, b4)
    line(b5, b6)
    
    # рисуем линии - - - вверху
    line(t1, t2)
    line(t3, t4)
    line(t5, t6)

    # рисуем линии ////
    line(b1, t3)
    line(b2, t4)
    line(b3, t5)
    line(b4, t6)
    
    # рисуем линии \\\\
    line(t1, b3)
    line(t2, b4)
    line(t3, b5)
    line(t4, b6)

    # идем в b6, будем рисовать следующий узор
    t.pu()
    t.goto(b6)
    
    
t = turtle.Turtle()
t.width(3)
t.color('red')

part(100, 50)

turtle.done() 
