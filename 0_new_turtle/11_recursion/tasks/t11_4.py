import turtle           
import time
from math import tan, sin, pi

colors = [
  'red',   # colors[0]
  'gold',  # colors[1]
  'blue'   # colors[2]
  ]
  
def sq(size, col):          # нарисовать отрезок размера size цвета col
  t.color(col)
  t.fd(size)
  t.left(90)
  
# нарисовать n отрезков, 
# первый размера size, 
# каждый следующий на d меньше
# уже нарисовали i отрезков
def sqn(size, d, n, i):
  if n == 0:                # если не надо больше рисовать отрезков        
    return 
  if size <= 0:             # если следующий отрезок маленький, больше не рисовать
    return

  k = len(colors)
  sq(size, colors[i % k])   # рисовать 1 отрезок
  sqn(size-d, d, n-1, i+1)  # рисовать следующие отрезки
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 10, 15, 0)    # спираль 15 отрезков, первый 200, следующие на 10 меньше.
t.hideturtle()

turtle.done()    