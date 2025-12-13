"""
Advent of Code 2025 - Day 4
Author: Rajesh M R
"""

from pathlib import Path
from typing import List, Tuple

import numpy as np


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """
    Parse the raw input into a usable format.

    Common patterns:
    - lines = raw_input.splitlines()
    - numbers = [int(x) for x in raw_input.split()]
    - grid = [list(line) for line in raw_input.splitlines()]
    - blocks = raw_input.split('\\n\\n')
    """
    lines = raw_input.strip().split("\n")
    return np.array([list(line) for line in lines])


def solve_part_one(grid):
    """
    Count rolls (@) with fewer than 4 adjacent @ rolls.

    Args:
        grid: Parsed input data

    Returns:
        The answer to part one
    """
    rows, cols = grid.shape
    # All 8 directions (including diagonals)
    directions = [
        (dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)
    ]

    return sum(
        grid[r, c] == "@"
        and sum(
            0 <= r + dr < grid.shape[0]
            and 0 <= c + dc < grid.shape[1]
            and grid[r + dr, c + dc] == "@"
            for dr, dc in directions
        )
        < 4
        for r in range(grid.shape[0])
        for c in range(grid.shape[1])
    )


def solve_part_two(data):
    """
    Solve part two of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part two
    """
    # TODO: Implement solution
    grid = data.copy()
    rows, cols = grid.shape

    directions = [
        (dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)
    ]

    to_check = {(r, c) for r in range(rows) for c in range(cols) if grid[r, c] == "@"}

    total_removed = 0

    def get_affected_neighbours(r, c):
        affected = set()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == "@":
                affected.add((nr, nc))

        return affected

    while to_check:
        accessible = [
            (r, c)
            for (r, c) in to_check
            if grid[r, c] == "@"
            and sum(
                0 <= r + dr < grid.shape[0]
                and 0 <= c + dc < grid.shape[1]
                and grid[r + dr, c + dc] == "@"
                for dr, dc in directions
            )
            < 4
        ]

        if not accessible:
            break

        next_check = set()

        for r, c in accessible:
            grid[r, c] = "."
            next_check.update(get_affected_neighbours(r, c))

        total_removed += len(accessible)
        to_check = next_check

        print(f"Removed {len(accessible)} rolls (total: {total_removed})")

    return total_removed


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print("Advent of Code 2025 - Day 4")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print("Part One: {answer_one}")

    answer_two = solve_part_two(data)
    print("Part Two: {answer_two}")

    print("=" * 50)
