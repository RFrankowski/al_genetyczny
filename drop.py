import pygame
from pygame.math import Vector2
import random

class Drop(object):
    def __init__(self, gra):
        self.pos=Vector2(random.randint(1, 600), random.randint(600, 1000)*(-1))
        self.gra = gra
        self.gravity = random.randint(0, 1)

    def update(self):
        self.pos.y += self.gravity
        self.gravity += 0.005
        if self.pos.y > 600:
            self.pos.y = random.randint(600, 800)*(-1)
            self.gravity = random.randint(0, 1)

    def draw(self):
        line = pygame.Rect(self.pos.x, self.pos.y, 2, random.randint(5,10))
        pygame.draw.rect(self.gra.screen, (230, 230, 250), line)
        self.update()
