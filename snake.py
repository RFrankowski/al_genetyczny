import pygame
scl = 0.2



class Snakee(object):
    def __init__(self, gra):
        self.x = 10
        self.y = 10
        self.xspeed = 1
        self.yspeed = 0
        self.gra = gra
        self.total = 1
        self.tailx = []
        self.taily = []
        self.tailx.append(round(self.x))
        self.taily.append(round(self.y))
        size = self.gra.screen.get_size()

    def update(self):
        for i in range(0, len(self.tailx) - 1):
            self.tailx[i] = self.tailx[i + 1] #+ 10 #* -self.xspeed
            self.taily[i] = self.taily[i + 1] #+ 10 #* -self.yspeed

        self.tailx[self.total - 1] = (round(self.x))
        self.taily[self.total - 1] = (round(self.y))
        self.x += self.xspeed * scl
        self.y += self.yspeed * scl

        #przechodzenie przez sciany
        if self.x > 600:
            self.x = self.x-600
        if self.y > 600:
            self.y = self.y - 600
        if self.x < 0:
            self.x = self.x+600
        if self.y < 1:
            self.y = self.y+600
    # self.tailx.append(self.x)
    # self.taily.append(self.y)


    def draw(self):
        for i in range(0, len(self.tailx)):
            pygame.draw.rect(self.gra.screen, (0, 200, 0), pygame.Rect(self.tailx[i], self.taily[i], 10, 10))
        # pygame.draw.rect(self.gra.screen, (0, 200, 0), pygame.Rect(self.x, self.y, 10, 10))
        self.keyPressed()
        self.update()

    def eat(self):


        for j in range(0, len(self.gra.F)):
            if self.x + 10 > self.gra.F[j].zwroc_loka().x > self.x - 10 and \
                                            self.y + 10 > self.gra.F[j].zwroc_loka().y > self.y - 10:
                self.gra.F[j].pickLoka()
                self.taily.append(round(self.x))
                self.tailx.append(round(self.x))
                self.total += 1

    def death(self):
        for i in range(0, len(self.tailx)-1):
            if (self.tailx[i+1]+1 > self.x > self.tailx[i+1]-1
                    and self.taily[i+1]+1 > self.y > self.taily[i+1]-1):
                self.tailx = []
                self.taily = []
                self.x = 300
                self.y = 300
                self.total = 1
                self.xspeed = 1
                self.tailx.append(300)
                self.taily.append(300)
                break

    def keyPressed(self):
        # wejscie
        wcisniety = pygame.key.get_pressed()
        if wcisniety[pygame.K_w]:
            if self.yspeed != 50:
                self.xspeed = 0
                self.yspeed = -50
        if wcisniety[pygame.K_s]:
            if self.yspeed != -50:
                self.xspeed = 0
                self.yspeed = 50
        if wcisniety[pygame.K_d]:
            if self.xspeed != -50:
                self.yspeed = 0
                self.xspeed = 50
        if wcisniety[pygame.K_a]:
            if self.xspeed != 50:
                self.yspeed = 0
                self.xspeed = -50


#eat jeden element
"""for i in range(0, len(self.tailx)):
            if (self.tailx[i] + 10 > self.gra.f.zwroc_loka()[0] > self.tailx[i] - 10
                    and self.taily[i] + 10 > self.gra.f.zwroc_loka()[1] > self.taily[i] - 10):
                self.taily.append(round(self.x) + 10 * -self.xspeed)
                self.tailx.append(round(self.x) + 10 * -self.yspeed)
                self.gra.f.pickLoka()
                self.total += 1"""