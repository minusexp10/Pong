from turtle import  Turtle


class Design(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.setheading(90)
        self.color("white")
        self.goto(0, - 360)

        #   dashed line
        while self.ycor() < 370:
            self.pd()
            self.forward(10)
            self.pu()
            self.forward(10)
