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

  
'''Sierpiński arrowhead curve'''
def tri(size, sign):
  ang = 60*sign
  t.left(ang)
  t.fd(size)
  t.right(ang)
  t.fd(size)
  t.right(ang)
  t.fd(size)
  t.left(ang)
  
def a(size, n):
  if n == 0:
    t.left(60)
    tri(size,1)
    return 
  b(size/2, n-1)
  a(size/2, n-1)
  b(size/2, n-1)
  
def b(size, n):
  if n == 0:
    t.right(60)
    tri(size, -1)
    return
  a(size/2, n-1)
  b(size/2, n-1)
  a(size/2, n-1)

def curve(size, n):
  a(size, n)

                    # конец функции
                    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

# t.up()
# t.fd(-200)
# t.down()

t.color('blue')
curve(100, 0)



# for i in range(1):
  # t.up()
  # t.home()
  # t.down()
  # t.color(colors[i])
  # curve(100, i)
  
  # time.sleep(1)

turtle.done()    