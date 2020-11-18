import turtle

t = turtle.Turtle()
s=turtle.Screen()
s.bgcolor("white")
t.pencolor("white")

t.speed(0)

def square(n):
    for j in range(4):
        t.forward(n)
        t.right(90)

def pattern(n,color):
    turn=20
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(18):
        square(n)
        t.right(turn)
    t.end_fill()

def petal(n):
    colorise = ["yellow","red","orange","#00FF00"]
    t.forward(80)
    t.right(30)
    t.forward(80)
    pattern(25,colorise[n%4])
    t.pencolor("white")
    t.fillcolor()
    t.begin_fill()
    t.right(150)
    t.penup()
    t.forward(35)
    t.pendown()
    t.forward(45)
    t.right(30)
    t.forward(80)
    t.end_fill()
    t.left(180)

for i in range(12):
    petal(i)

pattern(15,"#9400D3")
pattern(10,"cyan")
pattern(5,"#0000FF")

t.hideturtle()
input()
    


