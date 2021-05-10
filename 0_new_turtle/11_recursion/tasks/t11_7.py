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

def sq(size, i):
  t.fillcolor(colors[i])
  t.begin_fill()
  for i in range(5):
    t.fd(size)
    t.left(90)
  t.fd(size)
  t.end_fill()

def fib0(size, n):
    if n <= 2:
      k = n
    else:
      k = 2
    for i in range(k):
      sq(size, i)
    fib(1,1,size, 2,n-2)
    
def fib(f0, f1, size, i, n):
  print(f'fib(f0={f0}, f1={f1}, i={i}, n={n})') 
  if i > n:                    
    return 
  sq((f0+f1)*size, i)
  fib(f1, f0+f1, size, i+1, n)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

fib0(20, 8)
# t.hideturtle()

turtle.done()    
