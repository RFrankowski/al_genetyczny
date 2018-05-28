import pygame

class Woda(object):
    def __init__(self, Gra_space, x, y):
        self.gra = Gra_space
        self.x = x
        self.y = y

        self.toDelete =False

    def draw(self):
        pygame.draw.ellipse(self.gra.screen, (50, 0, 200), pygame.Rect(self.x, self.y, 10, 10))
        self.move()

    def move(self):
        self.y -= 10

    def hits(self, flower):
        if self.x + 20 > flower.x > self.x - 20 and \
                                            self.y + 20 > flower.y > self.y - 20:
            flower.rad += 5
            #if flower.rad > 50:

            return True






