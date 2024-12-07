import pytest
import numpy as np
import puzzle

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
        
        result = puzzle.parse(input_str.strip())
        pytest.assume(len(result) == 1)
        pytest.assume(np.array_equal(result[0].data, expected))

    def test_parse_multiple_patterns(self, sample_patterns):
        result = puzzle.parse(sample_patterns.strip())
        pytest.assume(len(result) == 2)

    def test_parse_empty_input(self):
        input_str = ""
        result = puzzle.parse(input_str)
        pytest.assume(len(result) == 0)

    def test_parse_single_line_pattern(self):
        input_str = "#.##..##."
        expected = np.array([['#', '.', '#', '#', '.', '.', '#', '#', '.']])
        
        result = puzzle.parse(input_str)
        pytest.assume(len(result) == 1)
        pytest.assume(np.array_equal(result[0].data, expected))

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
""", (puzzle.VERTICAL, 5)),
        ("""
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""", (puzzle.HORIZONTAL, 4)),
    ])
    def test_find_reflection(self, input_str, expected_reflection):
        puzzle = puzzle.Puzzle.from_string(input_str.strip())
        result = puzzle.find_reflections()
        pytest.assume(expected_reflection in result)

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
        puzzle = puzzle.Puzzle.from_string(input_str.strip())
        result = puzzle.find_reflections()
        pytest.assume(len(result) == 0)

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
        puzzle = puzzle.Puzzle.from_string(input_str.strip())
        result = puzzle.puzzle.find_smudged_reflection()
        pytest.assume(result == (puzzle.HORIZONTAL, 3))

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
        puzzle = puzzle.Puzzle.from_string(input_str.strip())
        result = puzzle.find_smudged_reflection()
        pytest.assume(result == (puzzle.HORIZONTAL, 1))

    @pytest.mark.parametrize("input_str, expected_reflection", [
        ("""
#...#
#...#
##.##
##.##
#..##
""", (puzzle.HORIZONTAL, 3)),
        ("""
#####
.....
..#..
#####
#####
""", (puzzle.HORIZONTAL, 2)),
    ])
    def test_find_smudged_reflection_edge_cases(self, input_str, expected_reflection):
        puzzle = puzzle.Puzzle.from_string(input_str.strip())
        result = puzzle.find_smudged_reflection()
        pytest.assume(result == expected_reflection, f"Expected {expected_reflection}, but got {result}")

class TestReflectionSum:
    def test_calculate_reflection_sum(self, sample_patterns):
        puzzles = puzzle.parse(sample_patterns.strip())
        result = puzzle.calculate_reflection_sum(puzzles)
        pytest.assume(result == 405)

    def test_calculate_reflection_sum_with_smudge(self, sample_patterns):
        puzzles = puzzle.parse(sample_patterns.strip())
        result = puzzle.calculate_reflection_sum(puzzles, use_smudge=True)
        pytest.assume(result == 400)

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
        puzzles = puzzle.parse(input_str.strip())
        result = puzzle.calculate_reflection_sum(puzzles)
        pytest.assume(result == 709)

        result_with_smudge = puzzle.calculate_reflection_sum(puzzles, use_smudge=True)
        pytest.assume(result_with_smudge == 800)

class TestSolutions:
    def test_solvePartOne(self):
        result = puzzle.solvePartOne(puzzle.readInput())
        pytest.assume(result == 27300)

    def test_solvePartTwo(self):
        result = puzzle.solvePartTwo(puzzle.readInput())
        pytest.assume(result == 29276)