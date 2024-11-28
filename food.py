from  turtle import Turtle
import random
COLOR=["red","green","yellow","blue","orange"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.fillcolor(random.choice(COLOR))
        self.shapesize(1,1)
        self.refresh()

    def refresh(self):
        """REFRESH THE FOOD POSITION  RANDOMLY"""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.fillcolor(random.choice(COLOR))
        self.goto(x, y)







