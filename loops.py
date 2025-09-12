import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(50)

def square(x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)

def addSquares(iRange):
    length = 5
    for i in range (iRange):
        square(length, 90)
        length += 5
        t.right(5)
addSquares(60)

def star(x):
     for i in range(5):
          t.forward(x)
          t.right(144)

def starspiral(iRange):
     length = 25
     for i in range(iRange):
          star(length)
          length += 5
          t.right(5)
starspiral(65)