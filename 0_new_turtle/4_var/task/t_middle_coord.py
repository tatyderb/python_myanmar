import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

# координаты черепахи, целые числа
def coord():
        x = int(t.xcor())
        y = int(t.ycor())
        write((x, y))


def middleLine(x1, x2):
    t.color('blue')

    # перейти в (x1, 0) и начать рисовать
    t.pu()
    t.goto(x1, 0)
    t.pd()
    
    coord()
    # линия от (x1, 0) до (x2, 0)
    t.goto(x2, 0)
    coord()

    # вычислили длину половины отрезка и сохранили в half
    half = (x2 - x1) / 2    

    t.goto(x1 + half, 0)
    t.color('red')
    coord()

middleLine(-200, 100)

turtle.done()
