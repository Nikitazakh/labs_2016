import turtle

turtle.shape('turtle')
for i in range (1,6):
    for j in range(72):
        turtle.forward(5*i/2)
        turtle.left(5)
    for j in range(72):
        turtle.forward(5 * i / 2)
        turtle.right(5)
