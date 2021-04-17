import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

def sq(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)
        
def squp(sizemin, d, sizemax):
    t.color('blue')
    size = sizemin
    while size <= sizemax:
        sq(size)
        size = size + d
        # напечатаем новую длину строны
        print(size)

      
squp(50, 25, 200)
# squp(0, 70, 200)

turtle.done()
