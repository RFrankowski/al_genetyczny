#! /usr/bin/env python2
# -*- coding: utf-8 -*-
import random
from random import choice
import graphviz as gv
from PIL import Image

graf = [['a', 'b', 3], ['a', 'e', 3], ['c', 'd', 3], ['c', 'f', 1], ['b', 'd', 3], ['e', 'f', 2], ['f', 'a', 6],
        ['f', 'd', 1], ['b', 'c', 1]]

text = open('graf_test.txt').read()
text = text.replace('\n', ',')
text = list(text.split(','))
graf = []
for i in range(0, len(text) - 2, 2):
    if len(graf) < 150:
        krawedz = []
        krawedz.append(text[i])
        krawedz.append(text[i + 1])
        graf.append(krawedz)

styles = {
    'graph': {
        'label': 'graf',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'oval',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '10',
        'fontcolor': 'white',
    }
}


def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {})
    return graph


def rys_alg_gen_rozw(wektor, graph):
    g1 = gv.Graph(format='jpg')
    wierzcho = wszystkie_wierzch(graph)
    wierzcho = sorted(wierzcho)
    for w in enumerate(wierzcho):
        g1.node(w[1], label="{} kolor = {}".format(w[1], wektor[w[0]]))
    for pocz, kon in graph:
        g1.edge(pocz, kon)
    g1 = apply_styles(g1, styles)
    filename = g1.render(filename='img/g1')
    img = Image.open('C:/Users/admin/Desktop/projektowanie_ekekty/Nowy/Nowy/img/g1.jpg')
    img.show()
    img.close()


def znajdz_sasiadow(graph, sourc):
    sasiedzi = []
    for krawedz in graph:
        i, j = krawedz
        if (i in sourc) or (j in sourc):
            if i == sourc:
                sasiedzi.append(j)
            elif j == sourc:
                sasiedzi.append(i)
    return sasiedzi


def wszystkie_wierzch(graph):
    wierzch = []
    for i, j in graph:
        if i not in wierzch:
            wierzch.append(i)
        if j not in wierzch:
            wierzch.append(j)
    return sorted(wierzch)


def generacja_populacji(liczba_pop, ile_wierzch, ile_kolorow):
    kolory = []
    populacja = []
    genotyp = []
    for i in range(0,
                   int(ile_kolorow)):
        kolory.append(i)
    for p in range(0, liczba_pop):
        for w in range(0, ile_wierzch):
            genotyp.append(choice(kolory))
        populacja.append(genotyp)
        genotyp = []
    return populacja


def ile_zlych(graph, wierzch, populacja):
    wierzchy = wszystkie_wierzch(graph)
    sasiadzi = znajdz_sasiadow(graph, wierzch)
    bledne_pokolorowania = 0

    for s in sasiadzi:

        if populacja[wierzchy.index(wierzch)] == populacja[wierzchy.index(s)]:
            bledne_pokolorowania += 1
    return bledne_pokolorowania


def ewaluacjia(pop_start, graph):
    ile_zle = []
    wierzchy = wszystkie_wierzch(graph)
    for p in pop_start:
        suma_zych = 0
        for w in enumerate(p):
            zle_pokolorwania = ile_zlych(graph, wierzchy[w[0]], p)
            suma_zych += zle_pokolorwania
        ile_zle.append((p, suma_zych))
    return ile_zle


def selekcja(populacjie):
    winners = []
    for i in range(0, len(populacjie), 2):
        x = []
        if len(populacjie) != 0:
            x.append(populacjie.pop(random.randint(0, len(populacjie) - 1)))
        if len(populacjie) != 0:
            x.append(populacjie.pop(random.randint(0, len(populacjie) - 1)))
        if len(x) != 0:
            x = sorted(x, key=lambda blad: blad[1])
            winners.append(x[0][0])
    print 'liczba polulacji po selekcji %d' % (len(winners))
    return winners


global szansa_na_sex
szansa_na_sex = 0.55


def sex(pop_po_selekcji, wielkosc_pop):
    global szansa_na_sex
    po_krzyzowce = []
    for ojciec in pop_po_selekcji:
        r = random.random()
        po_krzyzowce.append(ojciec)
        syn = []
        corka = []
        if r > szansa_na_sex:
            punkt_podzialu = random.randint(1, len(pop_po_selekcji[0]) - 1)
            matka = random.choice(pop_po_selekcji)
            syn.extend(ojciec[:punkt_podzialu])
            syn.extend(matka[punkt_podzialu:])
            po_krzyzowce.append(syn)
            corka.extend(ojciec[punkt_podzialu:])
            corka.extend(matka[:punkt_podzialu])
            po_krzyzowce.append(corka)
    print 'liczba osobnikow po krzyzowce %d' % (len(po_krzyzowce))
    return po_krzyzowce


def mutacja(po_sexie, ile_kolorow):
    kolory = []
    szansa_na_mutacje = 0.02
    po_mutacji = []
    for i in range(0, int(ile_kolorow)):
        kolory.append(i)
    for p in enumerate(po_sexie):
        po_mutacji.append(p[1])
        for w in enumerate(p[1]):
            szansa = random.random()
            if szansa_na_mutacje > szansa:
                x = random.choice(kolory)
                po_mutacji[p[0]][w[0]] = x
    return po_mutacji


print 'liczba wierzch = {}'.format(len(wszystkie_wierzch(graf)))


def alg_genetyczny(graph, ile_kolorow, wielkosc_populacji):
    wierzchy = wszystkie_wierzch(graph)
    global szansa_na_sex
    rozwiazanie = []
    pop_start = generacja_populacji(wielkosc_populacji, len(wierzchy), ile_kolorow)
    sprawdzone_populacje = ewaluacjia(pop_start, graph)
    warunek = 1

    for sp in sprawdzone_populacje:
        if sp[1] == 0:
            print sp
            rozwiazanie.append(sp)
    lider = sprawdzone_populacje[0]
    while warunek < 1000 and len(rozwiazanie) == 0:
        print 'nr generacji %d' % warunek
        pop_po_selekcji = selekcja(sprawdzone_populacje)
        po_sexie = sex(pop_po_selekcji, wielkosc_populacji)
        if len(po_sexie) < 0.9 * float(wielkosc_populacji):
            szansa_na_sex -= 0.01
        elif len(po_sexie) > 1.1 * float(wielkosc_populacji):
            szansa_na_sex += 0.02
        pop_mut = mutacja(po_sexie, ile_kolorow)
        sprawdzone_populacje = ewaluacjia(pop_mut, graph)
        najlepszy_okaz = sorted(sprawdzone_populacje, key=lambda bledy: bledy[1])[0]
        print sorted(sprawdzone_populacje, key=lambda bledy: -bledy[1])[0]
        print sorted(sprawdzone_populacje, key=lambda bledy: bledy[1])[0]
        if lider[1] > najlepszy_okaz[1]:
            lider = najlepszy_okaz
        if sorted(sprawdzone_populacje, key=lambda bledy: bledy[1])[0][1] > lider[1]:
            sprawdzone_populacje.append(lider)
        print sorted(sprawdzone_populacje, key=lambda bledy: bledy[1])[0]
        for sp in sprawdzone_populacje:
            if sp[1] == 0:
                print sp
                rozwiazanie.append(sp)
                rys_alg_gen_rozw(sp[0], graph)
                break
        warunek += 1
    if warunek > 998:
        print 'buuuu sprobuj z innymi parametrami'


alg_genetyczny(graf, 8, 100)
