import turtle
import math

def sq(size, col1, col2):
    t.color(col1, col2)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

def sqn(size, n):
    for i in range(n):
        sq(size, 'blue', 'green')
        t.fd(size/2)
        t.lt(45)
        
        size = size / math.sqrt(2)

        sq(size, 'red', 'yellow')
        t.fd(size/2)
        t.lt(45)

        size = size / math.sqrt(2)

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
sqn(200, 4)

shift(200, -100)
sqn(80, 1)

shift(150, -150)
sqn(120, 3)

turtle.done()
