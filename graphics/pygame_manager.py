import pygame

from logics.world import World


class Graphics(object):

    def __init__(self, window_size):
        self.w = World()
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.Running = True

    def parse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False

    def draw(self):
        self.screen.fill((255, 255, 255))

        cell_size = 0  # Calculate cell size based on the world size and window size

        # draw

        pygame.display.flip()

    @staticmethod
    def close(self):
        pygame.quit()

    # for x in range(grid_size * grid_size):
    #     pygame.draw.rect(screen, [0, 0, 0], [(x % grid_size) * cell_size + offset, int(x / grid_size) * cell_size + offset, cell_size, cell_size], 1)


