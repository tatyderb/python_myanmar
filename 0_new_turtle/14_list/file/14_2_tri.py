import turtle

def tri(points):
    # черепаха идет на первую точку
    t.pu()
    t.goto(points[0])
    t.pd()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

tpoints = [(100, 0), (0, 50), (100, 100)]
tri(tpoints)

turtle.done()
