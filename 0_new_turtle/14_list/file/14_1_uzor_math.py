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

def part(x0, y0, w, h, horizontal=True):
    """
    Рисует часть узора
    horizontal - горизонтальную часть True или вертикальную False
    w - размер части с -
    h - размер другой части
    x0, y0 - координаты начала рисования части узора
    """
    dw = w / 5

    bottom = [0] * 6
    top = [0] * 6
    

    if horizontal:
        for i in range(6):
            bottom[i] = (x0 + i*dw, y0)
            top[i]    = (x0 + i*dw, y0 + h)
    else:
        for i in range(6):
            bottom[i] = (x0,   y0 + i*dw)
            top[i]    = (x0+h, y0 + i*dw)
            
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

def uzor(x0, y0, w1, h1, nw, nh):

    # вершины прямоугольника, по ним будем рисовать диагонали
    # начинаем с нижнего левого угла
    sq_point = [
        (x0        , y0),           # левая нижняя
        (x0 + w1*nw, y0),           # правая нижняя
        (x0 + w1*nw, y0 + w1*nh),   # правая верхняя
        (x0        , y0 + w1*nh)    # левая верхняя
    ]    

    # низ
    x, y = sq_point[0]
    for i in range(nw):
        part(x+i*w1, y, w1, -h1, horizontal=True)

    # право
    x, y = sq_point[1]
    for i in range(nh):
        part(x, y+i*w1, w1, h1, horizontal=False)

    # лево
    x, y = sq_point[0]
    for i in range(nh):
        part(x, y+i*w1, w1, -h1, horizontal=False)

    # верх
    x, y = sq_point[-1]
    for i in range(nw):
        part(x+i*w1, y, w1, h1, horizontal=True)

    # диагонали
    line(sq_point[0], sq_point[2])
    line(sq_point[1], sq_point[3])

#part(0, 0, 75, 50)
uzor(-150, -100, 90, 50, 3, 2)
    
    
    
