from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        super().color("red")
        super().shape("circle")
        super().penup()
        super().shapesize(stretch_len=0.5, stretch_wid=0.5)
        super().speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        super().goto(random_x, random_y)
