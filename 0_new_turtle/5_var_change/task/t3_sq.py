import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

def sq(size, ang, col1, col2):
    t.color(col1, col2)
    t.seth(ang)
    t.begin_fill()
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.end_fill()

def sq3(size, ang):
    sq(size, ang, 'blue', 'green')

    t.fd(size/2)
    ang += 45
    size = size / math.sqrt(2)

    sq(size, ang, 'red', 'yellow')
    
    t.fd(size/2)
    ang += 45
    size = size / math.sqrt(2)

    sq(size, ang, 'orange', 'white')

sq3(150, 0)

turtle.done()
