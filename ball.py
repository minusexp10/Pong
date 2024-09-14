from turtle import Turtle
from scoreboard import Scoreboard

SPEED = 0


class Ball(Turtle):

    def __init__(self, screen, user, comp):
        super().__init__()
        self.game_over = False
        self.screen = screen
        self.pu()
        self.color("white")
        self.shape("circle")
        self.setheading(135)
        self.screen.tracer(0)
        # self.speed("normal")

        # User and Computer object maker for this class
        self.user = user
        self.comp = comp

        # Scorecard object initialization
        self.scoreboard = Scoreboard()

    def motion(self):
        self.screen.update()
        self.forward(10)
        self.collision_wall()
        self.slider_collision(self.user, self.comp)
        # self.screen.ontimer(self.motion, 15)

    def bounce_wall(self):
        if 0 < self.heading() < 90 or 180 < self.heading() < 270:
            self.right(90)
        else:
            self.left(90)

    def bounce_slider(self):
        if 0 < self.heading() < 90 or 180 < self.heading() < 270:
            self.left(90)
        else:
            self.right(90)

    def collision_wall(self):
        if self.ycor() >= 320 or self.ycor() <= -320:
            self.bounce_wall()
            
    def slider_collision(self, user, comp):
        # User
        if -580 <= self.xcor() <= -575:
            if self.distance(user) < 50:
                self.bounce_slider()
                self.scoreboard.update_user()
                self.screen.update()
        # Computer
        elif 575 <= self.xcor() <= 580:
            if self.distance(comp) < 50:
                self.bounce_slider()
                self.scoreboard.update_comp()
                self.screen.update()

    def end(self):
        if self.xcor() < -590 or self.xcor() > 590:
            self.game_over = True
            self.scoreboard.game_over()
            self.screen.onkeypress(None, "Up")
            self.screen.onkeypress(None, "Down")
