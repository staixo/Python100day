from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
my_screen = Screen()
print(my_screen.canvheight)
tim.color("red")

for _ in 4:
    tim.forward(100)
    tim.right(90)

my_screen.exitonclick()
