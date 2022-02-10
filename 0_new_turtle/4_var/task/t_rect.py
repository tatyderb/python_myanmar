import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def trifill(p1, p2, p3, col):
        t.color(col)
        t.begin_fill()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)
        t.end_fill()

def rect(w, h):
        # сохранить точку центра прямоугольника
        p0 = t.pos()

        # перейти в его вершину
        t.pu()
        t.fd(w/2)
        t.lt(90)
        t.fd(h/2)
        t.lt(90)
        t.pd()

        # обойти все вершины и сохранить их в переменные
        p1 = t.pos()
        t.fd(w)
        t.lt(90)
        p2 = t.pos()
        t.fd(h)
        t.lt(90)
        p3 = t.pos()
        t.fd(w)
        t.lt(90)
        p4 = t.pos()

        # вернуться в центр
        t.goto(p0)

        # нарисовать треугольники
        trifill(p0, p1, p2, 'green')
        trifill(p0, p2, p3, 'yellow')
        trifill(p0, p3, p4, 'blue')
        trifill(p0, p4, p1, 'red')

rect(200, 150)

turtle.done()
