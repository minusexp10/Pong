from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Game Over/ Default turtle
        self.hideturtle()
        self.pu()
        self.color("white")
        # User's score tracker
        self.user_score = Turtle()
        self.score_user = 0
        self.user_score.hideturtle()
        self.user_score.pu()
        self.user_score.color("white")
        self.user_score.goto(-50, 320)       # ball bounces off wall @ 320
        self.user_score.write(arg=self.score_user, align=ALIGNMENT, font=FONT)

        # Computer's score tracker
        self.comp_score = Turtle()
        self.score_comp = 0
        self.comp_score.hideturtle()
        self.comp_score.pu()
        self.comp_score.color("white")
        self.comp_score.goto(50, 320)       # ball bounces off wall @ 320
        self.comp_score.write(arg=self.score_comp, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_user(self):
        self.score_user += 1
        self.user_score.clear()
        self.user_score.write(arg=self.score_user, align=ALIGNMENT, font=FONT)

    def update_comp(self):
        self.score_comp += 1
        self.comp_score.clear()
        self.comp_score.write(arg=self.score_comp, align=ALIGNMENT, font=FONT)
