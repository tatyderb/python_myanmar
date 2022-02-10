import turtle

colors = [
    'blue',
    'green',
    'red',
    'gold'
]    

t = turtle.Turtle()
t.width(3)
t.speed(0)
a = []
y = 150
dy = -30

def write(text):
    t.write(text, font=('Arial', 14, 'normal'))

def length(s):
    start, finish, col = s
    return abs(start - finish)

def goto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def line(s, dy=0, only_finish=False):
    global y
    start, finish, col = s
    t.color(col)
    goto(start, y)
    if not only_finish:
        write(start)
    t.goto(finish, y)
    write(finish)
    y += dy
    goto(finish, y)

with open('data.txt') as fin:
    n = int(fin.readline())
    i = 0
    y = 150
    for text in fin:
        if text.strip() == '':
            continue
        start, finish = map(int, text.split())
        s = (start, finish, colors[i])
        a.append(s)
        line(s, dy)
        i += 1

a.sort(key=length, reverse=True)
for s in a:
    line(s, dy)

x = 0
i = 0
goto(x, y)
write(x)
while x < 400:
    x_end = x+length(a[i])
    line((x, x_end, a[i][2]), 0, True)
    x = x_end
    i += 1

y -= 50
x = 0
i = 0
goto(x, y)
write(x)
while x < n:
    x_end = x+length(a[i])
    line((x, x_end, a[i][2]), 0, True)
    x = x_end
    i += 1



turtle.done()
    
        
        
