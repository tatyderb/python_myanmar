import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')

def veer(d, ang):
    size = 0
    total_ang = 0          # на сколько всего повернулись
    while total_ang <= 180:
        t.fd(size)
        t.fd(-size)
        t.lt(ang)
        total_ang += ang
        
        size = size + d
        # напечатаем на сколько всего повернулись
        print(total_ang)
        
veer(40, 30)

turtle.done()
