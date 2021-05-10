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

# нарисовать n квадратов, 
# первый размера size, 
# каждый следующий на d меньше
# уже нарисовали i квадратов
def sqn(size, d, n, i):
  if n == 0:          # если не надо больше рисовать квадратов        
    return 
  if size <= 0:        # если следующий квадрат маленький, больше не рисовать
    return

  sqn(size-d, d, n-1, i+1) # рисовать следующий квадрат
    
  sq(size, colors[i])   # colors[i] - взять цвет номер i из colors
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(100, 20, 7, 0)    # 7 квадратов, первый размером 200, другие на 20 меньше

turtle.done()    