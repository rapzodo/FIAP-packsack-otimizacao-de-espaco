from ga.mutation import Mutation


class TestMutation:
    def test_mutation_class_bit_flip_basic(self):
        individual = [1, 0, 1, 0, 1]
        mutated = Mutation.bit_flip(individual, mutation_rate=1.0)

        assert len(mutated) == len(individual)
        expected = [0, 1, 0, 1, 0]
        assert mutated == expected
        assert mutated is not individual

    def test_mutation_class_bit_flip_no_mutation(self):
        individual = [1, 0, 1, 0, 1]
        mutated = Mutation.bit_flip(individual, mutation_rate=0.0)

        assert mutated == individual
        assert mutated is not individual

    def test_mutation_class_bit_flip_preserves_length(self):
        individual = [1, 0, 1, 0, 1, 1, 0]
        mutated = Mutation.bit_flip(individual, mutation_rate=0.5)

        assert len(mutated) == len(individual)

    def test_mutation_class_bit_flip_binary_values(self):
        individual = [1, 0, 1, 0, 1]
        mutated = Mutation.bit_flip(individual, mutation_rate=0.5)

        assert all(gene in [0, 1] for gene in mutated)

    def test_mutation_class_bit_flip_empty_individual(self):
        individual = []
        mutated = Mutation.bit_flip(individual, mutation_rate=1.0)

        assert mutated == []

    def test_mutation_class_bit_flip_single_element(self):
        individual = [1]
        mutated = Mutation.bit_flip(individual, mutation_rate=1.0)

        assert mutated == [0]

    def test_mutation_class_preserves_original(self):
        original = [1, 0, 1, 0, 1]
        original_copy = original.copy()

        Mutation.bit_flip(original, mutation_rate=1.0)

        assert original == original_copy

    def test_mutation_class_bit_flip_variation(self):
        individual = [1, 0, 1, 0, 1, 0, 1, 0]
        results = []

        for _ in range(20):
            mutated = Mutation.bit_flip(individual, mutation_rate=0.3)
            results.append(tuple(mutated))

        unique_results = set(results)
        assert len(unique_results) > 1
