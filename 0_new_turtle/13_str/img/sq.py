import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.speed(0)

def sq(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

t.color(input())
sq(int(input()))

turtle.done()
