import pytest
from ga.population import create_population, create_individual, POPULATION_SIZE
from ga.fitness import Item


class TestPopulation:
    def test_create_individual_basic(self):
        items = [Item(10, 5), Item(20, 10), Item(15, 8)]
        individual = create_individual(items)

        assert len(individual) == len(items)
        assert all(gene in [0, 1] for gene in individual)

    def test_create_individual_empty_items(self):
        items = []
        individual = create_individual(items)
        assert individual == []

    def test_create_individual_single_item(self):
        items = [Item(5, 3)]
        individual = create_individual(items)

        assert len(individual) == 1
        assert individual[0] in [0, 1]

    def test_create_individual_multiple_calls_different_results(self):
        items = [Item(10, 5) for _ in range(20)]
        individuals = [create_individual(items) for _ in range(10)]
        unique_individuals = set(tuple(ind) for ind in individuals)
        assert len(unique_individuals) > 1

    def test_create_population_basic(self):
        items = [Item(10, 5), Item(20, 10), Item(15, 8)]
        population = create_population(items)

        assert len(population) == POPULATION_SIZE
        for individual in population:
            assert len(individual) == len(items)
            assert all(gene in [0, 1] for gene in individual)

    def test_create_population_empty_items(self):
        items = []
        with pytest.raises(ValueError, match="Input list must have values"):
            create_population(items)

    def test_create_population_none_items(self):
        with pytest.raises(ValueError, match="Input list must have values"):
            create_population(None)

    def test_create_population_diversity(self):
        items = [Item(i, i+1) for i in range(10)]
        population = create_population(items)
        unique_individuals = set(tuple(ind) for ind in population)
        diversity_ratio = len(unique_individuals) / len(population)
        assert diversity_ratio > 0.7

    def test_create_population_large_items(self):
        items = [Item(i, i+1) for i in range(100)]
        population = create_population(items)

        assert len(population) == POPULATION_SIZE
        for individual in population:
            assert len(individual) == 100
            assert all(gene in [0, 1] for gene in individual)

    def test_population_size_constant(self):
        assert isinstance(POPULATION_SIZE, int)
        assert POPULATION_SIZE > 0
        assert POPULATION_SIZE <= 1000

    def test_create_population_with_different_item_types(self):
        items = [Item(0, 1), Item(1, 0), Item(0, 0), Item(10, 5)]
        population = create_population(items)

        assert len(population) == POPULATION_SIZE
        for individual in population:
            assert len(individual) == len(items)

    def test_individual_randomness_distribution(self):
        items = [Item(i, i+1) for i in range(100)]

        total_ones = 0
        total_genes = 0
        num_individuals = 100

        for _ in range(num_individuals):
            individual = create_individual(items)
            total_ones += sum(individual)
            total_genes += len(individual)

        ones_ratio = total_ones / total_genes
        assert 0.4 <= ones_ratio <= 0.6

    def test_create_population_returns_new_instances(self):
        items = [Item(10, 5), Item(20, 10)]

        pop1 = create_population(items)
        pop2 = create_population(items)

        assert pop1 is not pop2
        for i in range(len(pop1)):
            assert pop1[i] is not pop2[i]
