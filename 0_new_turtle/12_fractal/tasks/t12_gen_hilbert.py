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
'''
Алфавит : A, B
Константы : F + -
Аксиома : A
Правила:
A -> - B F + A F A + F B -
B -> + A F - B F B - F A +
Здесь F означает «движение вперёд», 
«-» означает поворот влево на 90°, 
«+» означает поворот вправо на 90° (см. turtle graphics), 
а A и B игнорируются при рисовании.
'''
def gen(size, n):
  # s = size / (2**n//2) / math.sqrt(2)**(n%2)
  s = 10
  A(size, n-1)
  
def minus():
  t.left(90)
  
def plus():
  t.right(90)
  
def F(size):
  t.fd(size)
  
def A(size, n):
  if n==0:
    return
                  # A -> - B F + A F A + F B -
  minus()                   
  B(size, n-1)
  F(size)
  plus()
  A(size, n-1)
  F(size)
  A(size, n-1)
  plus()
  F(size)
  B(size, n-1)
  minus()
    
def B(size, n):
  if n==0:
    return
                 # B -> + A F - B F B - F A +
  plus()
  A(size, n-1)
  F(size)
  minus()
  B(size, n-1)
  F(size)
  B(size, n-1)
  minus()
  F(size)
  A(size, n-1)
  plus()
  
def draw_curve(size, n, i):
  t.color(colors[i])
  gen(size, 2+i)
  t.up()
  t.home()
  t.down()
    

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
# t.color('blue')
# gen(10, 10)

size = 300
for i in range(4):
  t.clear()
  draw_curve(size, 2+i, i)
  size /= 3
  # draw_curve(size, 2+i+1, i+1)
  time.sleep(1)

t.hideturtle()
turtle.done()