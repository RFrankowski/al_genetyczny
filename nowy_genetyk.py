import pygame, sys
# from drop import Drop
import random

# from nowy_genetyk_licz import Miasto


class Gra(object):
    def __init__(self, miasta,sciezka):
        self.mia = miasta
        # inicjalizacja
        # self.miasta = []
        # self.miasta.append(Miasto())
        self.li =sciezka
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
        # li = [0, 3, 1, 8, 6, 4, 2, 0]

        for i in range(0, len(self.li)-1):
            pygame.draw.line(self.screen, (0, 127, 0), (self.mia[self.li[i]].x, self.mia[self.li[i]].y),
                             (self.mia[self.li[i + 1]].x, self.mia[self.li[i + 1]].y))

            pass


if __name__ == '__main__':
    Gra()
