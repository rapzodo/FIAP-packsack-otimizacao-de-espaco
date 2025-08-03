import pytest
from ga.fitness import evaluate_fitness, INVALID_SOLUTION_SCORE


def test_valid_solution_within_capacity():
    individual = [1, 0, 1]
    items = [(10, 2), (20, 5), (15, 3)]
    capacity = 6
    assert evaluate_fitness(individual, items, capacity) == 25


def test_solution_exceeds_capacity():
    individual = [1, 1, 1]
    items = [(10, 4), (15, 5), (20, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_empty_individual():
    individual = []
    items = []
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_valid_solution_exact_capacity():
    individual = [1, 0, 1]
    items = [(30, 5), (0, 8), (25, 5)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == 55


def test_partial_selection_exceeds_capacity():
    individual = [1, 1, 0]
    items = [(10, 4), (40, 8), (5, 2)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_items_with_zero_value():
    individual = [1, 1]
    items = [(0, 2), (0, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_inconsistent_lengths():
    individual = [1, 0]
    items = [(10, 2)]
    capacity = 10
    with pytest.raises(ValueError):
        evaluate_fitness(individual, items, capacity)
