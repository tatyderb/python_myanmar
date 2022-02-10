import turtle
import math

def sq(size, col):
        t.color(col)
        t.fd(size)
        t.lt(90)

        t.fd(size)
        t.lt(90)

        t.fd(size)
        t.lt(90)

        t.fd(size)
        t.lt(90)

def sqin(size, col1, col2):
        sq(size, col1)
        t.fd(size/2)
        t.lt(45)
        sq(size/math.sqrt(2), col2)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

sqin(150, 'blue', 'black')

turtle.done()
