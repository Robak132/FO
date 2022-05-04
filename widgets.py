import pygame
from consts import *


class Widget:
    def handle_event(self, event):
        raise Exception("This is interface")


class Slider(Widget):
    def __init__(self, screen, name, val, maxi, mini, xpos, ypos, font):
        self.screen = screen
        self.val = val    # start value
        self.maxi = maxi  # maximum at widgets.py position right
        self.mini = mini  # minimum at widgets.py position left
        self.xpos = xpos
        self.ypos = ypos
        self.surf = pygame.surface.Surface((150, 100))
        self.txt_surf = font.render(name, True, WHITE)
        self.txt_rect = self.txt_surf.get_rect(center=(75, 15))

        self.hit = False  # the hit attribute indicates widgets.py movement due to mouse interaction

        self.button_surf = self.render()

    def render(self):
        pygame.draw.rect(self.surf, WHITE, [35, 30, 80, 5], 0)
        self.surf.blit(self.txt_surf, self.txt_rect)
        button_surf = pygame.surface.Surface((20, 20))
        button_surf.fill(TRANS)
        button_surf.set_colorkey(TRANS)
        pygame.draw.circle(button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(button_surf, ORANGE, (10, 10), 4, 0)
        return button_surf

    def draw(self):
        surf = self.surf.copy()
        pos = (35 + int((self.val - self.mini) / (self.maxi - self.mini) * 80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position
        self.screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 35) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
        print(self.val)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(pos):
                self.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.hit = False
        elif event.type == pygame.MOUSEMOTION:
            if self.hit:
                self.move()
