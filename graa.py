import pygame, sys
from snake import Snakee
from food import Food


class gra(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.s = Snakee(self)
        self.F = []
        for i in range(0, 10):
            self.F.append(Food(self))
        # self.f = Food(self)
        # tick
        self.max_tps = 50.0
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tps_delta -= 1 / self.max_tps
                # rysowanie
                self.screen.fill((0, 0, 0))
                self.draw()
                pygame.display.flip()

    def draw(self):
        self.s.draw()
        # self.f.draw()
        self.s.eat()
        self.s.death()
        for i in range(0, 10):
            self.F[i].draw()
            # self.food = pygame.math.Vector2((random.randint(0, szerokosc), random.randint(0, wysokosc)))
            # pygame.draw.rect(self.screen, (0, 200, 0), pygame.Rect(food[0], food[1], 10, 10))
            # self.s.eat((food[0], food[1]))


gra()
