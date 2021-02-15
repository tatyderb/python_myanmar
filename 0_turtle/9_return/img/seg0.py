import turtle           

def write(data):
    t.write(data, font=("Arial", 14, "normal"))
    
def moveto(p):
    t.pu()
    t.goto(p)
    t.pd()

def dot(p):
    moveto(p)
    t.dot(10)
    write(p)
    
def line(x1, y1, x2, y2):
    moveto((x1, y1))
    write((x1,y1))
    t.goto(x2, y2)
    write((x2, y2))

def middle(x1, x2):
    line(x1, 0, x2, 0)
    xc = (x1 + x2)/2  # вычислили значение х координаты центра xc
    centr = (xc, 0)   # точка centr с координатами центра отрезка
    return centr      # ВЕРНЕМ ЗНАЧЕНИЕ центр


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
pc = middle(-100, 150)  # Нарисуем отрезок [-100, 150] и получим точку центра pc
                        # вычислять ее больше не нужно
                        # pc вычисляет функция middle
t.color('red')
dot(pc)                 # поставим точку на этот центр

turtle.done()