import turtle

t = turtle.Turtle()
t.pensize(4)

t.pencolor('red')
triangle()      # вызов функции triange
t.lt(45)
t.pencolor('green')
triangle()      # вызов функции triange
t.lt(45)
t.pencolor('blue')
triangle()      # вызов функции triange

# определение новой функции triangle
def triangle():
    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)

    t.fd(100)
    t.lt(120)
# здесь функция triangle закончилась

turtle.done()

