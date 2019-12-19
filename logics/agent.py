from pygame.math import Vector2


class Agent(object):
    def __init__(self):
        self.lifetime = 0
        self.location = Vector2()
        self.location.x, self.location.y = 0, 0