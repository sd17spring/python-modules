"""
An implementation of the Brick Breaker game.

Software Design uses this repository as an example of how to
organize larger Python programs into modules.
"""

# By convention ( https://www.python.org/dev/peps/pep-0008/#imports )
# imports are grouped as:

# 1) standard library
import time

# 2) 3rd party libraries
import pygame
from pygame.locals import *

# 3) Local modules
from controller.keyboard_controller import Controller
from model.simple_model import Model
from view.pygame_window_view import View

if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    model = Model(size)
    view = View(screen, model)
    controller = Controller(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)

        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()
