from turtle import  Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")


class Scoreboad(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)


    def update_score(self):
        self.score+=1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)


