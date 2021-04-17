import turtle

def petal():
    t.color('red')
    t.fd(100)
    t.stamp()
    t.color('orange')
    t.bk(100)

def flower():
    petal()
    t.seth(20)
    petal()
    t.seth(45)
    petal()
    t.seth(90)
    petal()
    t.seth(-20)
    petal()
    t.seth(-45)
    petal()
    t.seth(-90)
    petal()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# petal()
flower()

turtle.done()
