import turtle
import random



def randomwalk(turtle, length):
    turtle.color(["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])])
    turtle.forward(int(length))
    turtle.right(random.randint(-2,2)*90)


tim = turtle.Turtle()

tim.hideturtle()
tim.speed(200)
tim.width(5)
tim.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)

for _ in range (10000):
    randomwalk(tim, 20)


