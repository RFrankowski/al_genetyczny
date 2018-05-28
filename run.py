import pygame as pg, sys
from rocket import Rocket
class Game(object):

    def __init__(self):
        #config
        self.max_tps = 100.0

        #inicjalizacja
        pg.init()
        self.tps_clock = pg.time.Clock()
        self.screen = pg.display.set_mode((800, 600))
        self.tps_delta = 0.0
        self.player = Rocket(self)

        while True:
            # handle events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)

            #ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1 / self.max_tps
            #rysowanie
                self.screen.fill((0, 0, 0))
                self.draw()
                pg.display.flip()

    def tick(self):
        self.player.tick()

    def draw(self):
        # type: () -> object
        self.player.draw()


if __name__ == '__main__':
    Game()

"""
max_tps = 1000.0
pg.init()
screen = pg.display.set_mode((800, 600))
box = pg.Rect(10,50,50,50)
clock = pg.time.Clock()
delta = 0.0

while True:
    #handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit(0)


    #clock
    delta += clock.tick()/1000.0
    while delta > 1/max_tps:
        delta -=1/max_tps
        # ruch
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            box.x += 1
        if keys[pg.K_a]:
            box.x += -1
        if keys[pg.K_w]:
            box.y += -1
        if keys[pg.K_s]:
            box.y += 1

    #rysowanie
    screen.fill((0,0,0))
    pg.draw.rect(screen,(0,200,0),box)
    pg.display.flip()
"""