import turtle
import random
import colorgram

colors = colorgram.extract('Python100day\Intermediate\Turtle\image.png', 30)

rgb_colors=[]
for color in colors:
    r = int(color.rgb.r)/255
    g = int(color.rgb.g)/255
    b = int(color.rgb.b)/255
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

def antipyrylazo(turtle, size):
    for _ in range (10):
        turtle.dot(5*size)
        turtle.penup()
        turtle.color(random.choice(rgb_colors))
        turtle.forward(10*size)
        turtle.pendown()
    turtle.left(90)
    turtle.dot(5*size)
    turtle.penup()
    turtle.color(random.choice(rgb_colors))
    turtle.forward(10*size)
    turtle.left(90)
    for _ in range (10):
        turtle.dot(5*size)
        turtle.penup()
        turtle.color(random.choice(rgb_colors))
        turtle.forward(10*size)
        turtle.pendown()
    turtle.dot(5*size)
    turtle.right(90)
    turtle.penup()
    turtle.color(random.choice(rgb_colors))
    turtle.forward(10*size)
    turtle.right(90)

tim = turtle.Turtle()
tim.hideturtle()
tim.shape("turtle")
my_screen = turtle.Screen()
print(my_screen.canvheight)
tim.penup()
size = 6
tim.setx(-size*50)
tim.sety(-size*50)
for side in range (20):
    antipyrylazo(tim, size)
