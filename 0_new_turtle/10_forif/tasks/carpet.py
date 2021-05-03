import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

# 1 квадрат со стороной size, цвет col
def csq(size, col):
    t.color('gold', col)
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

# по числу i определить цвет
def getColor(i, col1, col2):
    if i % 2 == 0:    # i четное
        col = col1    # цвет col1
    else :            # иначе (нечетное)
        col = col2    # цвет col2
    return col        # вернуть цвет

# n квадратов со стороной size; цвет первого квадрата col1, второго col2
def csq_row(size, n, col1, col2):
    for i in range(n):
        col = getColor(i, col1, col2)
        csq(size, col)
        t.fd(size)

def goto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

# горизонтальные линии
# прямоугольник n рядов, m квадратов в ряду
def hcarpet(size, n, m):
    t.rt(90)
    
    x = t.xcor()
    y = t.ycor()

    for i in range(m):
        csq_row(size, n, 'red', 'yellow')
        x = x + size
        goto(x, y)

# вертикальные линии
# прямоугольник n рядов, m квадратов в ряду
def vcarpet(size, n, m):
    
    x = t.xcor()
    y = t.ycor()

    for i in range(n):
        csq_row(size, m, 'red', 'yellow')
        y = y - size
        goto(x, y)    

# шахматная доска
# прямоугольник n рядов, m квадратов в ряду
def chess(size, n, m):
    
    x = t.xcor()
    y = t.ycor()

    for i in range(n):
        if i % 2 == 0:
            csq_row(size, m, 'red', 'yellow')
        else:
            csq_row(size, m, 'yellow', 'red')
        y = y - size
        goto(x, y)    


# hcarpet(40, 5, 7)
# vcarpet(40, 5, 7)
chess(40, 5, 7)

turtle.done()
