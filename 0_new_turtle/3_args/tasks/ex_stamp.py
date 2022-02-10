import turtle

def line():
    t.fd(100)
    t.bk(100)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
            
line()    # 0 градусов

t.lt(90)    # +90 градусов = 90 градусов
line()

t.lt(90)    # +90 градусов = 180 градусов
line()

t.lt(90)    # +90 градусов = 270 градусов
line()

turtle.done()
