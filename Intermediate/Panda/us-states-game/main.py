import pandas as pd
import numpy as np
from turtle import Turtle, Screen
import random

class State(Turtle):
    def write_state(self, x, y, state):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state, align="center", font=("Courier", 8, "normal"))



screen = Screen()
screen.title("U.S. States Game")
image = "Python100day/Intermediate/Panda/us-states-game/blank_states_img.gif"
screen.bgpic(image)
us_state = pd.read_csv("Python100day/Intermediate/Panda/us-states-game/50_states.csv")
print(us_state.head())
print(us_state.tail())

game = True

while game:
    state_name = screen.textinput(title=f"{len(us_state)}/50 States Correct", prompt="What's another state's name?").title()
    if state_name == "Exit":
        print("You lost!")
        us_state.to_csv("Python100day/Intermediate/Panda/us-states-game/states_to_learn.csv")
        game = False
        break
    if state_name in us_state["state"].values:
        state_row = us_state[us_state["state"] == state_name]
        state = State()
        state.write_state(int(state_row["x"]), int(state_row["y"]), state_name)
        us_state = us_state[us_state["state"] != state_name]
        print(us_state)
    if len(us_state) == 0:
        game = False
        print("You won!")

screen.exitonclick()
