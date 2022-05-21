import math
import random
import pygame as pygame
from consts import *
from widgets import Slider


def render_static():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (15, 475, 100, 500))
    pygame.draw.rect(screen, RED, (875, 475, 100, 500))
    for s in interactables:
        s.draw()


class Atom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx, self.vy = self.random_movement()
        self.object = pygame.draw.circle(screen, BLUE, (self.x, self.y), interactables[2].val)

    @staticmethod
    def random_movement():
        return random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)

    def move(self):
        self.vx, self.vy = self.random_movement()
        # self.x += self.vx
        # self.y += self.vy
        self.object = pygame.draw.circle(screen, BLUE, (self.x, self.y), interactables[2].val)


class Electron:
    def __init__(self):
        self.x = 115 + random.randint(0, 50)
        self.y = 475 + random.randint(0, 500)
        self.vx = 0
        self.vy = 0
        self.object = pygame.draw.circle(screen, GREEN, (self.x, self.y), 2)

    def move(self):
        self.vx = 2
        for atom in atoms:
            if math.sqrt((atom.x - self.x) * (atom.x - self.x) + (atom.y - self.y) * (atom.y - self.y)) < interactables[2].val:
                self.vx = 0
                self.vy = 0

        self.x += self.vx
        self.y += self.vy
        if self.y < 475:
            self.y = 975 - self.y + 475
        if self.x <= 875:
            self.object = pygame.draw.circle(screen, GREEN, (self.x, self.y), 2)
        else:
            self.__init__()


def create_atoms():
    atoms = []
    for x in range(12):
        for y in range(8):
            atoms.append(Atom(165 + x * 60, 515 + y * 60))
    return atoms


def create_electrons():
    electrons = []
    for i in range(int(interactables[1].val) + 25):
    # for i in range(1):
        electrons.append(Electron())
    return electrons


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1000, 1000])
    font = pygame.font.SysFont("Verdana", 12)

    interactables = [
        Slider(screen, "Temperature", 50, 100, 1, 425, 100, font),
        Slider(screen, "Atoms Concentration", 50, 200, 1, 425, 200, font),
        Slider(screen, "Atoms Size", 10, 15, 5, 425, 300, font)
    ]
    electrons = create_electrons()
    atoms = create_atoms()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for s in interactables:
                if s.handle_event(event):
                    electrons = create_electrons()
        render_static()

        for atom in atoms:
            atom.move()

        for electron in electrons:
            electron.move()

        pygame.display.flip()

pygame.quit()
