import turtle           
from math import tan, sin, pi

colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
]

def sq(size, col):          # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

def shift(size, ang):
  angrad = ang*pi/180
  tga = tan(angrad)
  return size * tga / (1+tga)
  
def new_size(a, ang):
  angrad = ang*pi/180
  return a/sin(angrad)
  
def goto_next(size, ang):
  a = shift(size, ang)
  x = new_size(a, ang)
  t.fd(a)
  t.left(ang)
  return x
  
# нарисовать n квадратов, 
# первый размера size, 
# каждый следующий на d меньше
# уже нарисовали i квадратов
def sqn(size, ang, n, i):
  if n == 0:                # если не надо больше рисовать квадратов        
    return 
  if size <= 0:             # если следующий квадрат маленький, больше не рисовать
    return

  sq(size, colors[i])         # рисовать 1 квадрат
  size = goto_next(size, ang)  
  sqn(size, ang, n-1, i+1)  # рисовать следующий квадрат
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 30, 7, 0)    # 7 квадратов, первый размером 200, другие на 20 меньше

turtle.done()    