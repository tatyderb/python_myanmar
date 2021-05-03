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

# меняет желтый цвет на красный, а любой другой цвет на желтый
def next_col(col):
    if col == 'yellow':
        return 'red'
    else:
        return 'yellow'

# n квадратов со стороной size; цвет первого квадрата col
def csq_row(size, n, col):
    for i in range(n):
        csq(size, col)
        t.fd(size)
        col = next_col(col)

csq_row(40, 7, 'red')

turtle.done()
