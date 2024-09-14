from turtle import Screen
from slider import Slider
from ball import Ball
from slider_control import SliderControl
from design import Design
from mode import Mode
import time
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# Screen Setup
screen = Screen()
screen.title("Pong")
screen.setup(1280, 720)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# Mode selection
MODE = 0
SPEED = 0
mode = Mode(screen)
screen.update()
while not mode.start:
    MODE = mode.mode
    screen.update()

if mode.start:
    # Panel creation
    user = Slider((-600, 0))
    comp = Slider((600, 0))
    ball = Ball(screen, user, comp)
    Design()
    screen.update()

    if MODE == 0:
        SPEED = 0.030
    elif MODE == 1:
        SPEED = 0.025
    elif MODE == 2:
        SPEED = 0.010

    gameplay = SliderControl(screen, user, MODE)
    screen.onkeypress(gameplay.up, "Up")
    screen.onkeypress(gameplay.down, "Down")
    autoplay = SliderControl(screen, comp, MODE)
    while not ball.game_over:
        autoplay.comp_ai(ball)
        ball.motion()
        ball.end()
        time.sleep(SPEED)


screen.exitonclick()
