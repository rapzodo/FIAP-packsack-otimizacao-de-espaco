import pytest
from ga.crossover import single_point_crossover, uniform_crossover


def test_single_point_crossover_basic():
    """Test basic single-point crossover functionality."""
    parent1 = [1, 0, 1, 0, 1]
    parent2 = [0, 1, 0, 1, 0]

    child1, child2 = single_point_crossover(parent1, parent2)

    # Children should have same length as parents
    assert len(child1) == len(parent1)
    assert len(child2) == len(parent2)

    # Children should contain only 0s and 1s
    assert all(gene in [0, 1] for gene in child1)
    assert all(gene in [0, 1] for gene in child2)


def test_single_point_crossover_different_lengths():
    """Test that crossover raises error for different length parents."""
    parent1 = [1, 0, 1]
    parent2 = [0, 1]

    with pytest.raises(ValueError):
        single_point_crossover(parent1, parent2)


def test_single_point_crossover_single_gene():
    """Test crossover with single gene individuals."""
    parent1 = [1]
    parent2 = [0]

    child1, child2 = single_point_crossover(parent1, parent2)

    # With single gene, children should be copies of parents
    assert child1 == parent1
    assert child2 == parent2


def test_uniform_crossover_basic():
    """Test basic uniform crossover functionality."""
    parent1 = [1, 0, 1, 0, 1]
    parent2 = [0, 1, 0, 1, 0]

    child1, child2 = uniform_crossover(parent1, parent2, prob=0.5)

    # Children should have same length as parents
    assert len(child1) == len(parent1)
    assert len(child2) == len(parent2)

    # Children should contain only 0s and 1s
    assert all(gene in [0, 1] for gene in child1)
    assert all(gene in [0, 1] for gene in child2)


def test_uniform_crossover_extreme_probabilities():
    """Test uniform crossover with extreme probabilities."""
    parent1 = [1, 0, 1, 0, 1]
    parent2 = [0, 1, 0, 1, 0]

    # With prob=1.0, child1 should be identical to parent1
    child1, child2 = uniform_crossover(parent1, parent2, prob=1.0)
    assert child1 == parent1
    assert child2 == parent2

    # With prob=0.0, child1 should be identical to parent2
    child1, child2 = uniform_crossover(parent1, parent2, prob=0.0)
    assert child1 == parent2
    assert child2 == parent1


def test_uniform_crossover_different_lengths():
    """Test that uniform crossover raises error for different length parents."""
    parent1 = [1, 0, 1]
    parent2 = [0, 1]

    with pytest.raises(ValueError):
        uniform_crossover(parent1, parent2)


def test_crossover_preserves_genetic_material():
    """Test that crossover preserves genetic material from both parents."""
    parent1 = [1, 1, 1, 1, 1]
    parent2 = [0, 0, 0, 0, 0]

    child1, child2 = single_point_crossover(parent1, parent2)

    # Each child should have some genes from each parent
    assert 0 in child1 and 1 in child1
    assert 0 in child2 and 1 in child2
