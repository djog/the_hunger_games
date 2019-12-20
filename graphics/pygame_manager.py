import pygame

from logics.world import World


class Graphics(object):

    def __init__(self, window_size, world_size):
        self.w = World((world_size, world_size))
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.Running = True
        self.gridsize = world_size

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False

    def draw(self):
        self.screen.fill((255, 255, 255))

        # Calculate cell size based on the world size and window size
        cell_size = int(((pygame.display.Info().current_w - 30) / self.gridsize) + 0.5)
        offset = (pygame.display.Info().current_w - (self.gridsize * cell_size)) / 2

        # draw
        for x in range(self.gridsize * self.gridsize):
            pygame.draw.rect(self.screen, [0, 0, 0], [(x % self.gridsize) * cell_size + offset, int(x / self.gridsize) * cell_size + offset, cell_size, cell_size], 1)

        pygame.display.flip()

    @staticmethod
    def close():
        pygame.quit()

    # for x in range(grid_size * grid_size):
    #     pygame.draw.rect(screen, [0, 0, 0], [(x % grid_size) * cell_size + offset, int(x / grid_size) * cell_size + offset, cell_size, cell_size], 1)


