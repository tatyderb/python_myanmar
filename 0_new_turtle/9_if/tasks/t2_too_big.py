import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def write(text):
    t.write(text, font=('Arial', 14, 'normal'))

def sq(size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def sqcheck(size):
    t.color('blue')
    if 0 < size < 200:              # хороший размер
        t.color('blue')
        sq(size)
    else:                           # иначе плохой
        t.color('red')
        write('Плохой размер')     
        

# sqcheck(150)
# sqcheck(300)
sqcheck(-150)

t.ht()
    
turtle.done()
