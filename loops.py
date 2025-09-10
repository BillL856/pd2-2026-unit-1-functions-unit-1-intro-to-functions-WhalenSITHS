import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(25)

for i in range(60):
    def square(x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)
    square(100,90)
    t.right(5)

for i in range(60):
    def addsquare(x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)
    square(100,90)
    t.right(5)