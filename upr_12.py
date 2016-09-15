import turtle

turtle.shape('turtle')
turtle.left(90)
for n in range(3):
    for j in range(36):
        turtle.forward(5)
        turtle.right(5)
    for i in range(36):
        turtle.forward(1)
        turtle.right(5)