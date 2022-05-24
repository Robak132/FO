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
        self.x = 115 + random.randint(0, 30)
        # self.x = 120
        self.y = 475 + random.randint(0, 500)
        # self.y = 520
        self.vx = 0
        self.vy = 0
        self.object = pygame.draw.circle(screen, GREEN, (self.x, self.y), 2)

    def move(self):
        self.vx += 0.01
        x = self.x + self.vx
        y = self.y + self.vy

        reflected = False
        for atom in atoms:
            if math.sqrt((atom.x - x) * (atom.x - x) + (atom.y - y) * (atom.y - y)) <= interactables[2].val:
                if self.vy == 0 and self.vx == 0.01:
                    self.x = 115
                    break
                cos = (atom.x - x) / interactables[2].val
                alpha = math.acos(cos)*2 if ((atom.x - x) * (atom.y - y) < 0) else math.acos(cos)*2 - math.pi
                vx =  (-self.vx) * math.cos(alpha) + (-self.vy) * math.sin(alpha)
                vy = -(-self.vx) * math.sin(alpha) + (-self.vy) * math.cos(alpha)
                self.vy = round(vy, 6)
                self.vx = round(vx, 6)
                reflected = True
                break
        if not reflected:
            self.x = x
            self.y = y

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
        Slider(screen, "Atoms Concentration", 50, 250, 1, 425, 200, font),
        Slider(screen, "Atoms Size", 10, 20, 5, 425, 300, font)
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
