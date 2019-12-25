from pygame.math import Vector2

from logics.agent import Agent


class World:

    def __init__(self, size: tuple):
        self.size = Vector2()
        self.size.x, self.size.y = size

        self.agents = []

    def add_agent(self, a: Agent):
        self.agents.append(a)

    def update(self):
        # update agents
        for a in self.agents:
            a.update()
