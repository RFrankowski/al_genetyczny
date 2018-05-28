import random
import sys,pygame
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
                osobnik.append(bin(miasto))
        random.shuffle(osobnik)
        osobnik.insert(0, bin(poczatek))
        osobnik.append(bin(poczatek))
        populacja.append(osobnik)
    return populacja


def ocen(pop_start, miasta):
    ocena = []
    # print len(pop_start)
    for osobnik in pop_start:
        dlugosc_trasy = 0
        for i in enumerate(osobnik):
            if i[0] != len(osobnik) -1:
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
                dlugosc_trasy += math.sqrt(abs(iksy + igreki))
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
    new.reverse()  # moze sie okaze nie trzeba odwraca
    posortowane = []
    for fit, droga in new:
        posortowane.append(droga)
    # print posortowane
    # print ocena
    propa = get_probability_list(ocena)
    # print propa

    return roulette_wheel_pop(posortowane, propa, 30)


def krzyzowanie(populacja, pocz):
    pocz = bin(pocz)
    po_krzyzowce = []
    cr = random.random()
    for osobnik in populacja:
        po_krzyzowce.append(osobnik)
        if cr > 0.6:
            matka = random.choice(populacja)[1:len(osobnik) - 1]

            syn = [pocz]
            punkt_podzialu = random.randint(1, len(osobnik) - 1)
            syn.extend(osobnik[1:punkt_podzialu])
            for gen in matka:
                if gen not in syn:
                    syn.extend([gen])
            syn.extend([pocz])
            po_krzyzowce.append(syn)

            # corka =[pocz]
            #
            # corka.extend(matka[1:punkt_podzialu])
            # for gen in osobnik:
            #     if gen not in corka:
            #         corka.extend([gen])
            # corka.extend([pocz])
            # po_krzyzowce.append(corka)

            # corka.extend(matka[punkt_podzialu:len(osobnik)])
            # for gen in osobnik:
            #     if gen not in corka:
            #         corka.extend([gen])
            # corka.extend([pocz])
            # po_krzyzowce.append(corka)
    # for i in po_krzyzowce:
    #     print i
    return po_krzyzowce


def mutacja(populacja, ile_miast):
    for osobnik in populacja:
        for ind, wartosc in enumerate(osobnik):
            if 0.1 > random.random():
                if ind != 0 and ind != len(osobnik):
                    mut = random.randint(1, ile_miast-1)
                    osobnik[ind] = bin(mut)
    return populacja

# def create_global_variable():
global miasta
miasta = []


# create_global_variable()

def genetyk(ile_miast, poczatek, ile_populacji):
    pop_start = generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji)
    # print(pop_start)
    # miasta = []
    for i in range(ile_miast):
        miasta.append(Miasto())
    ocena = ocen(pop_start, miasta)
    print ocena
    # selekcja
    po_selekcji = selekcja(pop_start, ocena)
    # print po_selekcji

    # krzyzowanie
    po_krzyzowaniu = krzyzowanie(po_selekcji, poczatek)

    # mutacja

    po_mutacji = mutacja(po_krzyzowaniu, ile_miast)
    ocena = ocen(po_mutacji, miasta)

    i = 0
    while i < 999:

        po_selekcji = selekcja(po_mutacji, ocena)
        po_krzyzowaniu = krzyzowanie(po_selekcji, poczatek)
        po_mutacji = mutacja(po_krzyzowaniu, ile_miast)
        ocena = ocen(po_mutacji, miasta)


        i += 1
    print selekcja(po_mutacji, ocena)


# ile_miast, poczatek, ile_populacji
genetyk(20, 0, 40)

from nowy_genetyk import Gra

if __name__ == '__main__':
    g = Gra(miasta)


