import random

populacja = [0, 1, 2]

fitnes = [1293.6014467429875, 1180.121633177069, 1362.1011954110897]

fitnes.sort(key=lambda b: -b)

random.seed(0)

print fitnes


def get_probability_list(fitnes):
    fitness = fitnes
    total_fit = float(sum(fitness))
    relative_fitness = [f / total_fit for f in fitness]
    probabilities = [sum(relative_fitness[:i + 1])
                     for i in range(len(relative_fitness))]
    return probabilities


propa = get_probability_list(fitnes)


def roulette_wheel_pop(population, probabilities, number):
    chosen = []
    for n in range(number):
        r = random.random()
        for (i, individual) in enumerate(population):
            if r <= probabilities[i]:
                chosen.append(individual)
                break
    return chosen


print roulette_wheel_pop(populacja, propa, 6)
