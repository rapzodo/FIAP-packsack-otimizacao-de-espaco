import random


def bit_flip_mutation(individual, mutation_rate):
    """
    Perform bit-flip mutation on an individual.
    Args:
        individual: binary list representing an individual
        mutation_rate: probability of flipping each bit
    Returns:
        mutated individual
    """
    mutated = individual.copy()

    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = 1 - mutated[i]  # Flip bit (0->1, 1->0)

    return mutated


def random_reset_mutation(individual, mutation_rate):
    """
    Perform random reset mutation on an individual.
    Args:
        individual: binary list representing an individual
        mutation_rate: probability of resetting each bit
    Returns:
        mutated individual
    """
    mutated = individual.copy()

    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = random.randint(0, 1)

    return mutated
