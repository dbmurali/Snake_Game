from turtle import  Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")


class Scoreboad(Turtle):
    def __init__(self):
        super().__init__()

        with open("data.txt") as file:
            self.current_score=int(file.read())

        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score+=1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        if self.score==self.current_score:
            self.current_score=self.score
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.high_scores()
        with open("data.txt") as file:
            self.current_score=int(file.read())

        self.write(f"GAME OVER\nHigh Score: {self.current_score}",align=ALIGNMENT,font=FONT)

    def high_scores(self):
        if self.score > self.current_score:
            with open("data.txt", mode="w")as file:
                file.write(self.score.__str__())




