from ga.fitness import evaluate_fitness, INVALID_SOLUTION_SCORE

def test_valid_solution_within_capacity():
    individual = [1, 0, 1]
    weights = [2, 5, 3]
    values = [10, 20, 15]
    capacity = 6
    assert evaluate_fitness(individual, weights, values, capacity) == 25

def test_solution_exceeds_capacity():
    individual = [1, 1, 1]
    weights = [4, 5, 3]
    values = [10, 15, 20]
    capacity = 10
    assert evaluate_fitness(individual, weights, values, capacity) == INVALID_SOLUTION_SCORE

def test_empty_individual():
    individual = []
    weights = []
    values = []
    capacity = 10
    assert evaluate_fitness(individual, weights, values, capacity) == INVALID_SOLUTION_SCORE

def test_valid_solution_exact_capacity():
    individual = [1, 0, 1]
    weights = [5, 8, 5]
    values = [30, 0, 25]
    capacity = 10
    assert evaluate_fitness(individual, weights, values, capacity) == 55