import random

import math
import numpy as np

random.seed(0)


class Miasto():
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)


def generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji):
    populacja = []
    for p in range(ile_populacji):
        osobnik = []
        for miasto in range(ile_miast):
            if poczatek != miasto:
                osobnik.append(miasto)
        random.shuffle(osobnik)
        osobnik.insert(0, poczatek)
        osobnik.append(poczatek)
        populacja.append(osobnik)
    return populacja


# print generuj_populacjie_starowa(3,2,1)


def genetyk(ile_miast):
    pop_start = generuj_populacjie_starowa(2, 2, 1)
    print(pop_start)
    miasta = []
    for i in range(ile_miast):
        miasta.append(Miasto())

    for i in miasta:
        print i.x, i.y

    dlugos = 0
    for i in enumerate(pop_start[0]):
        if i[0] != len(pop_start[0]) - 1:
            miasto1 = pop_start[0][i[0]]
            miasto2 = pop_start[0][i[0] + 1]
            # print pop_start[0][i[0]], pop_start[0][i[0]+1]

            dlugos += math.sqrt(
                abs((miasta[miasto2].x - miasta[miasto1].x) ^ 2 + (miasta[miasto2].y - miasta[miasto1].y) ^ 2))

    print dlugos


genetyk(3)
