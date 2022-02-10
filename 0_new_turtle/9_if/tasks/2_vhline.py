import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def circle(x, y, r, col):
    # окружность радиуса r с центром в точке (x,y)
    t.color(col)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.stamp()
    t.pu()
    t.goto(x, y-r)
    t.pd()
    t.circle(r)

def vline(x0, col):
    # вертикальная линия x=x0
    t.color(col)
    t.pu()
    t.goto(x0, -200)
    t.pd()
    t.goto(x0, 200)

def hline(y0, col):
    # горизонтальная линия y=y0
    t.color(col)
    t.pu()
    t.goto(-200, y0)
    t.pd()
    t.goto(200, y0)

circle(0, 0, 100, 'blue')
hline(100, 'red')
vline(50, 'lightgreen')
    
turtle.done()
