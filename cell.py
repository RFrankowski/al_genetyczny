import pygame

class Flower(object):

    def __init__(self, Gra_space, i, j):
        self.gra = Gra_space
        self.i = i
        self.j = j



    def draw(self):
        pygame.draw.Rect(self.gra.screen, (200, 200, 50), pygame.Rect(self.x, self.y, 10, 10))