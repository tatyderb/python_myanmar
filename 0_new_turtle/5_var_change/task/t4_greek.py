import turtle
def write(text):
    t.write(text, font = ("Arial", 14, "normal"))
            
def spi(size,d):
    t.color('blue')
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)

    t.color('green')
    size += d
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)

    t.color('red')
    size += d
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)

    t.color('gold')
    size += d
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)

    t.color('yellow')
    size += d
    write(size)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

spi(40,30)
turtle.done()
    
