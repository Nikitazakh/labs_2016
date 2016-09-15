import turtle

import numpy as np

turtle.shape('turtle')
turtle.left(90)
r = 5/(2*np.sin(2*np.pi/(2*72)))
turtle.penup()
turtle.goto(-r,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black", "yellow")
for j in range(72):
    turtle.forward(5)
    turtle.right(5)
turtle.end_fill()
turtle.penup()
turtle.goto(20,20)
turtle.pendown()
turtle.begin_fill()
turtle.color("black","blue")
for j in range(72):
    turtle.forward(1)
    turtle.right(5)
turtle.penup()
turtle.goto(-20,20)
turtle.pendown()
for j in range(72):
    turtle.forward(1)
    turtle.left(5)
turtle.end_fill()
turtle.width(5)
turtle.color("brown")
turtle.penup()
turtle.goto(0,20)
turtle.pendown()
turtle.backward(30)
turtle.penup()
r = 3/(2*np.sin(2*np.pi/(2*72)))
turtle.goto(r,-10)
turtle.pendown()
turtle.color("red")
turtle.left(180)
for j in range(36):
    turtle.forward(3)
    turtle.right(5)

input()

