"""
Tests for Advent of Code 2025 - Day 8
Author: Rajesh M R
"""

import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


class TestDay08:
    """Test cases for Day 8 solutions."""

    def test_parse_basic(self):
        """Test basic parsing of coordinate strings"""
        input_data = """162,817,812
    57,618,57
    906,360,560"""

        expected = [(162, 817, 812), (57, 618, 57), (906, 360, 560)]

        result = parse(input_data)
        assert result == expected

    def test_parse_sample(self):
        """Test parsing with sample data."""
        if SAMPLE_INPUT:
            result = parse(SAMPLE_INPUT)

            assert len(result) == 20
            assert result[0] == (162, 817, 812)
            assert result[-1] == (425, 690, 689)
            assert all(isinstance(coord, tuple) for coord in result)
            assert all(len(coord) == 3 for coord in result)

    def test_parse_single_line(self):
        """Test parsing a single coordinate"""
        input_data = "100,200,300"
        result = parse(input_data)
        assert result == [(100, 200, 300)]

    def test_parse_empty_string(self):
        """Test parsing empty string"""
        result = parse("")
        assert result == []

    def test_parse_with_trailing_newline(self):
        """Test parsing with trailing newline"""
        input_data = "100,200,300\n"
        result = parse(input_data)
        assert result == [(100, 200, 300)]

    def test_parse_returns_integers(self):
        """Test that coordinates are integers, not strings"""
        input_data = "1,2,3"
        result = parse(input_data)
        assert result[0] == (1, 2, 3)
        assert all(isinstance(val, int) for val in result[0])

    def test_parse_handles_large_numbers(self):
        """Test parsing large coordinate values"""
        input_data = "999999,888888,777777"
        result = parse(input_data)
        assert result == [(999999, 888888, 777777)]

    def test_parse_handles_zero_values(self):
        """Test parsing zero coordinate values"""
        input_data = "0,0,0\n1,0,1"
        result = parse(input_data)
        assert result == [(0, 0, 0), (1, 0, 1)]

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data, 10)
            print(f"Part One (sample): {result}")
            assert result == 40

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 164475

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 25272

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
    # Run with: python test_puzzle_day_8.py
    # Or: pytest test_puzzle_day_8.py -v -s
    pytest.main([__file__, "-v", "-s"])
