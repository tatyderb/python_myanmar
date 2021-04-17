import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

def line(r, size):
    t.pu()
    t.fd(r)
    t.pd()
    t.fd(size)
    t.pu()
    t.bk(size + r)

def sun(r, size, angle, col):
    t.color(col)
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

    line(r, size)
    angle += 36
    t.seth(angle)

def sun3(r, size):
    ang0 = 90
    d = 10
    sun(r, size - 2*d, ang0, 'yellow')
    ang0 += 12
    sun(r - d, size, ang0, 'orange')
    ang0 += 12
    sun(r, size, ang0, 'red')
    ang0 += 12
    
sun3(40, 100)

turtle.done()
