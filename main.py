import pygame
from consts import *
from widgets import Slider


def render_static():
    pygame.draw.rect(screen, BLUE, (15, 475, 100, 500))
    pygame.draw.rect(screen, RED, (875, 475, 100, 500))
    circles = []
    for x in range(12):
        for y in range(8):
            circle = pygame.draw.circle(screen, BLUE, (165 + x * 60, 515 + y * 60), 15)
            circles.append(circle)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([1000, 1000])
    font = pygame.font.SysFont("Verdana", 12)

    temp = Slider(screen, "Temperature", 50, 100, 1, 425, 100, font)
    atom_conc = Slider(screen, "Atoms Concentration", 50, 100, 1, 425, 200, font)
    atom_size = Slider(screen, "Atoms Size", 50, 100, 1, 425, 300, font)
    interactables = [temp, atom_conc, atom_size]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for s in interactables:
                s.handle_event(event)

        render_static()
        for s in interactables:
            s.draw()

        pygame.display.flip()

pygame.quit()
