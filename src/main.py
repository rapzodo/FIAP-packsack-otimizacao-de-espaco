import random
import matplotlib.pyplot as plt
from ga.fitness import evaluate_fitness, Item
from ga.population import create_population
from ga.selection import tournament_selection, roulette_selection
from ga.crossover import single_point_crossover, uniform_crossover
from ga.mutation import bit_flip_mutation

# Configuration parameters - Balanced for demonstration
NUM_ITEMS = 50  # Challenging but manageable
POPULATION_SIZE = 100  # Good diversity without performance issues
GENERATIONS = 200
MUTATION_RATE = 0.05
TOURNAMENT_SIZE = 5
ELITISM_SIZE = 5
KNAPSACK_CAPACITY = 200  # Proportional to item count

# Generate random items using Item class
items = [Item(random.randint(1, 20), random.randint(1, 15)) for _ in range(NUM_ITEMS)]


def calculate_population_fitness(population, items, capacity):
    """Calculate fitness for entire population."""
    return [evaluate_fitness(individual, items, capacity) for individual in population]


def get_best_individual(population, fitness_scores):
    """Get the individual with highest fitness."""
    best_idx = fitness_scores.index(max(fitness_scores))
    return population[best_idx], fitness_scores[best_idx]


def genetic_algorithm():
    """Main genetic algorithm implementation."""
    print("=== Knapsack Optimization with Genetic Algorithm ===")
    print(f"Items: {items}")
    print(f"Knapsack capacity: {KNAPSACK_CAPACITY}")
    print(f"Population size: {POPULATION_SIZE}")
    print(f"Generations: {GENERATIONS}")
    print(f"Mutation rate: {MUTATION_RATE}")
    print("-" * 50)

    # Initialize population
    population = create_population(items)

    # Track best solutions
    best_fitness_history = []
    avg_fitness_history = []
    best_solution = None
    best_fitness = 0

    for generation in range(GENERATIONS):
        # Calculate fitness for all individuals
        fitness_scores = calculate_population_fitness(population, items, KNAPSACK_CAPACITY)

        # Track statistics
        current_best_individual, current_best_fitness = get_best_individual(population, fitness_scores)
        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        best_fitness_history.append(current_best_fitness)
        avg_fitness_history.append(avg_fitness)

        # Update global best
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_solution = current_best_individual.copy()

        # Print progress
        if generation % 10 == 0 or generation == GENERATIONS - 1:
            print(f"Generation {generation:3d}: Best={current_best_fitness:3d}, Avg={avg_fitness:6.2f}")

        # Create new population
        new_population = []

        # Elitism: keep best individuals
        sorted_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)
        for i in range(ELITISM_SIZE):
            new_population.append(population[sorted_indices[i]].copy())

        # Generate rest of population through selection, crossover, and mutation
        while len(new_population) < POPULATION_SIZE:
            # Selection
            if sum(fitness_scores) > 0:
                parent1 = tournament_selection(population, fitness_scores, TOURNAMENT_SIZE)
                parent2 = tournament_selection(population, fitness_scores, TOURNAMENT_SIZE)
            else:
                # Fallback to random selection if all fitness scores are 0
                parent1 = random.choice(population)
                parent2 = random.choice(population)

            # Crossover
            child1, child2 = single_point_crossover(parent1, parent2)

            # Mutation
            child1 = bit_flip_mutation(child1, MUTATION_RATE)
            child2 = bit_flip_mutation(child2, MUTATION_RATE)

            # Add children to new population
            new_population.extend([child1, child2])

        # Trim population to exact size
        population = new_population[:POPULATION_SIZE]

    return best_solution, best_fitness, best_fitness_history, avg_fitness_history


def display_results(best_solution, best_fitness, best_fitness_history, avg_fitness_history):
    """Display the results of the genetic algorithm."""
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)

    print(f"Best fitness achieved: {best_fitness}")
    print(f"Best solution: {best_solution}")

    # Calculate solution details using Item class attributes
    total_weight = sum(items[i].weight for i, gene in enumerate(best_solution) if gene == 1)
    selected_items = [(i, items[i]) for i, gene in enumerate(best_solution) if gene == 1]

    print(f"Total weight: {total_weight}/{KNAPSACK_CAPACITY}")
    print(f"Weight utilization: {(total_weight/KNAPSACK_CAPACITY)*100:.1f}%")
    print("\nSelected items:")
    for idx, item in selected_items:
        print(f"  Item {idx}: {item}")

    # Plot fitness evolution
    plt.figure(figsize=(10, 6))
    plt.plot(best_fitness_history, label='Best Fitness', linewidth=2)
    plt.plot(avg_fitness_history, label='Average Fitness', linewidth=2)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Genetic Algorithm Evolution - Knapsack Problem')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def main():
    """Main execution function."""
    try:
        best_solution, best_fitness, best_fitness_history, avg_fitness_history = genetic_algorithm()
        display_results(best_solution, best_fitness, best_fitness_history, avg_fitness_history)
    except Exception as e:
        print(f"Error during execution: {e}")
        raise


if __name__ == "__main__":
    main()
