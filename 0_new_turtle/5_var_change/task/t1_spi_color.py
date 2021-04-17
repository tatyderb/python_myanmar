import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def spi(size, d):
    t.color('blue')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    size = size + d     # увеличили size на d

    t.color('green')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    size = size + d     # увеличили size на d

    t.color('red')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    size = size + d     # увеличили size на d

    t.color('orange')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    size = size + d     # увеличили size на d

    t.color('yellow')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    size = size + d     # увеличили size на d

    
spi(40, 30)

turtle.done()
