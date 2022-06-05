import turtle

def sq(size):
    points = [0, 0, 0, 0]
    # черепаха идет на первую точку
    for i in range(4):          # i меняется 0, 1, 2, 3
        points[i] = t.pos()     # запоминаем позицию черепахи
        t.fd(size)              # идем к следующей вершине квадрата
        t.lt(90)
    # тут закончился цикл
    # после цикла возвращаем список точек вершин квадрата
    return points


t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

points = sq(100)
print(points)   # [(0.00,0.00), (100.00,0.00), (100.00,100.00), (0.00,100.00)]

turtle.done()
