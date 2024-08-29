import pytest
import numpy as np
from puzzle import Puzzle, parse, calculate_reflection_sum, solvePartOne, solvePartTwo, readInput, VERTICAL, HORIZONTAL

@pytest.fixture
def sample_patterns():
    return """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

class TestPuzzleParsing:
    def test_parse_single_pattern(self):
        input_str = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        expected = np.array([
            ['#', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['#', '.', '#', '.', '#', '#', '.', '#', '.']
        ])
        
        result = parse(input_str.strip())
        assert len(result) == 1
        assert np.array_equal(result[0].data, expected)

    def test_parse_multiple_patterns(self, sample_patterns):
        result = parse(sample_patterns.strip())
        assert len(result) == 2

    def test_parse_empty_input(self):
        input_str = ""
        result = parse(input_str)
        assert len(result) == 0

    def test_parse_single_line_pattern(self):
        input_str = "#.##..##."
        expected = np.array([['#', '.', '#', '#', '.', '.', '#', '#', '.']])
        
        result = parse(input_str)
        assert len(result) == 1
        assert np.array_equal(result[0].data, expected)

class TestReflections:
    @pytest.mark.parametrize("input_str, expected_reflection", [
        ("""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
""", (VERTICAL, 5)),
        ("""
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""", (HORIZONTAL, 4)),
    ])
    def test_find_reflection(self, input_str, expected_reflection):
        puzzle = Puzzle.from_string(input_str.strip())
        result = puzzle.find_reflections()
        assert expected_reflection in result

    def test_find_reflection_none(self):
        input_str = """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..##.
#....#..#
"""
        puzzle = Puzzle.from_string(input_str.strip())
        result = puzzle.find_reflections()
        assert len(result) == 0

class TestSmudgedReflections:
    def test_find_smudged_reflection_horizontal(self):
        input_str = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""
        puzzle = Puzzle.from_string(input_str.strip())
        result = puzzle.find_smudged_reflection()
        assert result == (HORIZONTAL, 3)

    def test_find_smudged_reflection_vertical(self):
        input_str = """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
        puzzle = Puzzle.from_string(input_str.strip())
        result = puzzle.find_smudged_reflection()
        assert result == (HORIZONTAL, 1)

    @pytest.mark.parametrize("input_str, expected_reflection", [
        ("""
#...#
#...#
##.##
##.##
#..##
""", (HORIZONTAL, 3)),
        ("""
#####
.....
..#..
#####
#####
""", (HORIZONTAL, 2)),
    ])
    def test_find_smudged_reflection_edge_cases(self, input_str, expected_reflection):
        puzzle = Puzzle.from_string(input_str.strip())
        result = puzzle.find_smudged_reflection()
        assert result == expected_reflection, f"Expected {expected_reflection}, but got {result}"

class TestReflectionSum:
    def test_calculate_reflection_sum(self, sample_patterns):
        puzzles = parse(sample_patterns.strip())
        result = calculate_reflection_sum(puzzles)
        assert result == 405

    def test_calculate_reflection_sum_with_smudge(self, sample_patterns):
        puzzles = parse(sample_patterns.strip())
        result = calculate_reflection_sum(puzzles, use_smudge=True)
        assert result == 400

    def test_calculate_reflection_sum_complex(self):
        input_str = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

.#.##.#.#
.##..##..
.#.##.#..
#......##
#......##
.#.##.#..
.##..##.#

#..#....#
###..##..
.##.#####
.##.#####
###..##..
#..#....#
#...##...
"""
        puzzles = parse(input_str.strip())
        result = calculate_reflection_sum(puzzles)
        assert result == 709

        result_with_smudge = calculate_reflection_sum(puzzles, use_smudge=True)
        assert result_with_smudge == 800

class TestSolutions:
    def test_solvePartOne(self):
        result = solvePartOne(readInput())
        assert result == 27300

    def test_solvePartTwo(self):
        result = solvePartTwo(readInput())
        assert result == 29276