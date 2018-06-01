import random
import sys, pygame
import math
import numpy as np

random.seed(0)


class Miasto():
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.do_ktorej = -1
        self.ustaw_czas()


    def ustaw_czas(self):
        tr = random.random()
        if tr < 0.3:
            self.do_ktorej = random.randint(8, 16)


def generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji):
    populacja = []
    for p in range(ile_populacji):
        osobnik = []
        for miasto in range(ile_miast):
            if poczatek != miasto:
                osobnik.append(bin(miasto))
        random.shuffle(osobnik)
        osobnik.insert(0, bin(poczatek))
        osobnik.append(bin(poczatek))
        # print len(osobnik)
        populacja.append(osobnik)
    return populacja


def ocen(pop_start, miasta):
    ocena = []
    # print len(pop_start)
    for osobnik in pop_start:
        czas = 7  # kurier zaczyna prace o 7
        dlugosc_trasy = 0
        for i in enumerate(osobnik):
            if i[0] != len(osobnik) - 1:
                miasto1 = osobnik[i[0]]
                miasto2 = osobnik[i[0] + 1]
                # print(pop_start)

                # print osobnik[i[0]], osobnik[i[0] + 1]
                # print (miasta[int(miasto1,2)].x, miasta[int(miasto2].x)/
                # print (miasta[miasto1].y, miasta[miasto2].y)

                # print (int(miasto2, 2))
                # print (int(miasto1, 2))
                # # print osobnik
                #
                # print (miasta[int(miasto2, 2)].x , miasta[int(miasto1, 2)].x)
                # igreki = math.pow(abs((miasta[int(miasto2, 2)].y - miasta[int(miasto1, 2)].y)), 2)

                iksy = math.pow(abs((miasta[int(miasto2, 2)].x - miasta[int(miasto1, 2)].x)), 2)
                igreki = math.pow(abs((miasta[int(miasto2, 2)].y - miasta[int(miasto1, 2)].y)), 2)
                odcinek = math.sqrt(abs(iksy + igreki))
                dlugosc_trasy += odcinek
                czas += (odcinek / 2) / 60
                if miasta[int(miasto1, 2)].do_ktorej > czas:
                    # jak sie nie wyrobi to dostaje kare w wysorkosci 500
                    dlugosc_trasy += 500

        ocena.append(dlugosc_trasy)

    return ocena


def get_probability_list(fitnes):
    fitness = fitnes
    total_fit = float(sum(fitness))
    relative_fitness = [f / total_fit for f in fitness]
    probabilities = [sum(relative_fitness[:i + 1])
                     for i in range(len(relative_fitness))]
    return probabilities


def roulette_wheel_pop(population, probabilities, number):
    chosen = []
    for n in range(number):
        r = random.random()
        for (i, individual) in enumerate(population):
            if r <= probabilities[i]:
                chosen.append(individual)
                break
    return chosen


def selekcja(populacja, ocena):
    new = []
    for ind, wartosc in enumerate(ocena):
        new.append([[wartosc], populacja[ind]])
    new.sort(key=lambda b: b)
    new.reverse()
    posortowane = []
    for fit, droga in new:
        posortowane.append(droga)
    propa = get_probability_list(ocena)

    return roulette_wheel_pop(posortowane, propa, 160)


def krzyzowanie(populacja, pocz):
    pocz = bin(pocz)
    po_krzyzowce = []
    for osobnik in populacja:

        cr = random.random()
        po_krzyzowce.append(osobnik)
        if cr > 0:
            matka = random.choice(populacja)[1:len(osobnik) - 1]

            punkt_podzialu = random.randint(1, len(osobnik) - 1)

            syn = [pocz]

            syn.extend(osobnik[1:punkt_podzialu])
            for gen in matka:
                if gen not in syn and gen != pocz and len(syn) != len(osobnik) - 1:
                    syn.extend([gen])
            syn.extend([pocz])
            po_krzyzowce.append(syn)

            corka = [pocz]
            corka.extend(matka[1:punkt_podzialu])
            for gen in osobnik:
                if gen not in corka and gen != pocz and len(corka) != len(osobnik) - 1:
                    corka.extend([gen])
            corka.extend([pocz])
            po_krzyzowce.append(corka)
    return po_krzyzowce


def mutacja(populacja, ile_miast):
    for osobnik in populacja:
        for ind, wartosc in enumerate(osobnik):
            if 0.03 > random.random():
                if ind != 0 and ind != len(osobnik)-1:
                    mut = random.randint(1, ile_miast -1)
                    wartosc1 = osobnik[mut]
                    osobnik[mut] = wartosc
                    osobnik[ind] = wartosc1
    return populacja


global miasta
miasta = []



def genetyk(ile_miast, poczatek, ile_populacji):
    pop_start = generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji)
    for i in range(ile_miast):
        miasta.append(Miasto())
    ocena = ocen(pop_start, miasta)
    po_selekcji = selekcja(pop_start, ocena)
    po_krzyzowaniu = krzyzowanie(po_selekcji, poczatek)
    po_mutacji = mutacja(po_krzyzowaniu, ile_miast)
    ocena = ocen(po_mutacji, miasta)

    i = 0
    while i < 500:
        print i
        po_selekcji = selekcja(po_mutacji, ocena)
        po_krzyzowaniu = krzyzowanie(po_selekcji, poczatek)
        po_mutacji = mutacja(po_krzyzowaniu, ile_miast)
        ocena = ocen(po_mutacji, miasta)

        i += 1

    print(ocena)

    return po_mutacji[ocena.index(min(ocena))]


# ile_miast, poczatek, ile_populacji

from nowy_genetyk import Gra

if __name__ == '__main__':

    sciezka = genetyk(11, 0, 160)
    print sciezka
    for ind, wart in enumerate(sciezka):
        sciezka[ind] = int(wart, 2)
    for m in miasta:
        print (m.x, m.y)
        print m.do_ktorej
        print "\n"
    # print sciezka
    g = Gra(miasta, sciezka)
