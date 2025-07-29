INVALID_SOLUTION_SCORE = 0


def evaluate_fitness(individual, items, capacity):
    if not (len(individual) == len(items)):
        raise ValueError("Input lists must have the same length.")
    total_weight = 0
    total_value = 0
    for index, gene in enumerate(individual):
        if gene == 1:
            total_value += items[index][0]
            total_weight += items[index][1]

    if total_weight > capacity:
        return INVALID_SOLUTION_SCORE
    return total_value
