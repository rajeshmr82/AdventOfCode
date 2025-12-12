"""
Tests for Advent of Code 2025 - Day 3
Author: Rajesh M R
"""
import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111"""


class TestDay03:
    """Test cases for Day 3 solutions."""
    
    def test_parse_sample(self):
        """Test parsing with sample data."""
        
        # Test 2: Single row
        input2 = "123456"
        expected2 = [[1, 2, 3, 4, 5, 6]]
        assert parse(input2) == expected2, "Test 2 failed: Single row"
        print("✓ Test 2 passed: Single row")
        
        # Test 3: Empty string
        input3 = ""
        expected3 = []
        assert parse(input3) == expected3, "Test 3 failed: Empty string"
        print("✓ Test 3 passed: Empty string")
        
        # Test 4: Multiple rows with varying lengths
        input4 = """123
        45678
        9"""
        expected4 = [[1, 2, 3], [4, 5, 6, 7, 8], [9]]
        assert parse(input4) == expected4, "Test 4 failed: Varying lengths"
        print("✓ Test 4 passed: Varying lengths")
        
        # Test 5: Rows with spaces (should be ignored)
        input5 = """1 2 3
        4 5 6"""
        expected5 = [[1, 2, 3], [4, 5, 6]]
        assert parse(input5) == expected5, "Test 5 failed: Spaces in input"
        print("✓ Test 5 passed: Spaces in input")
            
        # Test 6: Single digit
        input6 = "7"
        expected6 = [[7]]
        assert parse(input6) == expected6, "Test 6 failed: Single digit"
        print("✓ Test 6 passed: Single digit")
        
    
    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 357
    
    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'='*50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'='*50}")
        assert result == 17109
    
    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 3121910778619
    
    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'='*50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'='*50}")
        assert result == 169347417057382


# Add unit tests for helper functions below
def test_helper_example():
    """Example test for a helper function."""
    # from puzzle import helper_function
    # result = helper_function(test_input)
    # assert result == expected_output
    pass


if __name__ == "__main__":
    # Run with: python test_puzzle_day_3.py
    # Or: pytest test_puzzle_day_3.py -v -s
    pytest.main([__file__, "-v", "-s"])