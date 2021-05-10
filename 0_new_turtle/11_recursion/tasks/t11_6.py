import turtle           

def branch(n, size0, dsize, ang0, dang):
  size = size0
  ang = ang0
  for i in range(n):
    if i == n/2:
      p = t.pos()
    t.fd(size)
    t.left(ang)
    size -= dsize
    ang += dang
  return p
  
def uzor(n, size0, dsize, ang0, dang, k):
  if k == 0:                    
    return 

  p = branch(n, size0, dsize, ang0, dang)
  t.up()
  t.goto(p)
  t.down()
  t.seth(0)
  uzor(n, size0, dsize, -ang0, -dang, k-1)
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
t.color('blue')
t.up()
t.setx(-300)
t.down()
uzor(6, 50, 5, 20, 10, 3)
# t.hideturtle()

turtle.done()    