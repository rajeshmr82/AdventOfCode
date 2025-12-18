"""
Advent of Code 2025 - Day 5
Author: Rajesh M R
"""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List
import re
from dataclasses import dataclass
from typing import List


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


"""
Ingredient Database Parser

Efficiently handles large ranges and many lookups by storing ranges
instead of expanding them into individual IDs.

Memory complexity: O(n) where n is the number of ranges (not the size of ranges)
Lookup complexity: O(n) where n is the number of ranges
"""


@dataclass
class Range:
    """Represents an inclusive range [start, end]."""

    start: int
    end: int

    def __contains__(self, value: int) -> bool:
        """Check if value is in this range using 'in' operator."""
        return self.start <= value <= self.end

    def __repr__(self):
        return f"Range({self.start}, {self.end})"


class IngredientDatabase:
    """
    Memory-efficient ingredient database using range-based storage.

    Example:
        >>> db = parse("1-10\\n\\n5\\n15")
        >>> db.is_fresh(5)
        True
        >>> db.fresh_available
        [5]
        >>> len(db)
        2
    """

    def __init__(self, fresh_ranges: List[Range], available_ids: List[int]):
        """Initialize with ranges and available IDs (ranges are auto-merged)."""
        self.available_ids = available_ids
        self.fresh_ranges = self._merge_ranges(fresh_ranges)

    def _merge_ranges(self, ranges: List[Range]) -> List[Range]:
        """Merge overlapping or adjacent ranges for better performance."""
        if not ranges:
            return []

        # Sort by start position and merge
        sorted_ranges = sorted(ranges, key=lambda r: r.start)
        merged = [sorted_ranges[0]]

        for current in sorted_ranges[1:]:
            last = merged[-1]

            # Merge if overlapping or adjacent
            if current.start <= last.end + 1:
                last.end = max(last.end, current.end)
            else:
                merged.append(current)

        return merged

    def is_fresh(self, ingredient_id: int) -> bool:
        """Check if an ingredient ID is fresh (in any range)."""
        return any(ingredient_id in r for r in self.fresh_ranges)

    def is_available(self, ingredient_id: int) -> bool:
        """Check if an ingredient ID is available."""
        return ingredient_id in self.available_ids

    @property
    def fresh_available(self) -> List[int]:
        """Get ingredient IDs that are both fresh and available."""
        return [id for id in self.available_ids if self.is_fresh(id)]

    def __len__(self) -> int:
        """Return number of available ingredients."""
        return len(self.available_ids)

    def __repr__(self) -> str:
        """Return clean string representation."""
        return f"IngredientDatabase(ranges={len(self.fresh_ranges)}, available={len(self.available_ids)})"

    def __str__(self) -> str:
        """Return user-friendly string representation."""
        return f"Database with {len(self.fresh_ranges)} range(s) and {len(self.available_ids)} available ingredient(s)"

    @property
    def total_fresh_count(self) -> int:
        """
        Count total number of distinct fresh ingredient IDs across all ranges.

        This counts how many unique IDs are covered by the fresh ranges,
        handling overlaps correctly.

        Example:
            >>> db = parse("3-5\\n10-14\\n")
            >>> db.total_fresh_count
            8
        """
        # After merging, ranges don't overlap, so we can just sum their sizes
        return sum(r.end - r.start + 1 for r in self.fresh_ranges)


def parse(text: str) -> IngredientDatabase:
    """
    Parse the ingredient database format.

    Args:
        text: Multi-line string containing ranges and ingredient IDs

    Returns:
        IngredientDatabase with parsed fresh ranges and available ingredient IDs

    Raises:
        ValueError: If the format is invalid

    Example:
        >>> data = '''3-5
        ... 10-14
        ...
        ... 1
        ... 5'''
        >>> db = parse(data)
        >>> db.is_fresh(5)
        True
    """
    # Handle empty input
    if not text or not text.strip():
        return IngredientDatabase(fresh_ranges=[], available_ids=[])

    lines = text.split("\n")

    # Find the blank line separator
    try:
        separator = lines.index("")
    except ValueError:
        raise ValueError(
            "Invalid format: missing blank line separator between ranges and IDs"
        )

    # Parse fresh ingredient ranges
    fresh_ranges = _parse_ranges(lines[:separator])

    # Parse available ingredient IDs
    available_ids = _parse_ids(lines[separator + 1 :])

    return IngredientDatabase(fresh_ranges=fresh_ranges, available_ids=available_ids)


def _parse_ranges(lines: List[str]) -> List[Range]:
    """Parse range lines into Range objects."""
    ranges = []
    range_pattern = re.compile(r"^(-?\d+)-(-?\d+)$")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        match = range_pattern.match(line)
        if not match:
            raise ValueError(
                f"Invalid range format: '{line}' (expected format: 'start-end')"
            )

        start, end = int(match.group(1)), int(match.group(2))

        if start > end:
            raise ValueError(f"Invalid range: {start}-{end} (start must be <= end)")

        ranges.append(Range(start, end))

    return ranges


def _parse_ids(lines: List[str]) -> List[int]:
    """Parse ID lines into a list of integers."""
    ids = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            ids.append(int(line))
        except ValueError:
            raise ValueError(f"Invalid ingredient ID: '{line}' (expected integer)")

    return ids


def solve_part_one(data):
    """
    Solve part one of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part one
    """
    return len(data.fresh_available)


def solve_part_two(data):
    """
    Solve part two of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part two
    """
    return data.total_fresh_count


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
