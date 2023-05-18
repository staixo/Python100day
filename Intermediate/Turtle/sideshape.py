import turtle
import random


def shapeandback(turtle, length, sides):
    turtle.color(["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])])
    for _ in range(sides):
        turtle.forward(int(length))
        turtle.right(360/sides)


tim = turtle.Turtle()
tim.hideturtle()
tim.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)

for side in range (3,11):
    shapeandback(tim, 100, side)


