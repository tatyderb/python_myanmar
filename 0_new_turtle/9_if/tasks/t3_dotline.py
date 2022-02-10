import turtle


def moveto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def hline(y):
    moveto(-100, y)
    t.goto(100, y)


def cdot(x, y, y0):
    moveto(x, y)
    if y > y0:
        col = 'red'
    else:
        col = 'blue'
    t.color(col)
    t.dot(5)
    # t.write(t.pos())


t = turtle.Turtle()
t.width(3)


# Пример 1: точка сверху
# y0 = 0
# x = -20
# y = 50


# Пример 2: точка снизу
y0 = 100
x = 50
y = 70

# Проверим оба случая сразу: сверху и снизу
y0 = 100
hline(y0)
cdot(20, 50, y0)    # снизу, синий
cdot(150, 50, y0)   # снизу, синий
cdot(0, 150, y0)    # сверху, красный
cdot(200, 150, y0)  # сверху, красный


turtle.done()
