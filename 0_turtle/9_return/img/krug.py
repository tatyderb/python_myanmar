import turtle
import math

t = turtle.Turtle()
t.width(5)

# перемещаемся в точку (x,y), ничего не рисуем.
def moveto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

# функция, которая вычисляет y по заданным x и r
# y*y + x*x = r*r     =>   y = sqrt(r*r - x*x)
def func(r, x):
    y = math.sqrt(r*r - x*x)
    return y
    
def krug(r):
    dx = r / 20          # будем рисовать 20 отрезков
    x = r                # начинаем с x = r и идем к х = 0
    moveto(x, 0)         # встаем в начало рисования     
    t.color('blue')
    while x >= 0:
        y = func(r, x)   # вычисляем y по х
        t.goto(x, y)     # рисуем следующий отрезок
        x -= dx          # вычисляем следующую координату х
        
r = int(input())
krug(r)
turtle.done()

    
   