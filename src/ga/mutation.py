import random
import copy

class Mutation:
    @staticmethod
    def bit_flip(individual, mutation_rate):
        """Bit flip mutation for binary individuals."""
        mutated = individual[:]
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = 1 - mutated[i]
        return mutated

    @staticmethod
    def swap(individual, mutation_rate):
        """Swap mutation for permutation or binary individuals."""
        mutated = individual[:]
        if random.random() < mutation_rate and len(mutated) > 1:
            idx1, idx2 = random.sample(range(len(mutated)), 2)
            mutated[idx1], mutated[idx2] = mutated[idx2], mutated[idx1]
        return mutated

    @staticmethod
    def scramble(individual, mutation_rate):
        """Scramble mutation for permutation or binary individuals."""
        mutated = individual[:]
        if random.random() < mutation_rate and len(mutated) > 1:
            start, end = sorted(random.sample(range(len(mutated)), 2))
            subset = mutated[start:end]
            random.shuffle(subset)
            mutated[start:end] = subset
        return mutated

    @staticmethod
    def inversion(individual, mutation_rate):
        """Inversion mutation for permutation or binary individuals."""
        mutated = individual[:]
        if random.random() < mutation_rate and len(mutated) > 1:
            start, end = sorted(random.sample(range(len(mutated)), 2))
            mutated[start:end] = mutated[start:end][::-1]
        return mutated

    @staticmethod
    def random_resetting(individual, mutation_rate):
        """Random resetting mutation for binary individuals."""
        mutated = individual[:]
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = random.randint(0, 1)
        return mutated

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
