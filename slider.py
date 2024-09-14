from turtle import Turtle


class Slider(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1, 0)
        self.goto(position)


