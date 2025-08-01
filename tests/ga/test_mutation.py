import pytest
from ga.mutation import bit_flip_mutation, random_reset_mutation


def test_bit_flip_mutation_no_mutation():
    """Test bit flip mutation with zero mutation rate."""
    individual = [1, 0, 1, 0, 1]
    mutated = bit_flip_mutation(individual, mutation_rate=0.0)

    # With 0% mutation rate, individual should remain unchanged
    assert mutated == individual
    # Should be a copy, not the same object
    assert mutated is not individual


def test_bit_flip_mutation_full_mutation():
    """Test bit flip mutation with 100% mutation rate."""
    individual = [1, 0, 1, 0, 1]
    mutated = bit_flip_mutation(individual, mutation_rate=1.0)

    # With 100% mutation rate, all bits should be flipped
    expected = [0, 1, 0, 1, 0]
    assert mutated == expected


def test_bit_flip_mutation_preserves_length():
    """Test that mutation preserves individual length."""
    individual = [1, 0, 1, 0, 1, 1, 0]
    mutated = bit_flip_mutation(individual, mutation_rate=0.5)

    assert len(mutated) == len(individual)


def test_bit_flip_mutation_binary_values():
    """Test that mutation only produces binary values."""
    individual = [1, 0, 1, 0, 1]
    mutated = bit_flip_mutation(individual, mutation_rate=0.5)

    # All genes should be 0 or 1
    assert all(gene in [0, 1] for gene in mutated)


def test_bit_flip_mutation_empty_individual():
    """Test mutation with empty individual."""
    individual = []
    mutated = bit_flip_mutation(individual, mutation_rate=0.5)

    assert mutated == []


def test_random_reset_mutation_no_mutation():
    """Test random reset mutation with zero mutation rate."""
    individual = [1, 0, 1, 0, 1]
    mutated = random_reset_mutation(individual, mutation_rate=0.0)

    # With 0% mutation rate, individual should remain unchanged
    assert mutated == individual
    # Should be a copy, not the same object
    assert mutated is not individual


def test_random_reset_mutation_preserves_length():
    """Test that random reset mutation preserves individual length."""
    individual = [1, 0, 1, 0, 1, 1, 0]
    mutated = random_reset_mutation(individual, mutation_rate=0.5)

    assert len(mutated) == len(individual)


def test_random_reset_mutation_binary_values():
    """Test that random reset mutation only produces binary values."""
    individual = [1, 0, 1, 0, 1]
    mutated = random_reset_mutation(individual, mutation_rate=1.0)

    # All genes should be 0 or 1
    assert all(gene in [0, 1] for gene in mutated)


def test_mutation_creates_copy():
    """Test that mutation functions create copies and don't modify originals."""
    original = [1, 0, 1, 0, 1]

    # Test bit flip mutation
    mutated1 = bit_flip_mutation(original, mutation_rate=1.0)
    assert original == [1, 0, 1, 0, 1]  # Original unchanged

    # Test random reset mutation
    mutated2 = random_reset_mutation(original, mutation_rate=1.0)
    assert original == [1, 0, 1, 0, 1]  # Original unchanged
