import turtle


def poly(col, n, size):
    t.color(col)        # цвет изменить 1 раз ДО цикла
    ang = 360 / n       # угол вычислить 1 раз до цикла
    
    for i in range(n):  # повторить n раз
        t.fd(size)
        t.lt(ang)

def shift(dx, dy):
    x = t.xcor()
    y = t.ycor()
    t.pu()
    t.setpos(x+dx, y+dy)
    t.pd()


t = turtle.Turtle()
t.shape('turtle')
t.width(3)

shift(-200, 0)
poly('blue', 8, 100)
shift(220, 0)
poly('red', 4, 100)
shift(180, 0)
poly('green', 5, 100)

turtle.done()
