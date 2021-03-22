import turtle as t
import random


class Food(t.Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed("fastest")

    def refresh(self):
        random_x = round(random.randint(-580, 580) / 10) * 10
        random_y = round(random.randint(-380, 380) / 10) * 10
        self.goto(random_x, random_y)
