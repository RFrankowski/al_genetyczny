import random

import math
import numpy as np


class Miasto():
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)

        # self.y = random.randint(10, 500)
        #
        # self.y = random.randint(0, 20)

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


# print generuj_populacjie_starowa(3, 1, 1)


def alg_genetyczny(ile_miast, poczatek, ile_populacji):
    populacja_startowa = generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji)

    miasta = []
    for miasto in range(ile_miast):
        miasta.append(Miasto())

    for i in miasta:
        print(i.x, i.y)

    dlugosc = 0
    for i in range(ile_miast):
        if i != ile_miast - 1:
            dlugosc += math.sqrt(abs((miasta[i + 1].x - miasta[i].x) ^ 2 + (miasta[i + 1].y - miasta[i].y) ^ 2))

    print(dlugosc)


alg_genetyczny(3, 1, 1)
