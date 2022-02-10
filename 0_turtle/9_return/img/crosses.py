import turtle
import math

t = turtle.Turtle()
t.width(5)

# перемещаемся в точку p, ничего не рисуем.
def movetop(p):
    t.pu()
    t.goto(p)
    t.pd()
    
# рисуем линию из точки p1 в точку p2    
def linep(p1, p2):
    movetop(p1)
    t.goto(p2)
    
def uzor1(w, h):
    dx = w/5
    t.pu()
    # нижний ряд
    b1 = t.pos()
    t.fd(dx)
    b2 = t.pos()
    t.fd(dx)
    b3 = t.pos()
    t.fd(dx)
    b4 = t.pos()
    t.fd(dx)
    b5 = t.pos()
    t.fd(dx)
    b6 = t.pos()
            
    t.lt(90)        # поворот наверх
    t.fd(h)
    t.lt(90)
    
    t6 = t.pos()    # верхний ряд
    t.fd(dx)
    t5 = t.pos()
    t.fd(dx)
    t4 = t.pos()
    t.fd(dx)
    t3 = t.pos()
    t.fd(dx)
    t2 = t.pos()
    t.fd(dx)
    t1 = t.pos()
    
    t.lt(90)        # поворот вниз
    t.fd(h)
    t.lt(90)
    
    t.pd()

    linep(b1, b2)    # нижний ряд
    linep(b3, b4)
    linep(b5, b6)

    linep(t1, t2)    # верхний ряд
    linep(t3, t4)
    linep(t5, t6)

    linep(b1, t3)    # ////
    linep(b2, t4)
    linep(b3, t5)
    linep(b4, t6)

    linep(t1, b3)    # \\\\
    linep(t2, b4)
    linep(t3, b5)
    linep(t4, b6)
    
    return b6
    
def dummy(w, h):
    t.fd(w)
    p = t.pos()
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    return p

t.color('blue')
p = uzor1(200, 100)
t.color('red')
movetop(p)
p = uzor1(200, 100)

turtle.done()