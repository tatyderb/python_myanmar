import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red', 'blue')

t.write('Start', font=('Arial', 18, 'normal'))

t.fd(100)

p = t.pos()
t.write(p, font=('Arial', 18, 'normal'))

turtle.done()
