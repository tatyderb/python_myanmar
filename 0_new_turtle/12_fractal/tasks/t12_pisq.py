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

def sq(size):
  for i in range(4):
    t.fd(size)
    t.left(90)

def tri(size, a):
  t.fd(size)
  t.left(135)
  t.fd(a)
  t.left(90)
  t.fd(a)
    
# sq -> left tri    
def toltri(size):
  t.left(90)
  t.fd(size)
  t.right(45)
  
# left tri -> right tri 
def tortri(size):
  t.fd(size)
  t.right(90)

# right tri -> sq  
def tosq(size, a):
  t.left(90)
  t.bk(a)
  t.left(45)
  t.bk(size)
  t.right(90)
  
def sqpi(size, n):
  if n == 0:
    t.color('green')
    sq(size)
    t.color('brown')
    # t.fd(size)
    # t.bk(size)
    return
  
  a = size/math.sqrt(2)
  sq(size)
  toltri(size)
  # time.sleep(1)
  # t.color('red')
  sqpi(a, n-1)
  # time.sleep(1)
  # t.color('green')
  tortri(a)
  # time.sleep(1)
  # t.color('gold')
  sqpi(a, n-1)
  tosq(size, a)
  
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.up()
t.goto(0, -200)
t.down()

t.color('brown')
sqpi(100, 7)
# for i in range(1):
  # t.up()
  # t.home()
  # t.down()
  # t.color(colors[i])
  # curve(100, i)
  
  # time.sleep(1)

turtle.done()    