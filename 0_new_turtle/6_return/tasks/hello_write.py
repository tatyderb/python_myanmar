import turtle

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')

t.write('Hello', font=('Arial', 18, 'normal'))  # поле черепахи
print('start')                                  # console
print('stop')                                   # console

t.fd(150)
t.rt(90)
t.color('red')
t.write('End', font=('Arial', 18, 'normal'))    # поле черепахи
