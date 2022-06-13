import turtle

def tri(col, points):
    """Рисует треугольник цветом col по его вершинам из списка points"""
    t.color(col)
    # печатаем, чтобы видеть по каким координатам рисуем
    print(col, points)
    # черепаха идет на первую точку
    t.pu()
    t.goto(points[-1])
    t.pd()
    t.begin_fill()
    for i in range(3):
        t.goto(points[i])
    t.end_fill()

def make_sqpoints(width, height):
    """Возвращает список вершин прямоугольника и его центр"""
    # Запоминаем 4 вершины прямоугольника в список sqpoints
    sqpoints = [0] * 4
    sqpoints[0] = t.pos()
    t.fd(width)
    t.lt(90)
    sqpoints[1] = t.pos()
    t.fd(height)
    t.lt(90)
    sqpoints[2] = t.pos()
    t.fd(width)
    t.lt(90)
    sqpoints[3] = t.pos()
    t.fd(height)
    t.lt(90)
    # центр прямоугольника
    center = (width/2, height/2)
    print(sqpoints, center)
    # вернем список вершин и отдельно точку центра
    return sqpoints, center

def flag(width, height):
    """Рисует флаг шириной width и высотой height из текущей точки"""
    # получаем список вершин и центр
    sqpoints, center = makesqpoints(width, height)
    # в цикле берем цвет, центр, точку прямоугольника и его следующую точку
    colors = ['blue', 'red', 'green', 'yellow']
    for i in range(4):
        tripoints = [center, sqpoints[i], sqpoints[(i+1)%4]]
        tri(colors[i], tripoints)

t = turtle.Turtle()
t.shape('turtle')
t.width(2)

width = 200
height = 150
flag(width, height)

turtle.done()
