INVALID_SOLUTION_SCORE = 0

def evaluate_fitness(individual, weights, values, capacity):
    total_weight = 0
    total_value = 0
    for index, gene in enumerate(individual):
        if gene == 1:
            total_weight += weights[index]
            total_value += values[index]

    if total_weight > capacity:
        return INVALID_SOLUTION_SCORE
    return total_value