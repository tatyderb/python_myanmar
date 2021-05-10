import turtle           
import time
import math

def sq(size):
  for i in range(4):
    t.fd(size)
    t.left(90)

def tri(size, a):
  t.fd(size)
  t.left(135) # 135
  t.fd(a)
  t.left(90)  # 90
  t.fd(a)
    
# sq -> left tri    
def toltri(size):
  t.left(90)  # 90
  t.fd(size)
  t.right(90-ang11) # 45
  
# left tri -> right tri 
def tortri(size):
  t.fd(size)
  t.right(180-angt) # 90

# right tri -> sq  
def tosq(size, a):
  t.left(180-angt)  # 90
  t.bk(a)
  t.left(90-ang11)  # 45  
  t.bk(size)
  t.right(90) # 90

def rad(grad):
  return math.pi*grad/180
    
def katet(size):
  a = size*sina/sint  
  b = size*sinb/sint  
  return a, b
  
def sqpi(size, n):
  if n == 0:
    t.color('green')
    sq(size)
    t.color('brown')
    # t.fd(size)
    # t.bk(size)
    return
  
  a1, a2 = katet(size)
  sq(size)
  toltri(size)
  # time.sleep(1)
  # t.color('red')
  sqpi(a1, n-1)
  # time.sleep(1)
  # t.color('green')
  tortri(a1)
  # time.sleep(1)
  # t.color('gold')
  sqpi(a2, n-1)
  tosq(size, a1)
  
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

t.up()
t.goto(0, -200)
t.down()

t.color('brown')
# последнее дерево содержит решения всех других деревьев.
# при этих константах получаем варианты 1, 2, 3
rect45 = {'ang11': 45, 'ang12':45, 'angt': 90}
rect30s = {'ang11': 30, 'ang12':30, 'angt': 120}
rect30r = {'ang11': 30, 'ang12':60, 'angt': 90}
# rect = rect45
# rect = rect30s
rect = rect30r
ang11 = rect['ang11']
ang12 = rect['ang12']
angt = rect['angt']
sina = math.sin(rad(ang12))
sinb = math.sin(rad(ang11))
sint = math.sin(rad(angt))
sqpi(100, 7)

turtle.done()    
