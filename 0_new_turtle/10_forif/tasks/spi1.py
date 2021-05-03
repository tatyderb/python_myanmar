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

def nextColor(col):
    if col == 'yellow':
        return 'red'
    else:
        return 'yellow'

# n квадратов со стороной size
def row(size, n, col):
    for i in range(n):
        csq(size, col)
        col = nextColor(col)    # цвет следующего квадрата
        t.fd(size)
    return col                  # вернули цвет следующего квадрата

def spi(size, n):
    col = 'red'
    while n > 0:
        col = row(size, n, col) # вернули цвет следующего квадрата
        t.lt(90)
        t.fd(size)
        n = n - 1
        

spi(30, 8)

turtle.done()
