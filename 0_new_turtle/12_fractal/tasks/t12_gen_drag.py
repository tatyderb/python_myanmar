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

def gen(size, n):
  # s = size / (2**n//2) / math.sqrt(2)**(n%2)
  s = 10
  t.fd(size)
  x(size, n-1)
  
def x(size, n):
  if n==0:
    return
                  # x ->  X+YF+
  x(size, n-1)
  t.right(90)
  y(size, n-1)
  t.fd(size)
  t.right(90)
    
def y(size, n):
  if n==0:
    return
                # y -> Y > -FX-Y
  t.left(90)
  t.fd(size)
  x(size, n-1)
  t.left(90)
  y(size, n-1)
  
def draw_curve(size, n, i):
  t.color(colors[i])
  t.seth(45*i)
  gen(size, 2+i)
  t.up()
  t.home()
  t.down()
    

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
t.color('blue')
gen(10, 10)

# size = 100
# for i in range(6):
  # t.clear()
  # draw_curve(size, 2+i, i)
  # size /= math.sqrt(2)
  # draw_curve(size, 2+i+1, i+1)
  # time.sleep(1)

t.hideturtle()
turtle.done()