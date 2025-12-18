# ------------------------------------------------------------------------------+
#   @file GA.py
#   @author Class 2019.1 - Otimização Bioinspirada
#   @name Genetical Algoritm (GA) with Python
#   @date June, 2019
#   @copyright Copyright (c) IC 2019
# ------------------------------------------------------------------------------+

import random
import numpy as np

def log(population, populationFitness, current_ite):
    maxFitness_index = 0
    for i in range(1, len(populationFitness)):
        if populationFitness[i] > populationFitness[maxFitness_index]:
            maxFitness_index = i
    print(
    '#', current_ite, ' Best fitness = ', -1 * populationFitness[maxFitness_index], '  ', population[maxFitness_index])
    return


def initialPopulation(populationSize, upperBound, lowerBound):
    population = []
    numberVar = len(upperBound)
    for i in range(populationSize):
        individual = []
        for v in range(numberVar):
            individual.append(random.randint(lowerBound[v] * 100, upperBound[v] * 100))
        population.append(individual)
    return population


'''
FUNCTIONS
'''


def sphere(individual):
    y = -1 * sum(map(lambda var: (var / 100.0) ** 2, individual))
    return y


def rastringin(individual, dimension):
    y = dimension * len(individual) + sum(
        map(lambda var: (var / 100.0) ** 2 - dimension * np.cos(2 * np.pi * var), individual))
    return -1 * y


def avalFitness(population, fitnessFunction):
    populationFitness = []
    for individual in population:
        if fitnessFunction == "Sphere":
            populationFitness.append(sphere(individual))
        elif fitnessFunction == "Rastrigin":
            populationFitness.append(rastringin(individual, 3))
    return populationFitness


# selecao de parentes - eletisa
def parents_selection(population, populationFitness, population_size):
    parents = []
    templist = []

    for i in range(len(population)):
        templist.append([population[i], populationFitness[i]])

    lst = [item[0] for item in templist[0:population_size]]

    i = 0
    while i <= int(len(lst) / 2):
        parents.append([lst[i], lst[i + 1]])
        parents.append([lst[i + 1], lst[i]])
        i += 2

    return parents


# selecao da população - elitista
def population_selection(population, offspring, populationFitness, offspringFitness, population_size):
    templist = []
    for i in range(len(population)):
        templist.append([population[i], populationFitness[i]])

    for i in range(len(offspring)):
        templist.append([offspring[i], offspringFitness[i]])

    templist = sorted(templist, key=lambda x: x[1], reverse=True)
    lst2 = [item[0] for item in templist[0:population_size]]
    return lst2  # retorna metade da populacao merged(pai, filhos)


def individual_code(individual):
    code = ''
    for x in individual:
        diff = 18 - len((bin(x)))  # diferenca de bits #16 bits - (x bits - 2) #2 => 0b
        code = code + ('0' * diff) + bin(x)[2:]
    return code


def code_individual(code):
    individual = []
    dimension = len(code) / 16
    for i in range(int(dimension)):
        individual.append(int('0b' + code[i * 16:(i * 16) + 16], 2))

    return individual


def crossover(parents, crossoverChance, mutationProb):
    offsprings = []

    for pair in parents:
        if (random.random() <= crossoverChance):
            code_parent1 = individual_code(pair[0])
            code_parent2 = individual_code(pair[1])

            # n_bits = len(code_parents)
            n_bits = len(parents)
            breakpoint1 = random.randint(1, n_bits - 3)
            breakpoint2 = random.randint(breakpoint1, n_bits - 2)

            code_offspring = code_parent1[:breakpoint1] + code_parent2[breakpoint1:breakpoint2] + code_parent1[
                                                                                                  breakpoint2:]
            offspring_mutation = mutation(code_offspring, mutationProb)

            offspring = code_individual(offspring_mutation)

        offsprings.append(offspring)
    return offsprings


def mutation(code, mutationProb):
    offspring = ''
    for bit in code:
        if random.random() <= mutationProb:
            if bit == '0':
                offspring += '1'
            else:
                offspring += '0'
        else:
            offspring += bit
    return offspring


def GA(upperBound, lowerBound, max_iterations=200, crossoverProb=0.8, mutationProb=0.1, populationSize=50,
       fitnessFunction="Sphere"):
    # gerar populacao inicial
    population = initialPopulation(populationSize, upperBound, lowerBound)
    current_iteration = 0
    while (current_iteration < max_iterations):
        # avaliar o fitness
        populationFitness = avalFitness(population, fitnessFunction)
        # selecao dos pais
        parents = parents_selection(population, populationFitness,
                                    populationSize)  # parents =  <<parent1,parent2>, <parent1,parent2>>
        # cruzamento
        offspring = crossover(parents, crossoverProb, mutationProb)
        offspringFitness = avalFitness(offspring, fitnessFunction)
        # selecao da proxima geracao
        population = population_selection(population, offspring, populationFitness, offspringFitness, populationSize)

        log(population, populationFitness, current_iteration)
        current_iteration += 1
    return


upperBound = []
lowerBound = []
for i in range(3):
    upperBound.append(5)
    lowerBound.append(-5)

GA(upperBound, lowerBound)
