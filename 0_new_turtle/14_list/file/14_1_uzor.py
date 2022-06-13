import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')
t.speed(0)

def line(p1, p2):
    t.pu()
    t.goto(p1)
    t.pd()
    t.goto(p2)

def part(w, h):
    dw = w / 5
    bottom = [0] * 6
    top = [0] * 6
    
    bottom[0] = t.pos()
    t.pu()
    for i in range(5):
        t.fd(dw)
        bottom[i+1] = t.pos()
    t.bk(w)
    t.lt(90)
    t.fd(h)
    t.rt(90)
    top[0] = t.pos()
    for i in range(5):
        t.fd(dw)
        top[i+1] = t.pos()

    print(top)
    print(bottom)

    # draw bottom and top lines
    for i in range(0, 6, 2):
        line(bottom[i], bottom[i+1])
        line(top[i], top[i+1])

    # draw / and \ lines
    for i in range(4):
        line(bottom[i], top[i+2])
        line(top[i], bottom[i+2])

def uzor(w1, h1, nw, nh):
    # вершины прямоугольника, по ним будем рисовать диагонали
    sq_point = [0] * 4

    # верх
    sq_point[0] = t.pos()
    for i in range(nw):
        part(w1, h1)
    t.rt(90)

    # право
    sq_point[1] = t.pos()
    for i in range(nh):
        part(w1, h1)
    t.rt(90)

    # низ
    sq_point[2] = t.pos()
    for i in range(nw):
        part(w1, h1)
    t.rt(90)

    # лево
    sq_point[3] = t.pos()
    for i in range(nh):
        part(w1, h1)
    t.rt(90)

    # диагонали
    line(sq_point[0], sq_point[2])
    line(sq_point[1], sq_point[3])

#part(75, 50)
t.pu()
t.goto(-150, 100)
uzor(90, 50, 3, 2)
    
    
    
