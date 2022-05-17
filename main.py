import random
import pygame as pygame
from consts import *
from widgets import Slider


def render_static(screen):
    screen.fill(BLACK)
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
    electrons = []
    for i in range(atom_conc.val+25):
        electrons.append(pygame.draw.circle(screen, GREEN, (115, 475 + random.randint(0, 500)), 1))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for s in interactables:
                s.handle_event(event)

        render_static(screen)
        for s in interactables:
            s.draw()

        new_electrons = []
        for electron in electrons:
            if electron.x + 1 < 875:
                new_electrons.append(pygame.draw.circle(screen, GREEN, (electron.centerx + 1, electron.centery), 1))
        electrons = new_electrons

        pygame.display.flip()

pygame.quit()
