import turtle           

colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
  ]

def sq(size, col):  # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

# n квадратов, первый размера size, каждый следующий на d меньше
def sqn(size, d, n):    
  for i in range(n):    # i меняется от 0 до n-1
    sq(size, colors[i]) # colors[i] - взять цвет номер i из colors
    size -= d
    if size < 0:        # если следующий квадрат маленький, больше не рисовать
      return
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

# sqn(200, 20, 7)   # 7 квадратов, первый размером 200, другие на 20 меньше
sqn(100, 20, 7)   # 5 квадратов, первый размером 100, другие на 20 меньше

turtle.done()    
