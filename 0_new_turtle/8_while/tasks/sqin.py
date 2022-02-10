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
        
def sqin(size):
    while size > 50:
        sq(size)
        t.fd(size/2)
        t.lt(45)
        
        size = size / math.sqrt(2)
        # напечатаем новую длину строны
        print(size)
        
# sqin(200)
# sqin(30)
sqin(240)

turtle.done()
