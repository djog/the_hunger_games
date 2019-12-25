from pygame.math import Vector2

class World:

    def __init__(self, size: tuple):
        self.size = Vector2()
        self.size.x, self.size.y = size

        self.agents = []

    def add_agent(self, a):
        self.agents.append(a)

    def update(self):
        # update agents
        for a in self.agents:
            a.update(self)

    def __str__(self):
        return "World - {}".format(self.size)
