import turtle
t = turtle.Turtle()
t.width(4)

def triangle(color):
    t.color(color)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

def sq(color):
    t.color(color)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

def uzor():
    sq("orange")
    t.left(45)
    sq("green")
    t.left(135)
    triangle("red")
    t.left(90)
    triangle("blue")

uzor()
turtle.done()

