"""
Tests for Advent of Code 2025 - Day 4
Author: Rajesh M R
"""

import numpy as np
import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


class TestDay04:
    """Test cases for Day 4 solutions."""

    def test_parse_basic_grid(self):
        """Test parsing a basic grid."""
        raw = "..@\nx@@\n@@@"
        result = parse(raw)
        expected = np.array([[".", ".", "@"], ["x", "@", "@"], ["@", "@", "@"]])
        np.testing.assert_array_equal(result, expected)

    def test_parse_with_leading_trailing_whitespace(self):
        """Test that leading/trailing whitespace is stripped."""
        raw = "\n\n..@\nx@@\n\n"
        result = parse(raw)
        expected = np.array([[".", ".", "@"], ["x", "@", "@"]])
        np.testing.assert_array_equal(result, expected)

    def test_parse_single_line(self):
        """Test parsing a single line."""
        raw = "..@@@"
        result = parse(raw)
        expected = np.array([[".", ".", "@", "@", "@"]])
        np.testing.assert_array_equal(result, expected)

    def test_parse_empty_cells(self):
        """Test parsing grid with dots (empty cells)."""
        raw = "...\n...\n..."
        result = parse(raw)
        expected = np.array([[".", ".", "."], [".", ".", "."], [".", ".", "."]])
        np.testing.assert_array_equal(result, expected)

    def test_parse_example_grid(self):
        """Test parsing the example from the problem."""
        result = parse(SAMPLE_INPUT)

        # Verify shape
        assert result.shape == (10, 10)

        # Verify specific positions
        assert result[0, 0] == "."
        assert result[0, 2] == "@"
        assert result[1, 0] == "@"

        # Verify it's a numpy array
        assert isinstance(result, np.ndarray)

    def test_parse_mixed_characters(self):
        """Test parsing with various characters."""
        raw = ".@x\n#$%\nabc"
        result = parse(raw)
        expected = np.array([[".", "@", "x"], ["#", "$", "%"], ["a", "b", "c"]])
        np.testing.assert_array_equal(result, expected)

    def test_parse_rectangular_grid(self):
        """Test parsing non-square grids."""
        raw = "..@@@\nx@@@@"
        result = parse(raw)
        assert result.shape == (2, 5)

        raw = "..\nx@\n@@"
        result = parse(raw)
        assert result.shape == (3, 2)

    def test_parse_dtype(self):
        """Test that the result is a string array."""
        raw = "..@\n@@@"
        result = parse(raw)
        assert result.dtype.kind == "U"  # Unicode string

    def test_parse_preserves_all_characters(self):
        """Test that all characters are preserved correctly."""
        raw = "@.x"
        result = parse(raw)
        assert result[0, 0] == "@"
        assert result[0, 1] == "."
        assert result[0, 2] == "x"

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 13

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 1419

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 43

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
    # Run with: python test_puzzle_day_4.py
    # Or: pytest test_puzzle_day_4.py -v -s
    pytest.main([__file__, "-v", "-s"])
