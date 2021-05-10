# -*- coding: utf-8 -*-
import turtle           
import time

def tree(size, d, ang, n):
  if n == 0:
    return
  
  t.fd(size)
  t.left(ang)
  tree(size-d, d, ang, n-1)
  t.left(-2*ang)
  tree(size-d, d, ang,  n-1)
  t.left(ang)
  t.fd(-size)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.seth(90)
t.up()
t.bk(200)
t.down()
t.color('brown')

tree(100, 20, 30, 1)

turtle.done()    