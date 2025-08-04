from unittest.mock import patch

import pytest
from ga.crossover import Crossover
from ga.fitness import evaluate_fitness, Item
from ga.mutation import Mutation
from ga.population import create_population
from ga.selection import tournament_selection
from main import calculate_population_fitness, get_best_individual, genetic_algorithm, main


class TestMainComponents:

    def test_calculate_population_fitness(self):
        items = [Item(10, 5), Item(20, 10), Item(15, 8)]
        population = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
        capacity = 20

        fitness_scores = calculate_population_fitness(population, items, capacity)

        assert len(fitness_scores) == len(population)
        assert all(isinstance(score, int) for score in fitness_scores)
        assert fitness_scores[0] == 25
        assert fitness_scores[1] == 20
        assert fitness_scores[2] == 30

    def test_get_best_individual(self):
        population = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
        fitness_scores = [25, 20, 30]

        best_individual, best_fitness = get_best_individual(population, fitness_scores)

        assert best_individual == [1, 1, 0]
        assert best_fitness == 30

    def test_get_best_individual_tie(self):
        population = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
        fitness_scores = [30, 20, 30]

        best_individual, best_fitness = get_best_individual(population, fitness_scores)

        assert best_individual == [1, 0, 1]
        assert best_fitness == 30


class TestGeneticAlgorithmIntegration:

    def test_genetic_algorithm_basic_run(self):
        test_items = [Item(10, 5), Item(20, 10), Item(15, 8), Item(25, 12)]

        with patch('main.items', test_items), \
             patch('main.NUM_ITEMS', 4), \
             patch('main.POPULATION_SIZE', 10), \
             patch('main.GENERATIONS', 5), \
             patch('main.KNAPSACK_CAPACITY', 20):

            best_solution, best_fitness, best_history, avg_history = genetic_algorithm()

            assert isinstance(best_solution, list)
            assert len(best_solution) == 4
            assert all(gene in [0, 1] for gene in best_solution)
            assert isinstance(best_fitness, int)
            assert best_fitness >= 0
            assert len(best_history) == 5
            assert len(avg_history) == 5
            assert all(isinstance(fitness, (int, float)) for fitness in best_history)
            assert all(isinstance(fitness, (int, float)) for fitness in avg_history)

    def test_genetic_algorithm_improvement(self):
        test_items = [Item(i*2, i) for i in range(1, 8)]

        with patch('main.items', test_items), \
             patch('main.NUM_ITEMS', 7), \
             patch('main.POPULATION_SIZE', 20), \
             patch('main.GENERATIONS', 10), \
             patch('main.KNAPSACK_CAPACITY', 15):

            best_solution, best_fitness, best_history, avg_history = genetic_algorithm()

            initial_best = best_history[0]
            final_best = best_history[-1]
            assert final_best >= initial_best
            assert best_fitness == final_best
            assert evaluate_fitness(best_solution, test_items, 15) == best_fitness


class TestBruteForceComparison:

    @staticmethod
    def brute_force_knapsack(items, capacity):
        n = len(items)
        best_value = 0
        best_solution = [0] * n

        for i in range(2**n):
            solution = [(i >> j) & 1 for j in range(n)]
            fitness = evaluate_fitness(solution, items, capacity)

            if fitness > best_value:
                best_value = fitness
                best_solution = solution

        return best_solution, best_value

    def test_small_instance_optimal(self):
        test_items = [Item(10, 5), Item(20, 10), Item(15, 8)]
        test_capacity = 15

        optimal_solution, optimal_value = self.brute_force_knapsack(test_items, test_capacity)

        best_ga_fitness = 0
        for _ in range(5):
            with patch('main.items', test_items), \
                 patch('main.NUM_ITEMS', 3), \
                 patch('main.POPULATION_SIZE', 20), \
                 patch('main.GENERATIONS', 50), \
                 patch('main.KNAPSACK_CAPACITY', test_capacity):

                ga_solution, ga_fitness, _, _ = genetic_algorithm()
                best_ga_fitness = max(best_ga_fitness, ga_fitness)

        optimality_gap = (optimal_value - best_ga_fitness) / optimal_value if optimal_value > 0 else 0
        assert optimality_gap <= 0.1

        print(f"Optimal value: {optimal_value}, GA best: {best_ga_fitness}, Gap: {optimality_gap:.1%}")

    def test_multiple_small_instances(self):
        test_cases = [
            ([Item(6, 3), Item(8, 4), Item(12, 6), Item(10, 5)], 10),
            ([Item(3, 2), Item(4, 3), Item(7, 4), Item(8, 5)], 8),
            ([Item(5, 1), Item(10, 2), Item(15, 3), Item(20, 4)], 6),
        ]

        for test_items, test_capacity in test_cases:
            optimal_solution, optimal_value = self.brute_force_knapsack(test_items, test_capacity)

            with patch('main.items', test_items), \
                 patch('main.NUM_ITEMS', len(test_items)), \
                 patch('main.POPULATION_SIZE', 30), \
                 patch('main.GENERATIONS', 30), \
                 patch('main.KNAPSACK_CAPACITY', test_capacity):

                ga_solution, ga_fitness, _, _ = genetic_algorithm()

            if optimal_value > 0:
                optimality_gap = (optimal_value - ga_fitness) / optimal_value
                assert optimality_gap <= 0.2
                assert ga_fitness > 0


class TestMainFunction:

    @patch('matplotlib.pyplot.show')
    def test_main_execution(self, mock_show):
        with patch('main.NUM_ITEMS', 5), \
             patch('main.POPULATION_SIZE', 10), \
             patch('main.GENERATIONS', 3), \
             patch('main.items', [Item(i*2, i) for i in range(1, 6)]):

            try:
                main()
            except SystemExit:
                pass

            mock_show.assert_called()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
