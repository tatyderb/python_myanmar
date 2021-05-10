# -*- coding: utf-8 -*-
import turtle           
import time

hues = [
  'violet',   # hues[0]
  'blue',     # hues[1]
  'green',    # hues[2]
  'yellow',   # hues[3]
  'gold',     # hues[4]
  'orange',   # hues[5]
  'red'       # hues[6]
  ]

def sq(size, col):          # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

# нарисовать n квадратов, 
# первый размера size, 
# каждый следующий на d меньше
# уже нарисовали i квадратов
def sqn(size, d, n, i):
  if n == 0:                # если не надо больше рисовать квадратов        
    return 
  if size <= 0:             # если следующий квадрат маленький, больше не рисовать
    return

  sqn(size-d, d, n-1, i+1)  # рисовать следующий квадрат
  sq(size, hues[i])         # рисовать 1 квадрат 
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 20, 7, 0)    # 7 квадратов, первый размером 200, другие на 20 меньше

turtle.done()    