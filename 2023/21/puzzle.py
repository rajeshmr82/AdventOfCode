import math
import fractions
from functools import lru_cache
from collections import deque


def read_input():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse(input):
    return [list(line.strip()) for line in input.strip().splitlines()]


def find_start_position(garden_map):
    """Find the starting position in the garden map."""
    for row in range(len(garden_map)):
        for col in range(len(garden_map[row])):
            if garden_map[row][col] == "S":
                return (row, col)
    return None


def solve_two(grid, n_steps=None):

    shape = (len(grid), len(grid[0]))
    start = find_start_position(grid)
    grid_tuple = tuple(tuple(row) for row in grid)

    @lru_cache(maxsize=None)
    def calculate_reachable_plots(n_steps, start_pos):
        visit = {start_pos}
        visited = set()
        reachable = set()
        odd = n_steps & 1
        for t in range(n_steps + 1):
            visit_next = set()
            while visit:
                i, j = visit.pop()
                visited.add((i, j))
                if t & 1 == odd:
                    reachable.add((i, j))
                for di, dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                    i_next, j_next = i + di, j + dj
                    if grid_tuple[i_next % shape[0]][j_next % shape[1]] == '#':
                        continue
                    if (i_next, j_next) in visited:
                        continue
                    visit_next.add((i_next, j_next))
            visit = visit_next
        return frozenset(reachable)

    def process_steps(n_steps):
        def verify_diamond_pattern():
            reachable = calculate_reachable_plots(shape[0] // 2, start)
            i, j = 0, shape[0] // 2
            for di, dj in [(+1, +1), (+1, -1), (-1, -1), (-1, +1)]:
                for dstep in range(shape[0] // 2):
                    i += di
                    j += dj
                    if (i, j) not in reachable:
                        return False
            return True

        special = shape[0] == shape[1]
        special &= shape[0] & 1
        special &= (n_steps - shape[0] // 2) % shape[0] == 0
        special = special and verify_diamond_pattern()
        if special:
            return calculate_infinite_grid(n_steps, start)
        return len(calculate_reachable_plots(n_steps, start))

    def calculate_infinite_grid(n_steps, start):
        def poly_lagrange(p):
            a = (
                fractions.Fraction(
                    math.prod(p - xj for xj in x if xj != xi),
                    math.prod(xi - xj for xj in x if xj != xi),
                )
                for xi in x
            )
            return sum(ai * yi for ai, yi in zip(a, y))
        order = 2
        x = [i * shape[0] // 2 for i in range(1, 2 * (order + 1), 2)]
        y = [len(calculate_reachable_plots(xi, start)) for xi in x]        
        return poly_lagrange(n_steps)  

    return process_steps(n_steps)


def solve_part_two(input):
    garden_map = parse(input)
    return solve_two(garden_map, 26501365)
