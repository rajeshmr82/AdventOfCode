"""
Tests for Advent of Code 2025 - Day 6
Author: Rajesh M R
"""

import pytest
from puzzle import (
    parse_to_cephal_format,
    read_input,
    parse,
    solve_part_one,
    solve_part_two,
)


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """


class TestParseFunction:
    def test_basic_single_problem(self):
        """Test parsing the simplest case - one problem"""
        input_text = """123
 45
  6
*"""
        result = parse(input_text)

        assert len(result) == 1, "Should parse exactly 1 problem"
        assert result[0]["operands"] == [123, 45, 6]
        assert result[0]["operator"] == "*"

    def test_example_four_problems(self):
        """Test the exact example from problem description"""
        input_text = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""
        result = parse(input_text)

        assert len(result) == 4, "Should parse exactly 4 problems"

        # Problem 1: 123 * 45 * 6
        assert result[0]["operands"] == [123, 45, 6]
        assert result[0]["operator"] == "*"

        # Problem 2: 328 + 64 + 98
        assert result[1]["operands"] == [328, 64, 98]
        assert result[1]["operator"] == "+"

        # Problem 3: 51 * 387 * 215
        assert result[2]["operands"] == [51, 387, 215]
        assert result[2]["operator"] == "*"

        # Problem 4: 64 + 23 + 314
        assert result[3]["operands"] == [64, 23, 314]
        assert result[3]["operator"] == "+"

    def test_two_problems_addition_and_multiplication(self):
        """Test two problems with different operators"""
        input_text = """12 34
56 78
+  *"""
        result = parse(input_text)

        assert len(result) == 2, "Should parse 2 problems"

        assert result[0]["operands"] == [12, 56]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [34, 78]
        assert result[1]["operator"] == "*"

    def test_problems_different_widths(self):
        """Test problems with varying number widths"""
        input_text = """1  9999
2  8888
+  *"""
        result = parse(input_text)

        assert len(result) == 2, "Should parse 2 problems"

        assert result[0]["operands"] == [1, 2]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [9999, 8888]
        assert result[1]["operator"] == "*"

    def test_three_operands_per_problem(self):
        """Test problems with three numbers"""
        input_text = """100
 50
 25
+"""
        result = parse(input_text)

        assert len(result) == 1
        assert result[0]["operands"] == [100, 50, 25]
        assert result[0]["operator"] == "+"

    def test_single_operand_per_problem(self):
        """Test edge case with single operand (though mathematically odd)"""
        input_text = """42
*"""
        result = parse(input_text)

        assert len(result) == 1
        assert result[0]["operands"] == [42]
        assert result[0]["operator"] == "*"

    def test_multiple_problems_three_operands_each(self):
        """Test multiple problems each with three operands"""
        input_text = """10 20 30
20 30 40
30 40 50
+  *  +"""
        result = parse(input_text)

        assert len(result) == 3

        assert result[0]["operands"] == [10, 20, 30]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [20, 30, 40]
        assert result[1]["operator"] == "*"

        assert result[2]["operands"] == [30, 40, 50]
        assert result[2]["operator"] == "+"

    def test_single_digit_numbers(self):
        """Test parsing single-digit numbers"""
        input_text = """1 2 3
4 5 6
+ * -"""
        result = parse(input_text)

        assert len(result) == 3

        assert result[0]["operands"] == [1, 4]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [2, 5]
        assert result[1]["operator"] == "*"

        assert result[2]["operands"] == [3, 6]
        assert result[2]["operator"] == "-"

    def test_large_numbers(self):
        """Test parsing large numbers"""
        input_text = """123456 789012
111111 222222
*      +"""
        result = parse(input_text)

        assert len(result) == 2

        assert result[0]["operands"] == [123456, 111111]
        assert result[0]["operator"] == "*"

        assert result[1]["operands"] == [789012, 222222]
        assert result[1]["operator"] == "+"

    def test_varying_operand_counts(self):
        """Test that all problems have same number of operands"""
        input_text = """10 20
30 40
50 60
70 80
+  *"""
        result = parse(input_text)

        assert len(result) == 2

        assert result[0]["operands"] == [10, 30, 50, 70]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [20, 40, 60, 80]
        assert result[1]["operator"] == "*"

    def test_extra_whitespace_handling(self):
        """Test that extra whitespace between problems is handled"""
        input_text = """12   34
56   78
+    *"""
        result = parse(input_text)

        assert len(result) == 2

        assert result[0]["operands"] == [12, 56]
        assert result[0]["operator"] == "+"

        assert result[1]["operands"] == [34, 78]
        assert result[1]["operator"] == "*"

    def test_operands_are_integers_not_strings(self):
        """Test that operands are parsed as integers"""
        input_text = """123
456
+"""
        result = parse(input_text)

        assert isinstance(result[0]["operands"][0], int)
        assert isinstance(result[0]["operands"][1], int)
        assert result[0]["operands"][0] == 123
        assert result[0]["operands"][1] == 456

    def test_operator_is_string(self):
        """Test that operator is a string"""
        input_text = """10
