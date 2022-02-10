import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def circle(x, y, r):
    t.pu()
    t.goto(x, y-r)
    t.pd()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

t.color('blue', 'orange')
circle(0, 0, 100)

t.color('green', 'lightgreen')
circle(0, 100, 50)

t.color('red', 'yellow')
circle(75, 0, 25)

    
turtle.done()
