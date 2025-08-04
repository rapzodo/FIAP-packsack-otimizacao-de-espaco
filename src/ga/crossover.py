import random
from typing import List, Tuple

class Crossover:
    @staticmethod
    def one_point(parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        """One-point crossover for binary individuals."""
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
