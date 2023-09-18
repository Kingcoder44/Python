from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
