import turtle
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def dashes(size):
    part = size/3
    t.color('red')
    t.fd(part)
    t.color('blue')
    t.fd(part)
    t.color('red')
    t.fd(part)

dashes(150)

turtle.done()
