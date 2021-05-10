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

variables : F G
constants : + −
start  : F−G−G
rules  : (F → F−G+F+G−F), (G → GG)
angle  : 120°
Here, F and G both mean "draw forward", + means "turn left by angle", and − means "turn right by angle".
'''
def gen(size, n):
  F(size, n-1)
  minus()
  G(size, n-1)
  minus()
  G(size, n-1)
  
def minus():
  t.left(120)
  
def plus():
  t.right(120)
  
def F(size, n):
  if n == 0:
    t.fd(size)
    return 
  F(size, n-1)  # F → F−G+F+G−F
  minus()
  G(size, n-1)
  plus()
  F(size, n-1)
  plus()
  G(size, n-1)
  minus()
  F(size, n-1)

def G(size, n):
  if n == 0:
    t.fd(size)
    return 
  G(size, n-1)  # G -> GG
  G(size, n-1)
  
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
gen(20, 4)

t.hideturtle()
turtle.done()