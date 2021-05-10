import turtle           
import time
import math

colors = [
  'yellow',   # colors[0]
  'gold',     # colors[1]
  'orange',   # colors[2]
  'red',      # colors[3]
  'violet',   # colors[4]
  'blue',     # colors[5]
  'green'     # colors[6]
  ]

def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
  a = size/math.sqrt(2)   # иначе разбиваем отрезок
                          # и вместо него делаем набор отрезков
  t.left(45)                            
  koch_line(a, n-1) # left
  t.right(90)
  koch_line(a, n-1) # up
  t.left(45)

                    # конец функции
                    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

# koch_line(320, 2)

t.up()
t.fd(-200)
t.down()

t.color('blue')
koch_line(320, 7)

turtle.done()    