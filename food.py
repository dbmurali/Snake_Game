from  turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.fillcolor("yellow")
        self.shapesize(1,1)
        self.refresh()

    def refresh(self):
        """REFRESH THE FOOD POSITION  RANDOMLY"""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)







