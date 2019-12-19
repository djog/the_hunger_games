from pygame.math import Vector2

class World:

    def __init__(self, size: tuple):
        self.size = Vector2()
        self.size.x, self.size.y = size
