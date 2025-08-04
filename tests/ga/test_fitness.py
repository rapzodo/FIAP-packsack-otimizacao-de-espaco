import pytest
from ga.fitness import evaluate_fitness, INVALID_SOLUTION_SCORE, Item


def test_valid_solution_within_capacity():
    individual = [1, 0, 1]
    items = [Item(10, 2), Item(20, 5), Item(15, 3)]
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
    items = [Item(10, 2)]
    capacity = 10
    with pytest.raises(ValueError):
        evaluate_fitness(individual, items, capacity)


def test_all_items_selected_within_capacity():
    individual = [1, 1, 1]
    items = [Item(5, 2), Item(10, 3), Item(8, 1)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == 23


def test_no_items_selected():
    individual = [0, 0, 0]
    items = [Item(10, 2), Item(20, 5), Item(15, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_large_values_and_weights():
    individual = [1, 0, 1]
    items = [Item(1000, 50), Item(500, 100), Item(2000, 75)]
    capacity = 150
    assert evaluate_fitness(individual, items, capacity) == 3000


def test_single_item_scenarios():
    individual = [1]
    items = [Item(25, 5)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == 25

    individual = [1]
    items = [Item(25, 15)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

    individual = [0]
    items = [Item(25, 5)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_negative_values_or_weights():
    individual = [1, 1]
    items = [Item(-5, 2), Item(10, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

    individual = [1, 1]
    items = [Item(10, -2), Item(5, 3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE

    individual = [1, 1]
    items = [Item(-10, -2), Item(-5, -3)]
    capacity = 10
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_zero_capacity():
    individual = [0, 0]
    items = [Item(10, 1), Item(5, 1)]
    capacity = 0
    assert evaluate_fitness(individual, items, capacity) == INVALID_SOLUTION_SCORE


def test_item_class_functionality():
    item = Item(15, 8)
    assert item.value == 15
    assert item.weight == 8
    assert str(item) == "Item(value=15, weight=8)"


def test_fitness_with_mixed_selection():
    individual = [1, 0, 1, 0, 1]
    items = [Item(10, 2), Item(5, 8), Item(20, 4), Item(15, 6), Item(8, 3)]
    capacity = 12
    assert evaluate_fitness(individual, items, capacity) == 38
