import pandas as pd
import numpy as np
from turtle import Turtle, Screen

class State(Turtle):
    def write_state(self, x, y, state):
        self.goto(x, y)
        self.write(state, align="center", font=("Courier", 8, "normal"))


screen = Screen()
screen.title("U.S. States Game")
image = "Python100day/Intermediate/Panda/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
us_state = pd.read_csv("Python100day/Intermediate/Panda/us-states-game-start/50_states.csv")
print(us_state.head())
print(us_state.tail())
