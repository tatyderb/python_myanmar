import turtle

t = turtle.Turtle()
t.width(5)

def sq(size, col):
    if col == 'black':  # если цвет РАВЕН белый
        col = 'blue'    #      то цвет ПРИСВОИТЬ синий
        
    t.color(col)        # рисуем цветом col
    for i in range(4):
        t.fd(size)
        t.lt(90)
        
sq(150, 'yellow')
sq(100, 'white')

turtle.done()
