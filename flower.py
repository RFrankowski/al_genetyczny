import pygame

class Flower(object):

    def __init__(self, Gra_space, x, y):
        self.gra = Gra_space
        self.x = x
        self.y = y
        self.rad = 10
        self.speed = 4


    def draw(self):
        pygame.draw.ellipse(self.gra.screen, (200, 200, 50), pygame.Rect(self.x, self.y, self.rad, self.rad))
        self.move()

    def move(self):
        self.x += self.speed

    def obniz(self):
        self.y += 20


