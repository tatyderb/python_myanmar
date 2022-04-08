import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(5)

def write(text):
    t.write(text, font=('Arial', 18, 'normal'))

def sq(size):
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

# функция принимает размер стороны квадрата
# возвращает площадь квадрата
def sqarea(size):
    res = size * size
    return res

t.color('red', 'yellow')

size = int(input())     # прочитали размер квадрата с консоли
sq(size)                # нарисовали квадрат

a = sqarea(size)        # вычислили площадь квадрата
write(a)                # написали площадь на поле с черепахой
print(a)                # напечатали площадь в консоли

t.ht()

turtle.done()



