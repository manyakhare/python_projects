from turtle import Turtle
ALIGNMENT = 'center'
FONTS = ('Arial', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONTS)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONTS)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
