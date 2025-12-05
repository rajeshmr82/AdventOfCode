"""
Comprehensive Tests for Advent of Code 2025 - Day 1
Author: Rajesh M R
"""
import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two


# Sample input from problem description
SAMPLE_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


class TestDay01:
    """Test cases for Day 1 solutions."""
    
    def test_parse_sample(self):
        """Test parsing with sample data."""
        if SAMPLE_INPUT:
            result = parse(SAMPLE_INPUT)
            assert result is not None
            assert len(result) == 10
            assert result[0] == ('L', 68)
            assert result[1] == ('L', 30)
    
    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 3
    
    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'='*50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'='*50}")
        assert result == 1023
    
    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 6
    
    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'='*50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'='*50}")
        assert result == 5899


class TestPartTwoBoundaryCases:
    """Specific test cases for part two boundary crossing logic."""
    
    def test_single_complete_rotation_right(self):
        """Test a single complete rotation to the right."""
        # Start at 50, move right 250
        # 50 → 300: crosses boundaries at 100, 200, 300
        # Crosses 0 three times
        test_input = "R250"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Single rotation right (R250)")
        print(f"Expected: 3, Got: {result}")
        assert result == 3
    
    def test_single_complete_rotation_left(self):
        """Test a single complete rotation to the left."""
        # Start at 50 (lap 0), move left 350 to -300 (lap -3)
        # Crosses: 0, -100, -200, -300 = 4 boundaries
        test_input = "L350"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Single rotation left (L350)")
        print(f"Expected: 4, Got: {result}")
        assert result == 4
    
    def test_exact_landing_on_zero(self):
        """Test landing exactly on position 0."""
        # Start at 50 (lap 0), move right 50 → lands on 100 (lap 1)
        # Crosses 1 boundary
        test_input = "R50"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Exact landing on 0 (R50)")
        print(f"Expected: 1, Got: {result}")
        assert result == 1
    
    def test_exact_landing_on_zero_from_left(self):
        """Test landing exactly on position 0 from left."""
        # Start at 50, move left 50 → lands on 0
        # Lands exactly on boundary, counts as 1 crossing
        test_input = "L50"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Exact landing on 0 from left (L50)")
        print(f"Expected: 1, Got: {result}")
        assert result == 1

    def test_exact_landing_on_zero_from_right(self):
        """Test landing exactly on position 0 from left."""
        # Start at 50, move right 150 → lands on 0
        # Lands exactly on boundary, counts as 1 crossing
        test_input = "R150"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Exact landing on 0 from right (R150)")
        print(f"Expected: 2, Got: {result}")
        assert result == 2       
    
    def test_multiple_moves_with_crossings(self):
        """Test multiple moves with boundary crossings."""
        # Start at 50
        # R60: 50 → 110 (cross 100) → position 10, crossings: 1
        # L150: 10 → -140 (cross 0, -100) → position 60, crossings: 3
        # R100: 60 → 160 (cross 100) → position 60, crossings: 4
        test_input = """R60
L150
R100"""
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Multiple moves with crossings")
        print(f"Expected: 4, Got: {result}")
        assert result == 4
    
    def test_no_crossing(self):
        """Test moves that don't cross any boundary."""
        # Start at 50, move right 30 → position 80
        test_input = "R30"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: No crossing (R30)")
        print(f"Expected: 0, Got: {result}")
        assert result == 0
    
    def test_multiple_small_moves_no_crossing(self):
        """Test multiple small moves that don't cross boundaries."""
        # Start at 50
        # R20: 50 → 70
        # L10: 70 → 60
        # R5: 60 → 65
        test_input = """R20
L10
R5"""
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Multiple small moves, no crossing")
        print(f"Expected: 0, Got: {result}")
        assert result == 0
    
    def test_exact_100_boundary(self):
        """Test landing exactly on 100 (which is same as 0)."""
        # Start at 50, move right 150
        # 50 → 200: crosses boundaries at 100, 200
        test_input = "R150"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Cross to exactly 100 (R150)")
        print(f"Expected: 2, Got: {result}")
        assert result == 2
    
    def test_multiple_complete_rotations(self):
        """Test multiple complete rotations."""
        # Start at 50, move right 500
        # Crosses at 100, 200, 300, 400, 500
        test_input = "R500"
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Multiple complete rotations (R500)")
        print(f"Expected: 5, Got: {result}")
        assert result == 5
    
    def test_alternating_directions_with_crossings(self):
        """Test alternating directions with multiple crossings."""
        # Start at 50
        # R80: 50 → 130 (cross 100) → position 30, crossings: 1
        # L200: 30 → -170 (cross 0, -100) → position 30, crossings: 3
        # R90: 30 → 120 (cross 100) → position 20, crossings: 4
        test_input = """R80
L200
R90"""
        data = parse(test_input)
        result = solve_part_two(data)
        print(f"\nTest: Alternating directions with crossings")
        print(f"Expected: 4, Got: {result}")
        assert result == 4


class TestEdgeCases:
    """Edge case tests."""
    
    def test_empty_input(self):
        """Test with empty input."""
        test_input = ""
        data = parse(test_input)
        result = solve_part_two(data)
        assert result == 0
    
    def test_single_step_right(self):
        """Test single step right."""
        test_input = "R1"
        data = parse(test_input)
        result = solve_part_two(data)
        assert result == 0
    
    def test_single_step_left(self):
        """Test single step left."""
        test_input = "L1"
        data = parse(test_input)
        result = solve_part_two(data)
        assert result == 0


if __name__ == "__main__":
    # Run with: python test_puzzle_day_1.py
    # Or: pytest test_puzzle_day_1.py -v -s
    pytest.main([__file__, "-v", "-s"])