import turtle

d = 30      # на сколько одна линия ниже другой

def write(text):
    t.write(text, font=('Arial', 18, 'normal'))

def one_line(size, col):
    """Рисуем 1 линию длины size и двигаемся рисовать следующую линию"""

    # запоминаем текущую позицию
    x = t.xcor()
    y = t.ycor()

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
prev = int(input())
one_line(prev, 'black')
# в цикле n-1 раз читаем число и рисуем отрезок
for i in range(n-1):
    cur = int(input())
    if cur > prev:
        one_line(cur, 'red')
    else:
        one_line(cur, 'blue')
    prev = cur

turtle.done()
