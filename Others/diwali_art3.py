import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
color="yellow"
t.pencolor(color)
t.shape("turtle")
t.speed(0)

def pattern(n):
    for j in range(12):
        t.forward(n)
        t.right(30)
        t.forward(n)
        t.right(150)
        t.forward(n)
        t.right(30)
        t.forward(n)
        t.right(180)

for j in range(12):
    t.forward(100)
    t.right(30)
    t.forward(100)
    pattern(25)
    t.right(150)
    t.forward(100)
    t.right(30)
    t.forward(100)
    t.right(180)

t.setposition(0,0)
t.pencolor("orange")
pattern(60)
t.pencolor("red")
pattern(40)
t.hideturtle()

turtle.done()
