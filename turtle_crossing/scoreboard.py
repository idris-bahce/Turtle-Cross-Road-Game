from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.write_score()

    def level_up(self):
        self.level += 1

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
