import pygame,sys
# from drop import Drop
import random



class Gra(object):
    def __init__(self,miasta):
        self.mia = miasta
        # inicjalizacja
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # ticking
        # rysowanie
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
    def draw(self):
        # x y with heith
        for m in self.mia:
            pygame.draw.ellipse(self.screen, (0, 127, 0), (m.x, m.y, 5, 5), 0)
            # pygame.draw.ellipse(self.screen, (0, 127, 0), (100, 50, 5, 5), 0)
            # pygame.draw.line(self.screen, (0, 127, 0), (10, 10), (100, 50))


if __name__ == '__main__':
    Gra()