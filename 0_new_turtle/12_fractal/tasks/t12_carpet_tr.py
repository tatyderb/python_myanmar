import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def tri(size):
    a = size/2
    t.left(60)
    t.fd(a)
    t.right(60)
    t.down()
    # t.stamp()
    
    t.begin_fill()
    for n in range(3):
      t.fd(a)
      t.right(120)
    t.end_fill()
    
    t.up()
    t.left(60)
    t.fd(-a)
    t.right(60)
    
def tri4(size, n):
  if n == 0:
    return 
  a = size/2
  
  tri(size)           # central tri
  # t.stamp()
  # t.color('green')
  
  # t.stamp()
  tri4(a, n-1)        # down left tri
  # t.stamp()
  
  # t.color('orange')
  
  t.left(60)
  t.fd(a)           # goto up tri
  t.right(60)
  # t.stamp()
  tri4(a, n-1)      # up tri
  # t.stamp()

  
  # t.color('black')  # goto down right tri
  t.left(60)
  t.fd(-a)
  t.right(60)
  t.fd(a)
  # t.stamp()
  tri4(a, n-1)      # right down tri
  # t.stamp()
  
  t.bk(a)          # back to initial point
  # t.stamp()

def carpet(size, n, col1, col2):
  x = t.xcor()
  y = t.ycor()
  t.color(col1)
  t.begin_fill()
  for i in range(3):
    t.fd(size)
    t.left(120)
  t.end_fill()
  t.color(col2)
  t.up()
  tri4(size, n)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
carpet(270, 3, 'blue', 'white')
t.hideturtle()
turtle.done()