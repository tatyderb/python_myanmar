import turtle

def line(size):
        t.pd()
        t.fd(size/3)
        t.pu()
        t.fd(size/3)
        t.pd()
        t.fd(size/3)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')

line(150)
t.lt(120)
line(150)
t.lt(120)
line(150)
t.lt(120)

turtle.done()
