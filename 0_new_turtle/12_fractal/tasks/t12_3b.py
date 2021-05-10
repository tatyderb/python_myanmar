import turtle           
import time

colors = [
  'yellow',   # colors[0]
  'gold',     # colors[1]
  'orange',   # colors[2]
  'red',      # colors[3]
  'violet',   # colors[4]
  'blue',     # colors[5]
  'green'     # colors[6]
  ]

def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
    
  a = size/4        # иначе разбиваем отрезок 
                    # и вместо него делаем набор отрезков  
  koch_line(a, n-1) # left
  t.left(90)
  koch_line(a, n-1) # up
  t.right(90)
  koch_line(a, n-1) # left
  t.right(90)
  koch_line(a, n-1) #down
  koch_line(a, n-1) #down
  t.left(90)
  koch_line(a, n-1) # left
  t.left(90)
  koch_line(a, n-1) # up 
  t.right(90)
  koch_line(a, n-1) # left
                    # конец функции
                    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

# koch_line(320, 2)

t.up()
t.fd(-300)
t.down()

for i in range(0, 4):
  p0 = t.pos()
  t.color(colors[i])
  koch_line(640, i)
  
  t.up()
  t.goto(p0)
  t.down()
  time.sleep(1)

turtle.done()    