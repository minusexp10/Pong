from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, 'bold')


class Mode:

    def __init__(self, screen):

        # super().__init__()
        self.mode = 0
        self.start = False

        self.screen = screen
        self.easy = Turtle()
        self.easy.ht()
        self.easy.pu()
        self.easy.color("red")
        self.easy.goto(0, 50)
        self.easy.write(arg="EASY", align=ALIGNMENT, font=FONT)

        self.normal = Turtle()
        self.normal.pu()
        self.normal.ht()
        self.normal.color("white")
        self.normal.goto(0, 0)
        self.normal.write(arg="NORMAL", align=ALIGNMENT, font=FONT)

        self.hard = Turtle()
        self.hard.pu()
        self.hard.ht()
        self.hard.color("white")
        self.hard.goto(0, -50)
        self.hard.write(arg="HARD", align=ALIGNMENT, font=FONT)

        self.screen.listen()
        self.change()

    def change(self):
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.select, "Return")

    def down(self):

        if self.mode == 0:
            self.easy.clear()
            self.easy.color("white")
            self.easy.write(arg="EASY", align=ALIGNMENT, font=FONT)
            self.mode += 1
            self.normal.clear()
            self.normal.color("red")
            self.normal.write(arg="NORMAL", align=ALIGNMENT, font=FONT)
            self.screen.update()

        elif self.mode == 1:
            self.normal.clear()
            self.normal.color("white")
            self.normal.write(arg="NORMAL", align=ALIGNMENT, font=FONT)
            self.mode += 1
            self.hard.clear()
            self.hard.color("red")
            self.hard.write(arg="HARD", align=ALIGNMENT, font=FONT)
            self.screen.update()

        elif self.mode == 2:
            self.hard.clear()
            self.hard.color("white")
            self.hard.write(arg="HARD", align=ALIGNMENT, font=FONT)
            self.mode = 0
            self.easy.clear()
            self.easy.color("red")
            self.easy.write(arg="EASY", align=ALIGNMENT, font=FONT)
            self.screen.update()

    def up(self):

        if self.mode == 0:
            self.easy.clear()
            self.easy.color("white")
            self.easy.write(arg="EASY", align=ALIGNMENT, font=FONT)
            self.mode = 2
            self.hard.clear()
            self.hard.color("red")
            self.hard.write(arg="HARD", align=ALIGNMENT, font=FONT)
            self.screen.update()

        elif self.mode == 1:
            self.normal.clear()
            self.normal.color("white")
            self.normal.write(arg="NORMAL", align=ALIGNMENT, font=FONT)
            self.mode -= 1
            self.easy.clear()
            self.easy.color("red")
            self.easy.write(arg="EASY", align=ALIGNMENT, font=FONT)
            self.screen.update()

        elif self.mode == 2:
            self.hard.clear()
            self.hard.color("white")
            self.hard.write(arg="HARD", align=ALIGNMENT, font=FONT)
            self.mode -= 1
            self.normal.clear()
            self.normal.color("red")
            self.normal.write(arg="NORMAL", align=ALIGNMENT, font=FONT)
            self.screen.update()

    def select(self):
        self.easy.clear()
        self.normal.clear()
        self.hard.clear()
        self.screen.onkey(None, "Return")
        self.screen.onkey(None, "Down")
        self.screen.onkey(None, "Up")
        self.start = True
        self.screen.update()
        return self.mode
