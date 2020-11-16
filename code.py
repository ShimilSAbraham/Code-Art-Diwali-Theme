import turtle

t = turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("white")

t.speed(0)

def square(n):
    for j in range(4):
        t.forward(n)
        t.right(90)

def pattern(n,color):
    turn=20
    t.pencolor(color)
    for i in range(18):
        square(n)
        t.right(turn)

def petal(n):
    colorise = ["yellow","red","orange","#00FF00"]
    t.forward(80)
    t.right(30)
    t.forward(80)
    pattern(30,colorise[n%4])
    t.pencolor("white")
    t.right(150)
    t.forward(80)
    t.right(30)
    t.forward(80)
    t.left(180)

for i in range(12):
    petal(i)

pattern(30,"cyan")
pattern(50,"#0000FF")
pattern(60,"#9400D3")

t.hideturtle()
input()
    


