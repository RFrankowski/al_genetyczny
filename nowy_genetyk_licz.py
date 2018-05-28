import random

import math
import numpy as np
import random as rand
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


def ocen(pop_start, miasta):
    ocena = []
    for osobnik in pop_start:
        dlugosc_trasy = 0
        for i in enumerate(osobnik):
            if i[0] != len(osobnik) - 1:
                miasto1 = osobnik[i[0]]
                miasto2 = osobnik[i[0] + 1]
                # print osobnik[i[0]], osobnik[i[0] + 1]
                # print (miasta[miasto1].x, miasta[miasto2].x)
                # print (miasta[miasto1].y, miasta[miasto2].y)

                iksy = math.pow(abs((miasta[miasto2].x - miasta[miasto1].x)), 2)
                igreki = math.pow(abs((miasta[miasto2].y - miasta[miasto1].y)), 2)
                dlugosc_trasy += math.sqrt(abs(iksy + igreki))
        ocena.append(dlugosc_trasy)

    return ocena


def selekcja(populacja, ocena):
    print(populacja)
    new = []
    for i in enumerate(ocena):
        oc = i[1]/min(ocena)
        new.append([[oc], populacja[i[0]]])


    new.sort(key=lambda b: b)
    print new


    pass



def genetyk(ile_miast, poczatek, ile_populacji):
    pop_start = generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji)
    # print(pop_start)
    miasta = []
    for i in range(ile_miast):
        miasta.append(Miasto())
    ocena = ocen(pop_start, miasta)
    selekcja(pop_start, ocena)

    # selekcja
    # krzyzowanie
    # mutacja


genetyk(5, 0, 3)



