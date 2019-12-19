import pygame

pygame.init()

screen = pygame.display.set_mode([600, 600])
grid_size = 15
cell_size = 35
offset = (pygame.display.Info().current_w - grid_size * cell_size) / 2

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for x in range(grid_size * grid_size):
        pygame.draw.rect(screen, [0, 0, 0], [(x % grid_size) * cell_size + offset, int(x / grid_size) * cell_size + offset, cell_size, cell_size], 1)

    pygame.display.flip()

pygame.quit()