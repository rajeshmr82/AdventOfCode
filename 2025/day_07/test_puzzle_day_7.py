"""
Tests for Advent of Code 2025 - Day 7
Author: Rajesh M R
"""

import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


class TestDay07:
    """Test cases for Day 7 solutions."""

    def test_parse_simple_grid(self):
        """Test parsing a simple grid."""
        input_text = """
    .......S.......
    ...............
    .......^.......
    """
        manifold = parse(input_text)

        assert manifold.source == (0, 7)
        assert (2, 7) in manifold.splitters
        assert len(manifold.splitters) == 1
        assert manifold.rows == 3
        assert manifold.cols == 15

    def test_parse_example_grid(self):
        """Test parsing the full example from the problem."""
        input_text = """.......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ..............."""

        manifold = parse(input_text)

        assert manifold.source == (0, 7)
        assert manifold.rows == 16
        assert manifold.cols == 15

        # Check some specific splitter positions
        assert (2, 7) in manifold.splitters
        assert (4, 6) in manifold.splitters
        assert (4, 8) in manifold.splitters

        # Count total splitters (from visual inspection)
        # Row 2: 1, Row 4: 2, Row 6: 3, Row 8: 3, Row 10: 4, Row 12: 3, Row 14: 6
        assert len(manifold.splitters) == 22

    def test_is_splitter(self):
        """Test the is_splitter helper method."""
        input_text = """.......S.......
    ...............
    .......^......."""

        manifold = parse(input_text)

        assert manifold.is_splitter(2, 7) == True
        assert manifold.is_splitter(0, 7) == False  # Source, not splitter
        assert manifold.is_splitter(1, 7) == False  # Empty space

    def test_in_bounds(self):
        """Test the in_bounds helper method."""
        input_text = """.......S.......
    ...............
    .......^......."""

        manifold = parse(input_text)

        assert manifold.in_bounds(0, 0) == True
        assert manifold.in_bounds(2, 14) == True
        assert manifold.in_bounds(-1, 0) == False
        assert manifold.in_bounds(3, 0) == False
        assert manifold.in_bounds(0, 15) == False

    def test_no_source_raises_error(self):
        """Test that missing source raises an error."""
        input_text = """...............
    ...............
    .......^......."""

        try:
            parse(input_text)
            assert False, "Should have raised ValueError"
        except ValueError as e:
            assert "No source" in str(e)

    def test_count_splitters_in_input(self):
        """Verify we're parsing the correct number of splitters."""
        input_text = """.......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ..............."""

        manifold = parse(input_text)
        print(f"Number of splitters in grid: {len(manifold.splitters)}")
        print(f"Splitters: {sorted(manifold.splitters)}")

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 21

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 1638

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 40

    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'=' * 50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'=' * 50}")
        # Once you submit and get the correct answer:
        # assert result == YOUR_CORRECT_ANSWER


# Add unit tests for helper functions below
def test_helper_example():
    """Example test for a helper function."""
    # from puzzle import helper_function
    # result = helper_function(test_input)
    # assert result == expected_output
    pass


if __name__ == "__main__":
    # Run with: python test_puzzle_day_7.py
    # Or: pytest test_puzzle_day_7.py -v -s
    pytest.main([__file__, "-v", "-s"])
