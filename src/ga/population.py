import random

POPULATION_SIZE = 50


def create_population(items):
    if not items:
        raise ValueError("Input list must have values.")
    return [create_individual(items) for _ in range(POPULATION_SIZE)]


def create_individual(items):
    return [random.randint(0, 1) for _ in items]
