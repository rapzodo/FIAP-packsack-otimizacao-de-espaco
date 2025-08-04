import pytest
from ga.crossover import Crossover


class TestCrossover:
    def test_crossover_class_one_point_basic(self):
        parent1 = [1, 0, 1, 0, 1]
        parent2 = [0, 1, 0, 1, 0]

        child1, child2 = Crossover.one_point(parent1, parent2)

        assert len(child1) == len(parent1)
        assert len(child2) == len(parent2)
        assert all(gene in [0, 1] for gene in child1)
        assert all(gene in [0, 1] for gene in child2)

    def test_crossover_class_one_point_preserves_genetic_material(self):
        parent1 = [1, 1, 1, 1, 1]
        parent2 = [0, 0, 0, 0, 0]

        child1, child2 = Crossover.one_point(parent1, parent2)

        assert 0 in child1 and 1 in child1
        assert 0 in child2 and 1 in child2

    def test_crossover_class_one_point_empty_parents(self):
        parent1 = []
        parent2 = []

        try:
            child1, child2 = Crossover.one_point(parent1, parent2)
            assert child1 == []
            assert child2 == []
        except (ValueError, IndexError):
            pass

    def test_crossover_class_one_point_single_gene(self):
        parent1 = [1]
        parent2 = [0]

        try:
            child1, child2 = Crossover.one_point(parent1, parent2)
            assert len(child1) == 1
            assert len(child2) == 1
            assert child1[0] in [0, 1]
            assert child2[0] in [0, 1]
        except (ValueError, IndexError):
            pass

    def test_crossover_class_preserves_originals(self):
        parent1 = [1, 0, 1, 0, 1]
        parent2 = [0, 1, 0, 1, 0]
        parent1_copy = parent1.copy()
        parent2_copy = parent2.copy()

        Crossover.one_point(parent1, parent2)

        assert parent1 == parent1_copy
        assert parent2 == parent2_copy

    def test_crossover_class_produces_variation(self):
        parent1 = [1, 0, 1, 0, 1, 0, 1, 0]
        parent2 = [0, 1, 0, 1, 0, 1, 0, 1]

        results = []
        for _ in range(20):
            child1, child2 = Crossover.one_point(parent1, parent2)
            results.append((tuple(child1), tuple(child2)))

        unique_results = set(results)
        assert len(unique_results) > 1

    def test_crossover_class_one_point_different_lengths(self):
        parent1 = [1, 0, 1]
        parent2 = [0, 1]  # Different length

        child1, child2 = Crossover.one_point(parent1, parent2)

        assert isinstance(child1, list)
        assert isinstance(child2, list)
        assert all(gene in [0, 1] for gene in child1)
        assert all(gene in [0, 1] for gene in child2)

    def test_crossover_class_one_point_longer_parents(self):
        parent1 = [1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
        parent2 = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]

        child1, child2 = Crossover.one_point(parent1, parent2)

        assert len(child1) == len(parent1)
        assert len(child2) == len(parent2)
        assert all(gene in [0, 1] for gene in child1)
        assert all(gene in [0, 1] for gene in child2)
