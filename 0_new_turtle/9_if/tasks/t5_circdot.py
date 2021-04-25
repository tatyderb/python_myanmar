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

def  cdot(x, y, x0, y0, r):
    """
    x, y - координаты точки
    x0, y0 - координаты центра окружности
    r - радиус окружности
    условие, что точка внутри окружности
    (x - x0)**2 + (y - y0)**2 < r**2
    """
    # Если вы уже прочитали про return, напишите функцию
    # dist(x, y, x0, y0), которая возвращает квадрат расстояния между точками
    # вычислим квадрат расстояния между точкой и центром окружности:
    dx = x - x0
    dy = y - y0
    d2 = dx * dx + dy * dy

    if d2 < r*r:
        col = 'green'
    else:
        col = 'yellow'
        
    moveto(x, y)
    t.color(col)
    t.dot(10)
    
t = turtle.Turtle()
t.width(3)

x0 = 0
y0 = -10
r = 100
circle(x0, y0, r)
cdot(-70, -40, x0, y0, r)     # зеленая
cdot(80, 60, x0, y0, r)       # желтая
cdot(50, 40, x0, y0, r)       # зеленая на рисунке
cdot(-100, -50, x0, y0, r)    # желтая на рисунке

turtle.done()
