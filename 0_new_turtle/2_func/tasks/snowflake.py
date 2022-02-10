import turtle
import math

t=turtle.Turtle()
t.shape('turtle')
t.pensize(4)
t.pencolor('blue')

def snowline():
    t.fd(110)
    t.bk(35)
    t.lt(45)
    t.fd(35)
    t.bk(35)
    t.rt(90)
    t.fd(35)
    t.bk(35)
    t.lt(45)
    t.bk(75)

def snowflake():
    snowline()
    t.lt(60)
    snowline()
    t.lt(60)
    snowline()
    t.lt(60)
    snowline()
    t.lt(60)
    snowline()
    t.lt(60)
    snowline()
    t.lt(60)

snowflake()
turtle.done()
