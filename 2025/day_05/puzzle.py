"""
Advent of Code 2025 - Day 5
Author: Rajesh M R
"""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List, Set


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


"""
Optimized Ingredient Database Parser

Efficiently handles large ranges and many lookups by storing ranges
instead of expanding them into individual IDs.

Memory complexity: O(n) where n is the number of ranges (not the size of ranges)
Lookup complexity: O(n) where n is the number of ranges
"""

import re
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Range:
    """Represents an inclusive range [start, end]."""

    start: int
    end: int

    def contains(self, value: int) -> bool:
        """Check if value is in this range."""
        return self.start <= value <= self.end

    def __repr__(self):
        return f"Range({self.start}, {self.end})"


class IngredientDatabase:
    """
    Ingredient database that stores ranges.

    Efficient for large ranges (e.g., 1-1000000000) and many ranges (175+).
    """

    def __init__(self, fresh_ranges: List[Range], available_ingredient_ids: List[int]):
        """
        Initialize the database.

        Args:
            fresh_ranges: List of Range objects representing fresh ingredient ranges
            available_ingredient_ids: List of available ingredient IDs
        """
        self.fresh_ranges = fresh_ranges
        self.available_ingredient_ids = available_ingredient_ids

        # Optional: merge overlapping ranges for even better performance
        # This is optional but can reduce lookup time
        self.fresh_ranges = self._merge_ranges(fresh_ranges)

    def _merge_ranges(self, ranges: List[Range]) -> List[Range]:
        """
        Merge overlapping or adjacent ranges.

        This optimization reduces the number of ranges to check during lookups.
        For 175 ranges with overlaps, this could reduce to fewer ranges.
        """
        if not ranges:
            return []

        # Sort ranges by start position
        sorted_ranges = sorted(ranges, key=lambda r: r.start)

        merged = [sorted_ranges[0]]

        for current in sorted_ranges[1:]:
            last = merged[-1]

            # Check if ranges overlap or are adjacent
            if current.start <= last.end + 1:
                # Merge by extending the end of the last range
                last.end = max(last.end, current.end)
            else:
                # No overlap, add as new range
                merged.append(current)

        return merged

    def is_fresh(self, ingredient_id: int) -> bool:
        """
        Check if an ingredient ID is fresh.

        Time complexity: O(n) where n is the number of ranges
        Space complexity: O(1)
        """
        for range_obj in self.fresh_ranges:
            if range_obj.contains(ingredient_id):
                return True
        return False

    def is_available(self, ingredient_id: int) -> bool:
        """Check if an ingredient ID is available."""
        return ingredient_id in self.available_ingredient_ids

    def count_fresh_available(self) -> int:
        """
        Count how many available ingredients are fresh.

        More efficient than creating a set of all fresh IDs.
        """
        count = 0
        for ingredient_id in self.available_ingredient_ids:
            if self.is_fresh(ingredient_id):
                count += 1
        return count

    def get_fresh_available_ids(self) -> List[int]:
        """Get ingredient IDs that are both fresh and available."""
        return [
            ingredient_id
            for ingredient_id in self.available_ingredient_ids
            if self.is_fresh(ingredient_id)
        ]

    def get_stats(self) -> dict:
        """Get statistics about the database."""
        return {
            "num_ranges": len(self.fresh_ranges),
            "num_available": len(self.available_ingredient_ids),
            "num_fresh_available": self.count_fresh_available(),
            "ranges": [(r.start, r.end) for r in self.fresh_ranges],
        }


def parse(text: str) -> IngredientDatabase:
    """
    Parse the ingredient database format.

    Args:
        text: Multi-line string containing ranges and ingredient IDs

    Returns:
        IngredientDatabase with parsed fresh ranges and available ingredient IDs

    Raises:
        ValueError: If the format is invalid
    """
    # Handle empty input
    if not text or not text.strip():
        return IngredientDatabase(fresh_ranges=[], available_ingredient_ids=[])

    lines = text.split("\n")

    # Find the blank line separator
    try:
        separator_index = lines.index("")
    except ValueError:
        raise ValueError(
            "Invalid format: missing blank line separator between ranges and IDs"
        )

    # Parse fresh ingredient ranges
    range_lines = lines[:separator_index]
    fresh_ranges = []

    # Pattern to match ranges: handles negative numbers correctly
    # Matches: "5-10", "-5-10", "5--10", "-5--10"
    range_pattern = r"^(-?\d+)-(-?\d+)$"

    for line in range_lines:
        line = line.strip()
        if not line:
            continue

        match = re.match(range_pattern, line)
        if not match:
            raise ValueError(
                f"Invalid range format: '{line}' (expected format: 'start-end')"
            )

        try:
            start_id = int(match.group(1))
            end_id = int(match.group(2))

            if start_id > end_id:
                raise ValueError(
                    f"Invalid range: {start_id}-{end_id} (start must be <= end)"
                )

            fresh_ranges.append(Range(start_id, end_id))
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError(f"Invalid range format: '{line}' (expected integers)")
            raise

    # Parse available ingredient IDs
    available_lines = lines[separator_index + 1 :]
    available_ids = []

    for line in available_lines:
        line = line.strip()
        if not line:
            continue

        try:
            ingredient_id = int(line)
            available_ids.append(ingredient_id)
        except ValueError:
            raise ValueError(f"Invalid ingredient ID: '{line}' (expected integer)")

    return IngredientDatabase(
        fresh_ranges=fresh_ranges, available_ingredient_ids=available_ids
    )


def solve_part_one(data):
    """
    Solve part one of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part one
    """
    return data.count_fresh_available()


def solve_part_two(data):
    """
    Solve part two of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part two
    """
    # TODO: Implement solution
    result = None
    return result


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 5")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")

    print("=" * 50)
