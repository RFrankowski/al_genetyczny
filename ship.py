import pygame
from woda import Woda
class Ship(object):
    def __init__(self, Gra_space):
        self.gra = Gra_space
        self.x = 300
        self.y = 560

    def draw(self):
        pygame.draw.rect(self.gra.screen, (0, 200, 0), pygame.Rect(self.x, self.y, 20, 20))
        self.keyPressed()

    def keyPressed(self):
        wcisniety = pygame.key.get_pressed()
        if wcisniety[pygame.K_a]:
            self.x -= 10
        if wcisniety[pygame.K_d]:
            self.x += 10
        if wcisniety[pygame.K_SPACE]:
            if len(self.gra.woda) < 40:
                self.gra.woda.append(Woda(self.gra, self.x, self.y))

