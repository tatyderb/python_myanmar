import turtle
import math

def sq(size, col):
    t.color('green', col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

def sq2(size, col1, col2):
    sq(size, col1)
    t.fd(size)
    sq(size, col2)
    t.fd(size)

def row(n, size):
    for i in range(n):
        sq2(size, 'red', 'yellow')

def row2(n, size):
    row(n, size)
    t.lt(180)
    row(n, size)
    t.lt(180)
    shift(0, -size*2)
    
def carpet(n, m, size):
    for i in range(m):
        row2(n, size)

def shift(dx, dy):
    x = t.xcor()
    y = t.ycor()
    t.pu()
    t.setpos(x+dx, y+dy)
    t.pd()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

shift(-200, 0)
# carpet(2, 1, 40)
carpet(5, 4, 40)

turtle.done()
