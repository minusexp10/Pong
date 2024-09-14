import random


class SliderControl:

    def __init__(self, screen, slider, mode):
        self.slider = slider
        self.screen = screen
        self.mode = mode

    def up(self):
        if self.slider.ycor() < 330:
            self.slider.sety(self.slider.ycor() + 10)
            self.screen.update()

    def down(self):
        self.slider.sety(self.slider.ycor() - 10)
        self.screen.update()

    def comp_ai(self, ball):
        # error = random.randint(-50, 50)
        # if self.mode == 0:
        #     error /= 10
        # elif self.mode == 1:
        #     error /= 50
        # elif self.mode == 2:
        #     error /= 100
        if ball.ycor() > self.slider.ycor():
            while abs(self.slider.ycor()-ball.ycor()) > 40:
                self.up()
        else:
            while abs(self.slider.ycor()-ball.ycor()) > 40:
                self.down()
