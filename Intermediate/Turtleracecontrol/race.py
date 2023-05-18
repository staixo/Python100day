import turtle
import random

turtlelist=[]
colors = ["red","green","blue","orange","yellow","purple","pink","brown","black","white"]

for color in colors:
    tim = turtle.Turtle()
    tim.shape("turtle")
    tim.color(color)
    turtlelist.append(tim)

def place(turtlelist,numberrange,size):
    for turtle in turtlelist:
        turtle.penup()
        turtle.goto(-size,-(size/(numberrange+1))*turtlelist.index(turtle)+size/2)
        turtle.pendown()

def race(turtlelist,size,textinput):
    for i in range(size):
        for turtle in turtlelist:
            turtle.forward(random.randint(1,10))
            if turtle.xcor() >= size/2:
                print("winner is : "+ turtle.color()[0])
                print("you entered : "+textinput)
                if textinput == turtle.color()[0]:
                    print("You win !!")
                else:
                    print("You lose !!")
                return turtle.color()[0]

my_screen = turtle.Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
textinput = turtle.textinput("Winner ?","Enter your guess, who will win ?")
print(len(turtlelist))
place(turtlelist,len(turtlelist),400)

while race(turtlelist,400,textinput) == None:
    pass

my_screen.exitonclick()
