import turtle

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
ball.dx = 0.2
ball.dy = -0.2

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-7, 8):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(x * 70, 200 - y * 30)
        bricks.append(brick)

# Move the paddle left
def move_left():
    x = paddle.xcor()
    if x > -340:
        x -= 20
    paddle.setx(x)

# Move the paddle right
def move_right():
    x = paddle.xcor()
    if x < 340:
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

    # Check for ball collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for ball collision with paddle
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (ball.ycor() < paddle.ycor() + 10 and ball.ycor() > paddle.ycor() - 10):
        ball.sety(paddle.ycor() + 20)
        ball.dy *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (ball.ycor() < paddle.ycor() + 10 and ball.ycor() > paddle.ycor() - 10):
        ball.sety(paddle.ycor() + 20)
        ball.dy *= -1

    # Check for ball collision with bricks
    for brick in bricks:
        if (brick.dx > 0) and (brick.xcor() + 30 > ball.xcor() > brick.xcor() - 30) and (
                brick.ycor() + 10 > ball.ycor() > brick.ycor() - 10):
            brick.goto(1000, 1000)  # Move brick off the screen
            ball.dx *= -1
            ball.dy *= -1

        if (brick.dx < 0) and (brick.xcor() + 30 > ball.xcor() > brick.xcor() - 30) and (
                brick.ycor() + 10 > ball.ycor() > brick.ycor() - 10):
            brick.goto(1000, 1000)  # Move brick off the screen
            ball.dx *= -1
            ball.dy *= -1
