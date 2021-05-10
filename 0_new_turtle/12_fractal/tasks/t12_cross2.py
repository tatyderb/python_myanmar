import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def sq(x0, y0, size):
    t.up()
    t.goto(x0, y0)
    t.down()
    t.begin_fill()
    for n in range(4):
      t.fd(size)
      t.left(90)
    t.end_fill()
    
def sq8(x0, y0, size, n):
  if n == 0:
    sq(x0, y0, size)
    return 
  a = size/3
  for xi in range(3):
    for yi in range(3):
      if (yi + xi)%2 == 0:
        sq8(x0+a*xi, y0+a*yi, a, n-1)

def carpet(size, n, col1, col2):
  x = t.xcor()
  y = t.ycor()
  t.color(col1)
  sq(x, y, size)
  t.color(col2)
  sq8(x, y, size, n)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
carpet(270, 3, 'white', 'blue')
t.hideturtle()
turtle.done()