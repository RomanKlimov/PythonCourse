import random

target = 'Roman'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '.', '?', '!', ',',
            ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

tempTarget = []
for i in target:
    tempTarget.append(i)

target = tempTarget

pop_size = 1000
population = []
mutation_rate = 10
keep_doing = True
iterations = 0
generation_number = 0
# create initial population
for i in range(pop_size):
    phrase = []
    for i in range(len(target)):
        phrase.append(alphabet[random.randint(0, len(alphabet) - 1)])
    population.append(phrase)

while keep_doing != False:

    # calculate fitnesses
    fitnesses = []

    for i in range(pop_size):
        fitness = 0
        for j in range(len(target)):
            if population[i][j] == target[j]:
                fitness += 1
        fitnesses.append(fitness)


    def crossover(a, b):
        half = round(len(target) / 2)
        c = a[0:half] + b[half:]
        return c


    def mutate(word):
        newWord = word
        for i in range(len(word)):
            if random.randint(1, 101) <= mutation_rate:
                newLetter = alphabet[random.randint(0, len(alphabet) - 1)]
                newWord = word[0:i]
                newWord.append(newLetter)
                newWord = newWord + word[i + 1:]
        return newWord


    # mating pool
    mating_pool = []
    for i in range(pop_size):
        for j in range(fitnesses[i]):
            mating_pool.append(population[i])


    def generate():
        population = []
        for i in range(pop_size):
            parentA = mating_pool[random.randint(0, len(mating_pool) - 1)]
            parentB = mating_pool[random.randint(0, len(mating_pool) - 1)]
            child = crossover(parentA, parentB)
            child = mutate(child)
            population.append(child)
        return population


    population = generate()

    # find the highest fitness
    fitnesses = []

    for i in range(pop_size):
        fitness = 0
        for j in range(len(target)):
            if population[i][j] == target[j]:
                fitness += 1
        fitnesses.append(fitness)

    highest_fitness1 = 0
    for i in range(len(fitnesses)):
        if fitnesses[highest_fitness1] < fitnesses[i]:
            highest_fitness1 = i
    s = ''.join(population[highest_fitness1])
    print("Generation number:", generation_number, s)
    generation_number += 1

    iterations += 1

    if population[highest_fitness1] == target:
        keep_doing = False
