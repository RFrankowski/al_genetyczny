import pygame
from pygame.math import Vector2
import random


class Food(object):
    def __init__(self, gra):
        self.xy = Vector2((random.randint(1, 600), random.randint(1, 600))) #Vector2(
        self.gra = gra

    def draw(self):
        pygame.draw.rect(self.gra.screen, (250, 200, 0), pygame.Rect(self.xy.x, self.xy.y, 10, 10))

    def pickLoka(self):
        self.xy = Vector2((random.randint(100, 500), random.randint(100, 500))) #Vector2(

    def zwroc_loka(self):
        return self.xy

        # food = wybierz_lokalizacje()

"""def dod_food(self):
szerokosc = self.screen.get_size()[0]
wysokosc = self.screen.get_size()[1]
self.food = pygame.math.Vector2((random.randint(0, szerokosc), random.randint(0, wysokosc)))
pygame.draw.rect(self.screen, (0, 200, 0), pygame.Rect(self.food.x, self.food.y, 10, 10))
def wybierz_lokalizacje():
food = pygame.math.Vector2((random.randint(1, 600), random.randint(1, 600)))
return food"""
