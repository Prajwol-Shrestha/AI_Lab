import random
from deap import algorithms, base, creator, tools

# Problem-specific constants
TARGET = "HELLO, WORLD!"
POPULATION_SIZE = 100
GENERATIONS = 50
MUTATION_PROBABILITY = 0.1

# Define the fitness function
def evaluate_individual(individual):
    score = sum(1 for i, j in zip(individual, TARGET) if i != j)
    return score,

# Define the individual and population types
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Initialize the attributes and population
toolbox.register("attr_char", random.choice, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,!")
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_char, len(TARGET))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the genetic operators
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

toolbox.register("evaluate", evaluate_individual)

# Main evolutionary algorithm
def main():
    random.seed(42)

    population = toolbox.population(n=POPULATION_SIZE)

    # Evaluate the initial population
    fitnesses = list(map(toolbox.evaluate, population))
    for individual, fitness in zip(population, fitnesses):
        individual.fitness.values = fitness

    for generation in range(1, GENERATIONS + 1):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        
        # Evaluate the offspring
        fitnesses = list(map(toolbox.evaluate, offspring))
        for individual, fitness in zip(offspring, fitnesses):
            individual.fitness.values = fitness

        population = toolbox.select(offspring, k=len(population))

        best_individual = tools.selBest(population, k=1)[0]
        best_fitness = best_individual.fitness.values[0]
        best_phrase = ''.join(best_individual)

        print(f"Generation {generation}: Best fitness = {best_fitness}, Best phrase = {best_phrase}")

# Run the main program
if __name__ == "__main__":
    main()
