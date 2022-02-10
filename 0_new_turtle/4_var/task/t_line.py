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
t.color('red')


def line(x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()

    coord()
    t.goto(x2, y2)
    coord()


line(-200, 50, 100, -50)

turtle.done()
