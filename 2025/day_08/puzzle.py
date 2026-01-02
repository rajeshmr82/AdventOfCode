"""
Advent of Code 2025 - Day 8
Author: Rajesh M R
"""

from collections import defaultdict
import heapq
from itertools import combinations
import math
from pathlib import Path


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """
    Parse the raw input into a list of co-ordinates.
    """

    return [tuple(map(int, line.split(","))) for line in raw_input.splitlines()]


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]


def solve_part_one(junctions, attempt_count=1000):
    # Calculate all pairwise distances and sort
    edges = [
        ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2, i, j)
        for i, j in combinations(range(len(junctions)), 2)
        for (x1, y1, z1), (x2, y2, z2) in [(junctions[i], junctions[j])]
    ]
    edges.sort()

    # Connect closest pairs using Union-Find
    uf = UnionFind(len(junctions))
    for _, i, j in edges[:attempt_count]:  # Take first N edges
        uf.union(i, j)

    # Count component sizes
    component_sizes = defaultdict(int)
    for i in range(len(junctions)):
        component_sizes[uf.find(i)] += 1

    # Multiply three largest
    top_three = sorted(component_sizes.values(), reverse=True)[:3]
    return top_three[0] * top_three[1] * top_three[2]


def solve_part_two(junctions):
    """
    Solve part two of the puzzle.

    Args:
        junctions: Parsed input data

    Returns:
        The answer to part two
    """
    # Calculate all pairwise distances and sort
    edges = [
        ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2, i, j)
        for i, j in combinations(range(len(junctions)), 2)
        for (x1, y1, z1), (x2, y2, z2) in [(junctions[i], junctions[j])]
    ]
    edges.sort()
    # Connect closest pairs using Union-Find
    uf = UnionFind(len(junctions))

    # Process ALL edges until everything is connected
    successful_unions = 0
    for distance, i, j in edges:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            successful_unions += 1

            # MST needs exactly (n-1) edges to connect n nodes
            if successful_unions == len(junctions) - 1:
                # This was the last edge!
                x1, _, _ = junctions[i]
                x2, _, _ = junctions[j]
                return x1 * x2


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 8")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")

    print("=" * 50)
