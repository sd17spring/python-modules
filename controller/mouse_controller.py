"""The Brick Breaker controller."""

from pygame.locals import *


class Controller:
    """Controls Brick Breaker using the mouse."""

    def __init__(self, model):
        """Construct a PyGameMouseController object.

        model: the Brick Breaker game state
        """
        self.model = model

    def handle_pygame_event(self, event):
        """Handle a PyGame key down event.

        event: a PyGame event of type KEYDOWN
        """
        if event.type != MOUSEMOTION:
            # nothing to do
            return
        self.model.paddle.x = event.pos[0] - self.model.paddle.width / 2.0
