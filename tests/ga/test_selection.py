import pytest
from ga.fitness import Item
from ga.selection import tournament_selection, roulette_selection


def test_tournament_selection_basic():
    population = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0]]
    fitness_scores = [10, 15, 20, 5]
    tournament_size = 2

    selected = tournament_selection(population, fitness_scores, tournament_size)

    assert selected in population
    assert all(gene in [0, 1] for gene in selected)

def test_tournament_selection_best_always_wins():
    population = [[1, 0], [0, 1], [1, 1], [0, 0]]
    fitness_scores = [5, 10, 20, 2]

    best_individual = [1, 1]
    selections = []

    for _ in range(20):
        selected = tournament_selection(population, fitness_scores, tournament_size=4)
        selections.append(selected)

    assert all(sel == best_individual for sel in selections)

def test_tournament_selection_different_sizes():
    population = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0], [1, 0, 0]]
    fitness_scores = [10, 15, 25, 5, 8]

    for size in [1, 2, 3, 4, 5]:
        selected = tournament_selection(population, fitness_scores, size)
        assert selected in population

def test_tournament_selection_single_tournament():
    population = [[1, 0], [0, 1], [1, 1]]
    fitness_scores = [10, 15, 20]

    selected = tournament_selection(population, fitness_scores, tournament_size=1)
    assert selected in population

def test_tournament_selection_bias_toward_higher_fitness():
    population = [[0, 0], [1, 1]]
    fitness_scores = [1, 100]

    selections = []
    for _ in range(100):
        selected = tournament_selection(population, fitness_scores, tournament_size=2)
        selections.append(tuple(selected))

    better_individual_count = sum(1 for sel in selections if sel == (1, 1))
    assert better_individual_count > 70

def test_roulette_selection_basic():
    population = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 0]]
    fitness_scores = [10, 15, 20, 5]

    selected = roulette_selection(population, fitness_scores)

    assert selected in population
    assert all(gene in [0, 1] for gene in selected)

def test_roulette_selection_zero_fitness():
    population = [[1, 0], [0, 1]]
    fitness_scores = [0, 0]

    with pytest.raises(ValueError, match="O fitness total deve ser positivo"):
        roulette_selection(population, fitness_scores)

def test_roulette_selection_bias_toward_higher_fitness():
    population = [[0, 0], [1, 1]]
    fitness_scores = [1, 99]

    selections = []
    for _ in range(1000):
        selected = roulette_selection(population, fitness_scores)
        selections.append(tuple(selected))

    better_individual_count = sum(1 for sel in selections if sel == (1, 1))
    assert better_individual_count > 950

def test_roulette_selection_equal_fitness():
    population = [[1, 0], [0, 1], [1, 1], [0, 0]]
    fitness_scores = [10, 10, 10, 10]

    selections = []
    for _ in range(100):
        selected = roulette_selection(population, fitness_scores)
        selections.append(tuple(selected))

    unique_selections = set(selections)
    assert len(unique_selections) > 1

def test_roulette_selection_single_individual():
    population = [[1, 0, 1]]
    fitness_scores = [15]

    selected = roulette_selection(population, fitness_scores)
    assert selected == [1, 0, 1]

def test_selection_functions_preserve_individuals():
    original_population = [[1, 0, 1], [0, 1, 0], [1, 1, 1]]
    population_copy = [ind.copy() for ind in original_population]
    fitness_scores = [10, 15, 20]

    tournament_selection(population_copy, fitness_scores, 2)
    assert population_copy == original_population

    roulette_selection(population_copy, fitness_scores)
    assert population_copy == original_population

def test_selection_with_negative_fitness():
    population = [[1, 0], [0, 1], [1, 1]]
    fitness_scores = [-5, 0, 10]

    selected = tournament_selection(population, fitness_scores, 2)
    assert selected in population

    negative_fitness_scores = [-5, -3, -1]
    with pytest.raises(ValueError):
        roulette_selection(population, negative_fitness_scores)

def test_tournament_selection_large_population():
    population = [[i % 2, (i+1) % 2] for i in range(100)]
    fitness_scores = list(range(100))

    selected = tournament_selection(population, fitness_scores, 10)
    assert selected in population

def test_selection_functions_return_copies():
    population = [[1, 0, 1], [0, 1, 0]]
    fitness_scores = [10, 15]

    selected1 = tournament_selection(population, fitness_scores, 2)
    selected1[0] = 1 - selected1[0]

    selected2 = tournament_selection(population, fitness_scores, 2)
    assert population[0] == [1, 0, 1]
    assert population[1] == [0, 1, 0]

def test_fitness_scores_length_mismatch():
    population = [[1, 0], [0, 1], [1, 1]]
    fitness_scores = [10, 15]

    selected = tournament_selection(population, fitness_scores, 2)
    assert selected in population[:2]
