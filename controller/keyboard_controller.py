"""The Brick Breaker keyboard controller."""

import pygame
from pygame.locals import *


class Controller:
    """Control Brick Breaker using the keyboard."""

    def __init__(self, model):
        """Construct a PyGameKeyboardController object.

        model: the Brick Breaker game state
        """
        self.model = model

    def handle_pygame_event(self, event):
        """Handle a PyGame key down event.

        event: a PyGame event of type KEYDOWN
        """
        if event.type != KEYDOWN:
            # nothing to do
            return
        if event.key == pygame.K_LEFT:
            self.model.change_paddle_velocity(-1)
        elif event.key == pygame.K_RIGHT:
            self.model.change_paddle_velocity(1)
