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
  
def sq(size, n, col):          # нарисовать многоугольник размера size цвета col
  t.color(col)
  ang = 180 - 180*(n-2)/n
  for i in range(n):
    t.fd(size)
    t.left(ang)
    
def rad(ang):
  return ang*pi/180
  
def goto_next(size, n):
  ang = 180*(n-2)/n
  print ('ang=', ang)
  b = (180-ang)/2
  print('b=', b)
  t.fd(size/2)
  t.left(b)
  # time.sleep(3)
  a = size * sin(rad(ang))/(2*sin(rad(b)) )
  return a
  
# k-угольники, 
# n штук надо нарисовать
# первый размера size, 
# уже нарисовали i многоугольников
def sqn(size, k, n, i):
  if n == 0:                # если не надо больше рисовать        
    return 
  if size <= 20:            # если следующий многоугольник маленький, больше не рисовать
    return

  sq(size, k, colors[i])        # рисовать 1 многоугольник
  size = goto_next(size, k)  
  sqn(size, k, n-1, i+1)        # рисовать следующий многоугольник
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 5, 5, 0)    # 7 квадратов, первый размером 200, другие на 20 меньше
t.hideturtle()

turtle.done()    
