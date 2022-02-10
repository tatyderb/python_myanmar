import turtle           

def write(data):
    t.write(data, font=("*Sans", 14, "normal"))
    
def coord():
    write(t.pos())

def moveto(x, y):
    t.pu()
    t.goto((x, y))
    t.pd()

    write((x, y))
    t.dot(10)

def line(x1, y1, x2, y2):
    t.pu()
    t.goto((x1, y1))
    t.pd()

    write((x1, y1))
    t.goto((x2, y2))
    write((x2, y2))

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x0, y0 = map(int, input().split())

t.color('blue')
line(x1, y1, x2, y2)

t.color('red')
moveto(x0, y0)

turtle.done()