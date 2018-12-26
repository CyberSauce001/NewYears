from turtle import *
from random import randint

BG_COLOR = "black"
t = Turtle()
t.speed(2)
screen = t.getscreen()
screen.bgcolor(BG_COLOR)
screen.title('New Years')
screen.setup(width = 1.0, height = 1.0)

r_angle = 90
radius = 70
half = 180
def date(t, x, y, width, height, angled):
    #Draw the Number 2
    t.pen(fillcolor="gold",pencolor="white", pensize=3)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(r_angle)
    t.forward(height)
    t.left(r_angle)
    t.forward(width)
    t.right(angled)
    t.forward(height*2.5)
    t.setheading(r_angle)
    t.circle(radius,half)
    t.left(r_angle)
    t.forward(width/3)
    t.setheading(r_angle)
    t.circle(-radius/2,half)
    t.left(-45)
    t.forward(height*2.5)
    t.left(-135)
    t.forward(-height-10)
    t.goto(x,y)
    t.end_fill()
    t.penup()

    t.goto(x+225,y)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(45)
    t.forward(height/2)
    t.left(45)
    t.forward(height)
    t.left(135)
    t.forward(height/2)
    t.left(180)
    t.forward(width/2)
    t.penup()
date(t, -500,-100, 100, 50, 130)
screen.mainloop()
