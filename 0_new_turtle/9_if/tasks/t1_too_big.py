import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def write(text):
    t.write(text, font=('Arial', 14, 'normal'))

def sq(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def sqcheck(size):
    t.color('blue')
    if size > 200:                  # если размер больше 200
        t.color('red')
        write('Очень большой')      # то написать Очень большой
    else:
        t.color('blue')

        for i in range(4):  # рисуем всегда
            t.fd(size)
            t.lt(90)

sqcheck(300)
# sqcheck(150)

t.ht()
    
turtle.done()