20
*"""
        result = parse(input_text)

        assert isinstance(result[0]["operator"], str)
        assert result[0]["operator"] == "*"

    def test_all_operators_supported(self):
        """Test all common arithmetic operators"""
        input_text = """10 20 30 40
5  10 15 20
+  -  *  /"""
        result = parse(input_text)

        assert result[0]["operator"] == "+"
        assert result[1]["operator"] == "-"
        assert result[2]["operator"] == "*"
        assert result[3]["operator"] == "/"

    def test_right_aligned_numbers(self):
        """Test numbers that are right-aligned (with leading spaces)"""
        input_text = """  99   88
  77   66
  +    *"""
        result = parse(input_text)

        assert len(result) == 2
        assert result[0]["operands"] == [99, 77]
        assert result[1]["operands"] == [88, 66]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


def problem_to_tuple(problem):
    """Convert problem dict to hashable tuple for comparison"""
    return (tuple(problem["operands"]), problem["operator"])


class TestParseToCephalFormat:
    def test_all_four_problems_complete(self):
        """Test all four problems from the example together"""
        input_text = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""
        actual = parse_to_cephal_format(input_text)

        assert len(actual) == 4

        expected = [
            {"operands": [356, 24, 1], "operator": "*"},
            {"operands": [8, 248, 369], "operator": "+"},
            {"operands": [175, 581, 32], "operator": "*"},
            {"operands": [4, 431, 623], "operator": "+"},
        ]
        assert set(map(problem_to_tuple, actual)) == set(
            map(problem_to_tuple, expected)
        )

    def test_single_problem(self):
        """Test parsing a single problem"""
        input_text = """123
 45
  6
*"""
        result = parse_to_cephal_format(input_text)

        assert len(result) == 1
        assert result[0]["operands"] == [356, 24, 1]
        assert result[0]["operator"] == "*"

    def test_two_problems_single_space_separator(self):
        """Test two problems with single space column separator"""
        input_text = """12 34
56 78
+  *"""
        actual = parse_to_cephal_format(input_text)

        assert len(actual) == 2

        expected = [
            {"operands": [26, 15], "operator": "+"},
            {"operands": [48, 37], "operator": "*"},
        ]
        assert set(map(problem_to_tuple, actual)) == set(
            map(problem_to_tuple, expected)
        )

    def test_single_digit_numbers(self):
        """Test with all single-digit numbers"""
        input_text = """1 2
3 4
+ *"""
        actual = parse_to_cephal_format(input_text)

        expected = [
            {"operands": [13], "operator": "+"},
            {"operands": [24], "operator": "*"},
        ]
        assert set(map(problem_to_tuple, actual)) == set(
            map(problem_to_tuple, expected)
        )

    def test_two_digit_numbers(self):
        """Test with two-digit numbers"""
        input_text = """11 22
33 44
*  +"""

        actual = parse_to_cephal_format(input_text)

        expected = [
            {"operands": [13, 13], "operator": "*"},
            {"operands": [24, 24], "operator": "+"},
        ]
        assert set(map(problem_to_tuple, actual)) == set(
            map(problem_to_tuple, expected)
        )

    def test_operators_preserved(self):
        """Test that all operators are correctly identified"""
        input_text = """10 20 30 40
50 60 70 80
+  -  *  /"""

        actual = parse_to_cephal_format(input_text)

        expected = [
            {"operands": [0, 48], "operator": "/"},
            {"operands": [0, 37], "operator": "*"},
            {"operands": [0, 26], "operator": "-"},
            {"operands": [0, 15], "operator": "+"},
        ]
        assert set(map(problem_to_tuple, actual)) == set(
            map(problem_to_tuple, expected)
        )

    def test_large_numbers(self):
        """Test with larger numbers"""
        input_text = """123456
789012
*"""
        result = parse_to_cephal_format(input_text)

        assert len(result) == 1
        # Columns right-to-left: [6,2], [5,1], [4,0], [3,9], [2,8], [1,7]
        assert result[0]["operands"] == [62, 51, 40, 39, 28, 17]
        assert result[0]["operator"] == "*"

    def test_operands_are_integers(self):
        """Test that operands are parsed as integers, not strings"""
        input_text = """12
34
+"""
        result = parse_to_cephal_format(input_text)

        assert all(isinstance(op, int) for op in result[0]["operands"])

    def test_maintains_structure(self):
        """Test that result maintains proper dict structure"""
        input_text = """12
34
+"""
        result = parse_to_cephal_format(input_text)

        assert isinstance(result, list)
        assert isinstance(result[0], dict)
        assert "operands" in result[0]
        assert "operator" in result[0]
        assert isinstance(result[0]["operands"], list)
        assert isinstance(result[0]["operator"], str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


class TestDay06:
    """Test cases for Day 6 solutions."""

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 4277556

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 6299564383938

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse_to_cephal_format(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 3263827

    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse_to_cephal_format(raw)
        result = solve_part_two(data)
        print(f"\n{'=' * 50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 11950004808442


if __name__ == "__main__":
    # Run with: python test_puzzle_day_6.py
    # Or: pytest test_puzzle_day_6.py -v -s
    pytest.main([__file__, "-v", "-s"])
