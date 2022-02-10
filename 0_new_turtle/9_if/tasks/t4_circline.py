import turtle


def moveto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def hline(y):
    moveto(-100, y)
    t.goto(100, y)

def vline(x):
    moveto(x, -100)
    t.goto(x, 100)

def circle(x, y, r):
    moveto(x, y)
    t.color('red')
    t.dot(10)

    moveto(x, y-r)
    t.color('blue')
    t.circle(r)

def  circleright(x, y, r, x0):
    # квадрат расстояния от центра окружности до прямой
    # dx2 = (x - x0) * (x - x0)
    # if dx2 > r*r:
    if x0 < x - r:
        circle(x, y, r)
    else:
        col = 'red'
        moveto(x, y)
        t.write('Не буду рисовать')

t = turtle.Turtle()
t.width(3)

x0 = 100
vline(x0)
circleright(80, 0, 50, x0)  # нет
circleright(170, 0, 50, x0) # ok
circleright(-70, 60, 90, x0) # ok

turtle.done()
