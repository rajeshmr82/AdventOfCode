"""
Tests for Advent of Code 2025 - Day 9
Author: Rajesh M R
"""

import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


class TestDay09:
    """Test cases for Day 9 solutions."""

    def test_parse_sample(self):
        """Test parsing with sample data."""
        if SAMPLE_INPUT:
            result = parse(SAMPLE_INPUT)
            expected = [
                (7, 1),
                (11, 1),
                (11, 7),
                (9, 7),
                (9, 5),
                (2, 5),
                (2, 3),
                (7, 3),
            ]

            assert result == expected

    def test_parse_single_line(self):
        """Test parsing a single coordinate pair"""
        input_data = "5,10"
        expected = [(5, 10)]

        result = parse(input_data)
        assert result == expected

    def test_parse_empty_string(self):
        """Test parsing an empty string"""
        input_data = ""
        expected = []

        result = parse(input_data)
        assert result == expected

    def test_parse_with_trailing_newline(self):
        """Test parsing with trailing newline"""
        input_data = "3,4\n5,6\n"
        expected = [(3, 4), (5, 6)]

        result = parse(input_data)
        assert result == expected

    def test_parse_returns_list_of_tuples(self):
        """Test that result is a list of tuples"""
        input_data = "1,2\n3,4"
        result = parse(input_data)

        assert isinstance(result, list)
        assert all(isinstance(item, tuple) for item in result)
        assert all(len(item) == 2 for item in result)

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 50

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 4781377701

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 24

    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'=' * 50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'=' * 50}")
        # Once you submit and get the correct answer:
        assert result == 1470616992


if __name__ == "__main__":
    # Run with: python test_puzzle_day_9.py
    # Or: pytest test_puzzle_day_9.py -v -s
    pytest.main([__file__, "-v", "-s"])
