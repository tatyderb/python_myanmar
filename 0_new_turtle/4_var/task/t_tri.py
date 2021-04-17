import turtle


def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

def coord():
        x = int(t.xcor())
        y = int(t.ycor())
        write((x, y))


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')


def tri(x1, y1, x2, y2, x3, y3):
    t.pu()
    t.goto(x1, y1)
    t.pd()

    coord()

    t.goto(x2, y2)
    coord()

    t.goto(x3, y3)
    coord()

    t.goto(x1, y1)

tri(-200, 200, 100, 0, -200, 0)

turtle.done()
