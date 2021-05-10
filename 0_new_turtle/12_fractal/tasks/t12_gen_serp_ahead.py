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
The Sierpinski triangle drawn using an L-system.

variables : A B
constants : + −
start  : A
rules  : (A → B-A-B), (B → A+B+A)
angle  : 60°
Here, A and B both mean "draw forward", + means "turn left by angle", and − means "turn right by angle".
'''
def gen(size, n):
  A(size, n-1)
  
def minus():
  t.left(60)
  
def plus():
  t.right(60)
  
def A(size, n):
  if n == 0:
    t.fd(size)
    return 
  B(size, n-1)  # A → B-A-B
  minus()
  A(size, n-1)
  minus()
  B(size, n-1)

def B(size, n):
  if n == 0:
    t.fd(size)
    return 
  A(size, n-1)  # B → A+B+A
  plus()
  B(size, n-1)
  plus()
  A(size, n-1)
  
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
t.color('blue')
gen(10, 6)

t.hideturtle()
turtle.done()