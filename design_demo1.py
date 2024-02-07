import turtle
t = turtle.Turtle()

# t.bgcolor('black')
t.color('black')
t.pencolor('cyan')
for i in range(200):
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
t.done()