import pygame, sys



class gra(object):
    def __init__(self):
        #clasy


        pygame.init()
        # tick i screen
        self.screen = pygame.display.set_mode((400, 400))
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
        pass

gra()