import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

t = turtle.Turtle()


write(t.pos())    # (0,0)


t.setpos(100, -50)
write(t.pos())    # (100,-50)


t.goto(100, 50)
write(t.pos())    # (100, 50)

turtle.done()
