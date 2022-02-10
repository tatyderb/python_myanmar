import turtle


def sq(size):
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

def  sq2(size1, size2):
    if size1 < size2:
        sizemin = size1
        sizemax = size2
    else:
        sizemin = size2
        sizemax = size1
    t.color('gold', 'yellow')
    sq(sizemax)
    t.color('gold', 'red')
    sq(sizemin)
    
t = turtle.Turtle()
t.width(3)

# sq2(50, 100)
# sq2(100, 100)
sq2(170, 40)


turtle.done()
