INVALID_SOLUTION_SCORE = 0


def evaluate_fitness(individual, items, capacity):
    """
    Evaluate fitness for knapsack problem.
    Args:
        individual: binary list representing which items to include
        items: list of (value, weight) tuples
        capacity: maximum weight capacity of knapsack
    Returns:
        total value if within capacity, otherwise INVALID_SOLUTION_SCORE
    """
    if not (len(individual) == len(items)):
        raise ValueError("Input lists must have the same length.")

    if not individual:  # Empty individual
        return INVALID_SOLUTION_SCORE

    total_weight = 0
    total_value = 0
    for index, gene in enumerate(individual):
        if gene == 1:
            total_value += items[index][0]  # value
            total_weight += items[index][1]  # weight

    if total_weight > capacity or total_value <= 0:
        return INVALID_SOLUTION_SCORE

    return total_value
