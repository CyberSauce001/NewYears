from turtle import *
from random import randint
import random

BG_COLOR = "black"
t = Turtle()
t.speed(20)
screen = t.getscreen()
screen.bgcolor(BG_COLOR)
screen.title('New Years')
screen.setup(width = 1.0, height = 1.0)
half_angle = 45
r_angle = 90
radius = 70
half = 180
full = 360
def date(t, x, y, width, height, angled):
    #Draw the Number 2
    t.pen(fillcolor="gold",pencolor="red", pensize=3)
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
    t.left(-half_angle)
    t.forward(height*2.5)
    t.left(-135)
    t.forward(-height-7)
    t.goto(x,y)
    t.end_fill()
    t.penup()

    #Draw the Number 0
    t.goto(x+225,y)
    t.pendown()
    t.begin_fill()
    t.setheading(half)
    for i in range(2):
        t.forward(width/3)
        t.right(half_angle)
        t.forward(height)
        t.right(half_angle)
        t.forward(height*2.7)
        t.right(half_angle)
        t.forward(height)
        t.right(half_angle)
        t.forward(width/3)
    t.goto(x+225, y)
    t.end_fill()
    t.penup()
    t.pen(fillcolor="black", pencolor="red", pensize=3)
    t.goto(x+237, y+75)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(width/4)
        t.right(half_angle)
        t.forward(height/4)
        t.right(half_angle)
        t.forward(height)
        t.right(half_angle)
        t.forward(height/4)
        t.right(half_angle)
    t.goto(x+237, y+75)
    t.end_fill()
    t.penup()

    #Draw the Number 1
    t.pen(fillcolor="gold", pencolor="red", pensize=3)
    t.goto(x+350,y)
    t.pendown()
    t.begin_fill()
    t.setheading(full)
    for i in range(2):
        t.forward(width/2)
        t.left(r_angle)
        t.forward(height*4)
        t.left(r_angle)
    t.end_fill()
    t.penup()

    #Draw the Number 9
    t.goto(x+500, y)
    t.pendown()
    t.begin_fill()
    t.setheading(full)
    for i in range(2):
        t.forward(width/3)
        t.left(r_angle)
        t.forward(height*4)
        t.left(r_angle)
    t.goto(x+500, y+100)
    t.setheading(half)
    for i in range(2):
        t.forward(width-30)
        t.right(r_angle)
        t.forward(height*2)
        t.right(r_angle)
    t.end_fill()
    t.penup()
    t.pen(fillcolor="black", pencolor="black", pensize=3)
    t.goto(x+470, y+130)
    t.pendown()
    t.begin_fill()
    t.setheading(r_angle)
    t.forward(50)
    t.end_fill()
    t.penup()

def stars():
    number_of_stars = randint(20, 35)
    t.pen(pencolor="white", pensize=1)
    for _ in range(0, number_of_stars):
        x_star = randint(-(screen.window_width() // 2), screen.window_width() // 2)
        y_star = randint(300, screen.window_height() // 2)
        t.penup()
        t.goto(x_star, y_star)
        t.pendown()
        for i in range(15):
            t.forward(i * 3)
            t.right(144)
    t.penup()


def fireworks():
    t.penup()
    t.color("white")
    t.goto(-300, -500)
    size = 10
    t.pen(pencolor="white", pensize=1)
    for i in range(20):
        t.stamp()
        size = size + 2
        t.forward(size)
        if i < 7:
            t.clearstamps()
        if i > 12:
            t.clearstamps(2)
    for x in range(90):
        t.pendown()
        t.speed(5)
        t.pencolor(random.random(), random.random(), random.random())
        t.width(x/100+1)
        t.forward(x)
        t.left(59)

def fireworks():
    t.penup()
    t.color("white")
    t.goto(-300, -500)
    size = 10
    j = 0
    t.pen(pencolor="white", pensize=1)
    for c in range(3):
        t.goto(-300+j, -500)
        for i in range(20):
            t.stamp()
            size = size + 2
            t.forward(size)
            if i < 7:
                t.clearstamps()
            if i > 12:
                t.clearstamps(2)
        for x in range(90):
            t.pendown()
            t.speed(5)
            t.pencolor(random.random(), random.random(), random.random())
            t.width(x/100+1)
            t.forward(x)
            t.left(59)
        t.setheading(90)
        size = 10
        j+=10
        t.penup()

date(t, -250,-300, 100, 50, 130)
#stars()
fireworks()
screen.mainloop()

#define fireworks



