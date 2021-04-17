import turtle

def tri(size, ang):
    p0 = t.pos()
    t.fd(size)
    p1 = t.pos()
    t.bk(size)
    t.lt(ang)
    t.fd(size)
    t.goto(p1)
    t.goto(p0)

def poly(n, size):
    ang = 360 / n       # угол вычислить 1 раз до цикла
    
    for i in range(n):  # повторить n раз
        tri(size, ang)
        
def shift(dx, dy):
    x = t.xcor()
    y = t.ycor()
    t.pu()
    t.setpos(x+dx, y+dy)
    t.pd()


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

shift(-200, 0)
poly(4, 100)
shift(220, 0)
poly(9, 100)
shift(220, 0)
poly(5, 100)

turtle.done()
