import math
import random
#bingung
def generateChromosome():
    #membuat satu kromosom dengan panjang 6 dan tipe data integer
    chromosome = []
    for _ in range(6):
        chromosome.append(random.randint(0, 9))

    return chromosome

def decodeX(chromosome):
    #mendekode nilai x
    bot, top = (-5, 5) #-5 <= x <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def decodeY(chromosome):
    #mendekode nilai y
    bot, top = (-5, 5) #-5 <= y <= 5

    return bot + ((top - bot)/(9 * 10**(-1) + 9 * 10**(-2)+ 9 * 10**(-3))) * (chromosome[0] * 10 ** (-1) + chromosome[1] * 10 ** (-2) + chromosome[2] * 10 ** (-3))

def fitnessFunction(chromosome):
    #menghitung nilai fitness
    x = decodeX(chromosome)
    y = decodeY(chromosome)

    return ((math.cos(x)+math.sin(y))**2) / (x**2 + y**2)

def generatePopulation(pop_size):
    #membuat populasi
    population = []
    for i in range(pop_size):
        chromosome = generateChromosome()
        population.append(chromosome)

    return population

def calculateFitness(population):
    fitness = []
    for i in range(len(population)):
        fitness_temp = fitnessFunction(population[i])
        fitness.append(fitness_temp)

    return fitness

def fitnessSort(population):
    fitness = calculateFitness(population)
    pas = 1
    while pas < len(population):
        idx = pas - 1
        i = pas
        while i < len(population):
            if fitness[idx] > fitness[i]:
                idx = i
            i += 1
        temp = population[pas-1]
        temp_fit = fitness[pas-1]
        population[pas-1] = population[idx]
        fitness[pas-1] = fitness[idx]
        population[idx] = temp
        fitness[idx] = temp_fit
        pas += 1

    return population

def getElitism(population):
    elitism = []
    for i in range(30):
        elitism.append(population[i])
    
    return elitism

def parentSelection(population):
    parent = []
    for i in range(20, 90):
        parent.append(population[i])

    return parent

def matingPool(parent):
    pasangan = []
    for i in range(len(parent)//2):
        pasangan_temp = []
        p1 = 0
        p2 = random.randint(1, (len(parent)-1))
        pasangan_temp.append(parent[p1])
        pasangan_temp.append(parent[p2])
        pasangan.append(pasangan_temp)
        parent.pop(p2); parent.pop(p1)
    
    print(pasangan)
    return pasangan

def crossover(p1, p2, pc):
    r = random.uniform(0, 1)
    if r < pc:
        t = random.randint(1, 4)
        c1 = p1[0:t], p2[t:5]
        c2 = p2[0:t], p1[t:5]
    else:
        c1 = p1
        c2 = p2

    return [c1, c2]

def mutation(child, pm):
    r = random.uniform(0, 1)
    if r < pm:
        child[0][random.randint(0,5)] = random.randint(0, 9)
        child[1][random.randint(0,5)] = random.randint(0, 9)
    
    return child

def generationalReplacement(pop_size, pc, pm, generation):
    popu = generatePopulation(pop_size)
    for i in range(generation):
        fitness = calculateFitness(popu)
        fitnessSort(popu)
        newPopu = getElitism(popu)
        parent = parentSelection(popu)
        i = 0
        while len(newPopu) < pop_size:
            pasangan = matingPool(parent)
            
            offspring = crossover(p1, p2, pc)
            offspring = mutation(offspring, pm)
            newPopu.append(offspring[i][0])
            newPopu.append(offspring[i][1])
            i += 1
        popu = newPopu
        fitness = calculateFitness(popu)

    return popu, fitness

def printHasil():
    pop_size = 100; pc = 0.65; pm = 0.04; generation = 100
    gen = generationalReplacement(pop_size, pc, pm, generation)
    best_chrom = gen[0][0]
    best_fitness = gen[1][0]
    nilaiX = decodeX(best_chrom)
    nilaiY = decodeY(best_chrom)
    print("-------------------------------------------------------------\n")
    print("Kromosom terbaik\t\t: ", best_chrom)
    print("Nilai fitness terbaik\t:", best_fitness)
    print("Nilai x \t\t=", nilaiX)
    print("Nilai y \t\t=", nilaiY)
    print("Jumlah generasi \t:", generation)

        
printHasil()
