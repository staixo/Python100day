import turtle 

tim = turtle.Turtle()

def up():
    tim.forward(10)

def down():
    tim.backward(10)

def right():
    tim.right(30)

def left():
    tim.left(30)

way = {
    "up":up,
    "down":down,
    "right":right,
    "left":left
}

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.listen()
my_screen.onkey(key="z",fun=way["up"])
my_screen.onkey(key="s",fun=way["down"])
my_screen.onkey(key="d",fun=way["right"])
my_screen.onkey(key="q",fun=way["left"])

my_screen.exitonclick()





