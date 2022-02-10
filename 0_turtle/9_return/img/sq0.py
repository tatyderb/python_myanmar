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

                      # вычислим координаты середины
    xc = size/2
    yc = size/2
    centr = (xc, yc)  # запомним точку центра
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