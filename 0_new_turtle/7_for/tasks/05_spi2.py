import turtle

def spiral2(n, start_size, delta):
    t.color('blue')
    size = start_size
    d = delta
    for i in range(n):
        t.fd(size)
        t.lt(90)
        size = size + d    # size += d

    t.rt(90)
    size = size - d

    t.color('red')
    for i in range(n):
        t.fd(size)
        t.lt(90)
        size = size - d    # size -= d


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)

t.seth(-90)
spiral2(16, 20, 10)

turtle.done()
