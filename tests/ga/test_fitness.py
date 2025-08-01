import pytest

from src.ga.fitness import evaluate_fitness, INVALID_SOLUTION_SCORE, Item


def test_valid_solution_within_capacity():
    individual = [1, 0, 1]
    items = [Item(10, 2), Item(20, 5), Item(15, 3)]  # (value, weight) tuples
    capacity = 6
    assert evaluate_fitness(individual, items, capacity) == 25


def test_solution_exceeds_capacity():
    individual = [1, 1, 1]
    items = [Item(10, 4), Item(15, 5), Item(20, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

def test_empty_individual():
    individual = []
    items = []
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

def test_valid_solution_exact_capacity():
    individual = [1, 0, 1]
    items = [Item(30, 5), Item(0, 8), Item(25, 5)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == 55

def test_partial_selection_exceeds_capacity():
    individual = [1, 1, 0]
    items = [Item(10, 4), Item(40, 8), Item(5, 2)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

def test_items_with_zero_value():
    individual = [1, 1]
    items = [Item(0, 2), Item(0, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

def test_inconsistent_lengths():
    individual = [1, 0]
    items = [Item(10, 2)]  # Only one item but individual has 2 genes
    capacity = 10
    with pytest.raises(ValueError):
        evaluate_fitness(individual, items, capacity)
