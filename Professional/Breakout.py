import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-2, 2])
ball.dy = -2

# Create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-7, 8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x * 50, 200 - y * 30)
        bricks.append(brick)

# Function to move the paddle left
def move_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

# Function to move the paddle right
def move_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for wall collisions
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Check for paddle collision
    if (ball.ycor() < -240) and (ball.xcor() > paddle.xcor() - 50) and (ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Check for brick collisions
    for brick in bricks:
        if (ball.ycor() > brick.ycor() - 20) and (ball.ycor() < brick.ycor() + 20) and (ball.xcor() > brick.xcor() - 50) and (ball.xcor() < brick.xcor() + 50):
            bricks.remove(brick)
            brick.goto(1000, 1000)  # Move brick off the screen
            ball.dy *= -1

    # Check if all bricks are destroyed
    if len(bricks) == 0:
        ball.goto(0, 0)
        ball.dx = random.choice([-2, 2])
        ball.dy = -2
        for brick in bricks:
            brick.goto(brick.xcor(), brick.ycor() - 100)

    # Check for game over
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        for brick in bricks:
            brick.goto(brick.xcor(), brick.ycor() - 100)
