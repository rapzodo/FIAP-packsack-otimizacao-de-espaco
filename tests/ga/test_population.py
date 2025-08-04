import pytest
from ga.population import create_population, create_individual, POPULATION_SIZE


def test_create_individual_with_items():
    items = [(10, 2), (20, 5), (15, 3)]
    individual = create_individual(items)
    assert len(individual) == 3
    assert all(gene in [0, 1] for gene in individual)


def test_create_individual_empty_items():
    items = []
    individual = create_individual(items)
    assert individual == []


def test_create_population_valid_items():
    items = [(10, 2), (20, 5), (15, 3)]
    population = create_population(items)
    assert len(population) == POPULATION_SIZE
    for individual in population:
        assert len(individual) == len(items)
        assert all(gene in [0, 1] for gene in individual)


def test_create_population_empty_items_raises():
    with pytest.raises(ValueError, match="Input list must have values."):
        create_population([])
