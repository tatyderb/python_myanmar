import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

def write(text):
    t.write(text, font=('Arial', 14, 'normal'))

# 1 квадрат со стороной size, цвет col
def csq(size, col):
    t.color('gold', col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

# по числу i определить цвет
def getColor(i):
    if i % 3 == 0:
        col = 'red'
    elif i % 3 == 1:
        col = 'yellow'
    else : 
        col = 'green'
    return col        # вернуть цвет

# n квадратов со стороной size
def csq3(size, d, n):
    x = t.xcor()
    y = t.ycor()
    # вычислим где рисовать число
    y = y + size + 50

    i = 0       # уже нарисовали квадратов

    while size > 0 and i < n:
        t.pd()
        col = getColor(i)
        csq(size, col)
        t.pu()
        t.fd(d/2)
        t.lt(90)
        t.fd(d/2)
        t.rt(90)
        size = size - d
        i = i + 1

    t.pu()
    t.goto(x, y)
    t.pd()
    write(i)

csq3(150, 20, 5)

turtle.done()
