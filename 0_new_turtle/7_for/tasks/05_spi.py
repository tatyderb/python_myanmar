import turtle

def spi(n, col):
    t.color(col)
    size = 20
    d = 15
    for i in range(n):
        t.fd(size)
        t.lt(90)
        size = size + d    # size += d


def shift(dx, dy):
    x = t.xcor()
    y = t.ycor()
    t.pu()
    t.setpos(x+dx, y+dy)
    t.pd()


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

t.seth(-90)
shift(-200, 0)
spi(10, 'green')

t.seth(-90)
shift(80, 30)
spi(7, 'red')

t.seth(-90)
shift(120, -150)
spi(15, 'blue')

turtle.done()
