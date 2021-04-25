import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def goto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    

def circle(x, y, r):
    goto(x, y)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def sq(x, y, a):
    goto(x, y)
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.lt(90)
    t.end_fill()

def tri(x, y, a):
    goto(x, y)
    t.begin_fill()
    for i in range(3):
        t.fd(a)
        t.lt(120)
    t.end_fill()


#t.color('green', 'lightgreen')    
#sq(-150, 0, 70)
#t.color('gold', 'yellow')
#circle(0, 0, 30)
#t.color('yellow', 'red')
#tri(70, 0, 80)


t.color('green', 'lightgreen')    
sq(0, 100, 70)
t.color('gold', 'yellow')
circle(40, 30, 30)
t.color('yellow', 'red')
tri(0, -50, 80)

t.ht()
    
turtle.done()
