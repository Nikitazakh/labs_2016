import turtle as tur
n=int(input())
for i in range(n):
    tur.forward(50)
    tur.stamp()
    tur.left(180)
    tur.forward(50)
    tur.left(180)
    tur.left(360/n)
input()