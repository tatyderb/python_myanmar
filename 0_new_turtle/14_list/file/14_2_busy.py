import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(2)

def rect(width, height, col):
    t.color('yellow', col)
    t.begin_fill()
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

def uzor(n, colors, width, heights):
    k = len(colors)
    for i in range(n):
        print(i, i%k)
        print(width, heights[i%k], colors[i%k])
        rect(width, heights[i%k], colors[i%k])
        t.fd(width)

n = int(input())
colors = input().split()
heights = [int(x) for x in input().split()]

uzor(n, colors, 30, heights)

turtle.done()
