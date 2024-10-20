import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return 3*x + 2*y**2


def generate_population(size, bounds):
    population = np.random.uniform(low=bounds[0], high=bounds[1], size=(size, 2))
    return population


def evaluate_fitness(population):
    return func(population[:, 0], population[:, 1])


def select_parents(population, fitness, num_parents):
    parents_idx = np.argsort(fitness)[:num_parents]
    return population[parents_idx]


def crossover(parents, offspring_size):
    offspring = np.zeros(offspring_size)
    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]

        offspring[k, 0] = (parents[parent1_idx, 0] + parents[parent2_idx, 0]) / 2
        offspring[k, 1] = (parents[parent1_idx, 1] + parents[parent2_idx, 1]) / 2
    return offspring


def mutate(offspring, mutation_rate=0.1):
    for idx in range(offspring.shape[0]):
        if np.random.rand() < mutation_rate:
            random_value_x = np.random.uniform(-1.0, 1.0)
            random_value_y = np.random.uniform(-1.0, 1.0)
            offspring[idx, 0] += random_value_x
            offspring[idx, 1] += random_value_y
    return offspring


def plot_population(population, gen_num, bounds):
    plt.scatter(population[:, 0], population[:, 1], c='blue', marker='o')
    plt.xlim(bounds)
    plt.ylim(bounds)
    plt.title(f'Генерация {gen_num}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.pause(1)


def genetic_algorithm(bounds, pop_size=100, num_generations=10, num_parents=10):
    population = generate_population(pop_size, bounds)
    
    for gen in range(num_generations):
        fitness = evaluate_fitness(population)
        
        plot_population(population, gen, bounds)
        
        parents = select_parents(population, fitness, num_parents)
        offspring_size = (pop_size - parents.shape[0], 2)
        offspring = crossover(parents, offspring_size)
        offspring = mutate(offspring)
        
        population[:parents.shape[0]] = parents
        population[parents.shape[0]:] = offspring
    
    best_solution_idx = np.argmin(evaluate_fitness(population))
    best_solution = population[best_solution_idx]
    print(f'Лучшее решение: x = {best_solution[0]}, y = {best_solution[1]}, f(x, y) = {func(best_solution[0], best_solution[1])}')


bounds = [-10, 10]  # Границы поиска
genetic_algorithm(bounds)

plt.show()