import turtle
import random
import math



def move(turtle,numberofcirle):
    turtle.penup()
    print(turtle.position())
    turtle.setx(math.cos(numberofcirle/math.pi)*50)
    turtle.sety(math.sin(numberofcirle/math.pi)*50)
    turtle.pendown()
    turtle.circle(50)



tim = turtle.Turtle()
tim.color(["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])])
tim.hideturtle()
tim.speed(200)
tim.width(1)
tim.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)
x,y=turtle.position()
for number in range (1,1000):
    move(tim, number)




