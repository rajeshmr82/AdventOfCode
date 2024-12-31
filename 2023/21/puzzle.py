import math
import fractions
from functools import lru_cache
from collections import deque


def read_input():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse(input):
    return [list(line.strip()) for line in input.strip().splitlines()]


def neighbors(position, grid):
    """Return valid neighboring positions for a given position."""
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
    valid_neighbors = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within bounds and is a garden plot
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == ".":
                valid_neighbors.append((new_row, new_col))

    return valid_neighbors


def count_reachable_positions(grid, start_position, total_steps):
    """Perform BFS to find all reachable positions after a given number of steps."""
    queue = deque([start_position])
    reachable_positions = set()
    visited = set()  # Track visited positions

    for t in range(total_steps + 1):
        visit_next = set()
        for _ in range(len(queue)):
            current_row, current_col = queue.popleft()
            visited.add((current_row, current_col))

            # Add to reachable positions if the step count is even
            if t % 2 == 0:
                reachable_positions.add((current_row, current_col))

            # Explore the four possible directions
            for new_row, new_col in neighbors((current_row, current_col), grid):
                new_position = (new_row, new_col)
                if new_position not in visited:
                    visit_next.add(new_position)

        queue.extend(visit_next)

    return len(reachable_positions)


def find_start_position(garden_map):
    """Find the starting position in the garden map."""
    for row in range(len(garden_map)):
        for col in range(len(garden_map[row])):
            if garden_map[row][col] == "S":  # Assuming 'S' marks the start position
                return (row, col)
    return None  # Return None if no start position is found


def solve_part_one(input):
    garden_map = parse(input)
    start_position = find_start_position(garden_map)
    result = count_reachable_positions(garden_map, start_position, 64)
    return result


def solve_two(grid, n_steps=None):
    if n_steps is None:
        n_steps = 26501365
    shape = (len(grid), len(grid[0]))
    start = find_start_position(grid)

    # Convert grid to tuple of tuples for hashability
    grid_tuple = tuple(tuple(row) for row in grid)

    @lru_cache(maxsize=None)
    def walk_general(n_steps, start_pos):
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
        return frozenset(reachable)  # Convert to frozenset for hashability

    def walk(n_steps):
        def check_diamond():
            reachable = walk_general(shape[0] // 2, start)
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
        special = special and check_diamond()
        if special:
            return walk_special(n_steps, start)
        return len(walk_general(n_steps, start))

    def walk_special(n_steps, start):
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
        y = [len(walk_general(xi, start)) for xi in x]        
        return poly_lagrange(n_steps)  

    return walk(n_steps)



def solve_part_two(input):
    garden_map = parse(input)

    reachable_count = solve_two(garden_map, 26501365)
    
    return reachable_count
