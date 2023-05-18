from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
my_screen = Screen()
print(my_screen.canvheight)
tim.color("red")

tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.hideturtle()
tim.right(90)
tim.forward(100)
my_screen.exitonclick()
