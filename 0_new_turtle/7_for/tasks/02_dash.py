import turtle


def dash(col, n):
    t.color(col)
    size = 40
    d = 30
    for i in range(n):  # повторить n раз
        t.pd()
        t.fd(size)
        t.pu()
        t.fd(d)


t = turtle.Turtle()
t.shape('turtle')
t.width(3)

t.pu()
t.bk(300)

dash('blue', 3)
dash('red', 2)
dash('green', 5)

turtle.done()
