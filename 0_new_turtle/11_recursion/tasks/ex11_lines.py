# -*- coding: utf-8 -*-
import turtle           
import time

colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
  ]

def line(size, col):  # нарисовать линию длины size цвета col
  t.color(col)
  t.fd(size)
  
def goto(x, y):
    t.pu()
    t.setpos((x, y))
    t.pd()

def lines(size, dy, n):
    x = t.xcor()
    y = t.ycor()
    k = len(colors)
    for i in range(n):    # i меняется от 0 до n-1
        line(size, colors[i%k])   # colors[i] - взять цвет номер i из colors
        y -= dy
        goto(x, y)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

#colors[9]
colors = ['red', 'yellow', 'green']
lines(100, 20, 6)

turtle.done()    
