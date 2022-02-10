import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))
    
def moveto(p):
    t.pu()
    t.goto(p)
    t.pd()

    write(p)
    t.dot(10)

def sq(size, col):
    t.color(col)
                      # нарисуем квадрат
    for i in range(4):
        t.fd(size)
        t.left(90)

    p0 = t.pos()      # запомним, где стояли
    t.pu()
                      # пойдем в середину квадрата
    t.fd(size/2)
    t.lt(90)
    t.fd(size/2)
    t.rt(90)
    
    centr = t.pos()   # ЗАПОМНИМ точку центра
    t.goto(p0)        # вернемся в начальную точку
    return centr      # ВЕРНЕМ ЗНАЧЕНИЕ центр


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
pc = sq(100, "blue")    # Нарисуем квадрат и получим точку центра pc
                        # вычислять ее больше не нужно
                        # pc вычисляет функция sq
t.color('red')
moveto(pc)              # поставим черепаху на этот центр
write(pc)

turtle.done()