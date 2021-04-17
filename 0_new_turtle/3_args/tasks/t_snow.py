import turtle

def snowline(x):
        t.fd(2*x)       # --

        t.lt(45)        #   /
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   -
        t.fd(x)
        t.bk(x)

        t.rt(45)        #   \
        t.fd(x)
        t.bk(x)

        t.lt(45)        # --
        t.bk(2*x)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

snowline(50)

turtle.done()
