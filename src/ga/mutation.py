import random


class Mutation:
    @staticmethod
    def bit_flip(individual, mutation_rate):
        """Bit flip mutation for binary individuals."""
        mutated = individual[:]
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = 1 - mutated[i]
        return mutated