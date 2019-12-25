import pygame

from logics.agent import Agent
from logics.world import World


class Graphics(object):

    def __init__(self, window_size, world_size: tuple):
        self.world = World(world_size)
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.Running = True
        self.grid_width, self.grid_height = world_size

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False

    def draw(self):
        self.screen.fill((255, 255, 255))

        # Calculate cell size based on the world size and window size
        cell_size_width = int(((pygame.display.Info().current_w - 30) / self.grid_width) + 0.5)
        cell_size_height = int(((pygame.display.Info().current_h - 30) / self.grid_height) + 0.5)
        cell_size = cell_size_width if cell_size_width < cell_size_height else cell_size_height
        offset_width = (pygame.display.Info().current_w - (self.grid_width * cell_size)) / 2
        offset_height = (pygame.display.Info().current_h - (self.grid_height * cell_size)) / 2

        # draw
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                pygame.draw.rect(self.screen, [0, 0, 0], [x * cell_size + offset_width, y * cell_size + offset_height, cell_size, cell_size], 1)

        agent_size = int(cell_size / 2)
        offset_width += agent_size
        offset_height += agent_size

        for a in self.world.agents:
            pygame.draw.circle(self.screen, [0, 0, 0], [int((a.location.x * cell_size) + offset_width), int((a.location.y * cell_size) + offset_height)], agent_size)

        pygame.display.flip()

    @staticmethod
    def close():
        pygame.quit()

