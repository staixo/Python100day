from turtle import Turtle, Screen

tim = Turtle()
print(tim)
tim.shape("turtle")
my_screen = Screen()
print(my_screen.canvheight)
tim.color("red")
tim.forward(100)
tim.color("green")
tim.forward(100)
my_screen.exitonclick()
