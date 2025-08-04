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

    @staticmethod
    def k_point(parent1: List[int], parent2: List[int], k: int = 2) -> Tuple[List[int], List[int]]:
        """K-point crossover for binary individuals."""
        points = sorted(random.sample(range(1, len(parent1)), k))
        child1, child2 = parent1[:], parent2[:]
        for i in range(len(points)):
            if i % 2 == 0:
                start = points[i]
                end = points[i+1] if i+1 < len(points) else len(parent1)
                child1[start:end], child2[start:end] = child2[start:end], child1[start:end]
        return child1, child2

    @staticmethod
    def uniform(parent1: List[int], parent2: List[int], p: float = 0.5) -> Tuple[List[int], List[int]]:
        """Uniform crossover for binary individuals."""
        child1, child2 = [], []
        for g1, g2 in zip(parent1, parent2):
            if random.random() < p:
                child1.append(g1)
                child2.append(g2)
            else:
                child1.append(g2)
                child2.append(g1)
        return child1, child2

    @staticmethod
    def shuffle(parent1: List[int], parent2: List[int], method='one_point') -> Tuple[List[int], List[int]]:
        """Shuffle crossover for binary individuals."""
        idx = list(range(len(parent1)))
        random.shuffle(idx)
        p1_shuffled = [parent1[i] for i in idx]
        p2_shuffled = [parent2[i] for i in idx]
        if method == 'one_point':
            c1, c2 = Crossover.one_point(p1_shuffled, p2_shuffled)
        elif method == 'uniform':
            c1, c2 = Crossover.uniform(p1_shuffled, p2_shuffled)
        else:
            raise ValueError("Unknown method for shuffle crossover")
        # Unshuffle
        unshuffled_c1 = [None]*len(parent1)
        unshuffled_c2 = [None]*len(parent1)
        for i, j in enumerate(idx):
            unshuffled_c1[j] = c1[i]
            unshuffled_c2[j] = c2[i]
        return unshuffled_c1, unshuffled_c2