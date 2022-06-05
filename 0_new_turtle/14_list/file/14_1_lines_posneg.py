import turtle

d = 30      # на сколько одна линия ниже другой

def write(text):
    t.write(text, font=('Arial', 18, 'normal'))

def one_line(size):
    """Рисуем 1 линию длины size и двигаемся рисовать следующую линию"""

    # запоминаем текущую позицию
    x = t.xcor()
    y = t.ycor()

    if size > 0:
        col = 'red'
    else:
        col = 'blue'
    t.color(col)

    # пишем и печатаем
    write(size)
    print(f'draw line size={size} from {x},{y}')  # не работает в repl.it
    # print(size, x, y)                           # для repl.it

    # рисуем линию
    t.fd(size)

    # идем рисовать следующую линию
    t.pu()
    t.goto(x, y - d)
    t.pd()

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

# читаем 1 число n
n = int(input())
# в цикле n раз читаем число и рисуем отрезок
for i in range(n):
    size = int(input())
    one_line(size)

turtle.done()
