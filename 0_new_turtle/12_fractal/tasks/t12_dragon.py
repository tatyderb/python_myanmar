# -*- coding: utf-8 -*-
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
  
'''Dragon fractal curve'''
def curve(size, n, sign):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    
    return
  a = size/math.sqrt(2)   # иначе разбиваем отрезок
                          # и вместо него делаем набор отрезков
  t.left(45*sign)
  curve(a, n-1, sign)
  t.right(90*sign)
  curve(a, n-1, -sign) 
  t.left(45*sign)

                    # конец функции
                    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.up()
t.fd(-200)
t.down()

# t.color('blue')
# curve(200, 2, 1)



for i in range(4):
  p0 = t.pos()
  t.color(colors[i])
  curve(200, i, 1)
  
  t.up()
  t.goto(p0)
  t.down()
  t.seth(0)
  time.sleep(1)

turtle.done()    