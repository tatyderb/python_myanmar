import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def circle(x, y, r, col):
    t.color(col)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.stamp()
    t.pu()
    t.goto(x, y-r)
    t.pd()
    t.circle(r)

circle(0, 0, 100, 'blue')
circle(0, 100, 50, 'gold')
circle(75, 0, 25, 'red')
    
turtle.done()
