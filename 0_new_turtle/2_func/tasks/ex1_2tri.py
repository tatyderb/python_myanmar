import turtle

t = turtle.Turtle()
t.pensize(4)
t.pencolor('red')

t.fd(100)   # рисуем 1 треугольник
t.lt(120)

t.fd(100)
t.lt(120)

t.fd(100)
t.lt(120)

t.lt(45)    # повернулись
t.pencolor('green')

t.fd(100)   # рисуем 2 треугольник
t.lt(120)

t.fd(100)
t.lt(120)

t.fd(100)
t.lt(120)

turtle.done()

