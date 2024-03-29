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
def row(size, n):
    global col
    for i in range(n):
        csq(size, col)
        col = nextColor(col)
        t.fd(size)

def spi(size, n):
    while n > 0:
        row(size, n)
        t.lt(90)
        t.fd(size)
        n = n - 1
        
col = 'red'
spi(30, 8)

turtle.done()
