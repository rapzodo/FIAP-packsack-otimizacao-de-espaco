import random


def single_point_crossover(parent1, parent2):
    """
    Perform single-point crossover between two parents.
    Args:
        parent1: binary list representing first parent
        parent2: binary list representing second parent
    Returns:
        tuple of two children
    """
    if len(parent1) != len(parent2):
        raise ValueError("Parents must have the same length")

    if len(parent1) <= 1:
        return parent1.copy(), parent2.copy()

    crossover_point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def uniform_crossover(parent1, parent2, prob=0.5):
    """
    Perform uniform crossover between two parents.
    Args:
        parent1: binary list representing first parent
        parent2: binary list representing second parent
        prob: probability of inheriting from parent1
    Returns:
        tuple of two children
    """
    if len(parent1) != len(parent2):
        raise ValueError("Parents must have the same length")

    child1 = []
    child2 = []

    for i in range(len(parent1)):
        if random.random() < prob:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return child1, child2
