import turtle as tur

tur.shape('turtle')
n=50
x,y=0,0
for i in range(5):
    i=i*10
    tur.penup()
    tur.goto(x-i, y-i)
    tur.pendown()
    tur.forward(50+2*i)
    tur.left(90)
    tur.forward(50+2*i)
    tur.left(90)
    tur.forward(50+2*i)
    tur.left(90)
    tur.forward(50+2*i)
    tur.left(90)
input()