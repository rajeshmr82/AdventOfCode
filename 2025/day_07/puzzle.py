"""
Advent of Code 2025 - Day 7
Author: Rajesh M R
"""

from bisect import bisect_left, bisect_right
from collections import deque, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


@dataclass
class TachyonManifold:
    """Represents the parsed tachyon manifold grid."""

    source: Tuple[int, int]  # (row, col) of the source 'S'
    splitters: Set[Tuple[int, int]]  # Set of (row, col) positions with splitters '^'
    rows: int
    cols: int

    # Pre-computed indices for fast lookup
    splitters_by_row: Dict[int, List[int]] = None  # row -> sorted list of cols
    splitters_by_col: Dict[int, List[int]] = None  # col -> sorted list of rows

    def __post_init__(self):
        """Pre-index splitters by column for O(log n) lookup."""
        self.splitters_by_col = defaultdict(list)
        for row, col in self.splitters:
            self.splitters_by_col[col].append(row)

        # Sort each column's rows for binary search
        for col in self.splitters_by_col:
            self.splitters_by_col[col].sort()

    def is_splitter(self, row: int, col: int) -> bool:
        """Check if a position contains a splitter."""
        return (row, col) in self.splitters

    def in_bounds(self, row: int, col: int) -> bool:
        """Check if a position is within the manifold bounds."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def find_next_splitter_down(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        """Binary search for next splitter - O(log n)."""
        if col not in self.splitters_by_col:
            return None

        rows_in_col = self.splitters_by_col[col]

        # Binary search for first row > current row
        idx = bisect_right(rows_in_col, row)

        if idx < len(rows_in_col):
            return (rows_in_col[idx], col)

        return None


def parse(input_text: str) -> TachyonManifold:
    """
    Parse the tachyon manifold input.

    Args:
        input_text: Multi-line string representing the manifold grid

    Returns:
        TachyonManifold object with source position, splitter positions, and dimensions
    """
    lines = input_text.strip().split("\n")

    source = None
    splitters = set()
    rows = len(lines)
    cols = len(lines[0]) if lines else 0

    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line.strip()):
            if char == "S":
                source = (row_idx, col_idx)
            elif char == "^":
                splitters.add((row_idx, col_idx))

    if source is None:
        raise ValueError("No source 'S' found in input")

    return TachyonManifold(source=source, splitters=splitters, rows=rows, cols=cols)


def solve_part_one(manifold):
    """
    Count how many times beams are split in the manifold.

    Intuition:
    1. Start with beam going DOWN from source
    2. For each beam state:
       - Move in that direction until we hit a splitter or exit
       - If we hit a splitter: create 2 new beams (left & right), count the split
       - If we exit: beam is done
    3. Track states to avoid infinite loops
    4. Use BFS queue to process all beams
    5. Count unique splitters that are hit by at least one beam.
    """

    queue = deque([manifold.source])
    visited = {manifold.source}
    hit_splitters = set()

    while queue:
        row, col = queue.popleft()

        next_splitter = manifold.find_next_splitter_down(row, col)

        if next_splitter is None:
            continue

        split_row, split_col = next_splitter

        # Mark this splitter as hit (even if we've hit it before)
        hit_splitters.add((split_row, split_col))

        for new_col in [split_col - 1, split_col + 1]:
            pos = (split_row, new_col)
            if 0 <= new_col < manifold.cols and pos not in visited:
                visited.add(pos)
                queue.append(pos)

    return len(hit_splitters)


def solve_part_two(manifold):
    """
    Count the number of distinct timelines (paths) through the manifold.

    A timeline is a complete path from source to exit.
    At each splitter, the path branches into 2 timelines.
    """

    @lru_cache(maxsize=None)
    def count_paths_from(row: int, col: int) -> int:
        """
        Count number of distinct paths from (row, col) to exit.

        Returns:
            Number of ways to reach the exit from this position
        """
        # Find next splitter going down
        next_splitter = manifold.find_next_splitter_down(row, col)

        if next_splitter is None:
            # This beam exits - that's 1 complete timeline
            return 1

        split_row, split_col = next_splitter

        # At splitter, particle can go left OR right
        # Each choice creates a separate timeline
        left_col = split_col - 1
        right_col = split_col + 1

        total_paths = 0

        # Count paths if we go left
        if 0 <= left_col < manifold.cols:
            total_paths += count_paths_from(split_row, left_col)

        # Count paths if we go right
        if 0 <= right_col < manifold.cols:
            total_paths += count_paths_from(split_row, right_col)

        return total_paths

    # Start from source
    return count_paths_from(manifold.source[0], manifold.source[1])


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 7")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")

    print("=" * 50)
