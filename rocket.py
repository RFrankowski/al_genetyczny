import pygame as pg

from pygame.math import Vector2

class Rocket(object):

    def __init__(self,game):
        self.game = game
        self.speed =1.2
        self.gravity = 0.2
        size = self.game.screen.get_size()
        self.pos = Vector2(size[0]/2, size[1]/2)

        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)


    def add_force(self, force):
        self.acc += force

    def tick(self):
        #wejscie
        wcisniety = pg.key.get_pressed()
        if wcisniety[pg.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if wcisniety[pg.K_s]:
            self.add_force(Vector2(0, self.speed))
        if wcisniety[pg.K_d]:
            self.add_force(Vector2(self.speed, 0))
        if wcisniety[pg.K_a]:
            self.add_force(Vector2(-self.speed, 0))

        #fizyka
        #opor powietrza
        self.vel *= 0.9
        #grawitacja
        self.vel -= Vector2(0,-self.gravity)
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        # type: () -> object
        # rysowanie
        #podstawowy trojkont
        points = [Vector2(0,-10),Vector2(5,5),Vector2(-5,5)]

        #obracanie
        angle = self.vel.angle_to(Vector2(0, 1))
        points = [p.rotate(angle) for p in points]

        points = [Vector2(p.x, p.y*-1) for p in points]

        # dodajemy pozycje
        points = [self.pos + p * 2 for p in points]
        pg.draw.polygon(self.game.screen,(0,100,255),points)
        #prostokont = pg.Rect(self.pos.x, self.pos.y, 50, 50)
        #pg.draw.rect(self.game.screen, (0, 200, 0), prostokont)
