import pygame, sys
from ship import Ship
from flower import Flower


class Gra_space(object):
    def __init__(self):
        # zmienne
        self.s = Ship(self)
        self.flower = []
        self.woda = []

        for i in range(0, 10):
            self.flower.append(Flower(self, i * 50 + 50, 50))

        # ekran
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        # tick
        self.max_tps = 15.0
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # eventy
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            # tick
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tps_delta -= 1 / self.max_tps
                # rysowanie
                self.screen.fill((0, 0, 0))
                self.draw()
                pygame.display.flip()

    def draw(self):
        # rysuje statek
        list = [(1, 1), (1, 100), (100, 1)]
        # line(Surface, color, start_pos, end_pos, width=1)
        lol = pygame.draw.line(self.screen, (255, 0, 0), (0, 0), (50, 50), 1)
        self.s.draw()
        # usuwam krople ktore wylatuja za ekran
        for i in range(0, len(self.woda)):
            if self.woda[i].y < 0:
                self.woda.pop(i)
                break
        # sprawdzam czy zestrzelilem wszyskie kwiaty
        if not self.flower:
            pass
        # odpowiada za ruch kwiatow
        elif self.flower[0].x < 0:
            for i in self.flower:
                i.speed = 4
                i.obniz()
        if not self.flower:
            pass

        elif self.flower[len(self.flower) - 1].x > 600:
            for i in self.flower:
                i.speed = -4
                i.obniz()

        # rysuje wszyskie kwiaty
        for i in range(0, len(self.flower)):
            self.flower[i].draw()
        # sprawdam czy trafiam
        for i in range(0, len(self.woda)):
            self.woda[i].draw()
            k = False
            for j in range(0, len(self.flower)):
                if self.woda[i].hits(self.flower[j]):
                    k = True
                    if self.flower[j].rad > 50:
                        self.flower.pop(j)
                    break
            if k:
                self.woda.pop(i)
                k = False
                break


Gra_space()
