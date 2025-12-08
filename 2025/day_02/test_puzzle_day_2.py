"""
Tests for Advent of Code 2025 - Day 2
Author: Rajesh M R
"""
import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


class TestDay02:
    """Test cases for Day 2 solutions."""
    
    def test_parse_sample(self):
        """Test parsing with sample data."""
        if SAMPLE_INPUT:
            result = parse(SAMPLE_INPUT)
            assert result is not None
            assert result == [(11, 22), (95, 115), (998, 1012), (1188511880, 1188511890), (222220, 222224), (1698522, 1698528), (446443, 446449), (38593856, 38593862), (565653, 565659), (824824821, 824824827), (2121212118, 2121212124)]
    
    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 1227775554
    
    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'='*50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'='*50}")
        assert result == 34826702005
    
    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            # Uncomment once you know the expected answer:
            # assert result == EXPECTED_SAMPLE_ANSWER
    
    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'='*50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'='*50}")
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
    # Run with: python test_puzzle_day_2.py
    # Or: pytest test_puzzle_day_2.py -v -s
    pytest.main([__file__, "-v", "-s"])