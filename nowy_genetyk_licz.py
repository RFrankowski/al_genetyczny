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

    return roulette_wheel_pop(posortowane, propa, 10)


def krzyzowanie(populacja):
    po_krzyzowce = []
    cr = random.random()
    for osobnik in populacja:
        po_krzyzowce.append(osobnik)
        if cr > 0.6:
            syn = []
            corka = []
            punkt_podzialu = random.randint(1, len(osobnik) - 1)


            # matka = random.choice(populacja)
            # syn.extend(osobnik[:punkt_podzialu])
            # syn.extend(matka[punkt_podzialu:])
            # po_krzyzowce.append(syn)
            # corka.extend(osobnik[punkt_podzialu:])
            # corka.extend(matka[:punkt_podzialu])
            # po_krzyzowce.append(corka)
    print po_krzyzowce




def genetyk(ile_miast, poczatek, ile_populacji):
    pop_start = generuj_populacjie_starowa(ile_miast, poczatek, ile_populacji)
    # print(pop_start)
    miasta = []
    for i in range(ile_miast):
        miasta.append(Miasto())
    ocena = ocen(pop_start, miasta)
    # selekcja
    po_selekcji = selekcja(pop_start, ocena)
    print po_selekcji

    # krzyzowanie
    krzyzowanie(po_selekcji)

    # mutacja


# ile_miast, poczatek, ile_populacji
genetyk(5, 0, 10)
