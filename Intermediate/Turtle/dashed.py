import turtle

tim = turtle.Turtle()

tim.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)


for _ in range (20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
my_screen.exitonclick()