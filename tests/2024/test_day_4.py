import pytest
import sys
sys.path.append('2024/day_04')
import puzzle


@pytest.fixture
def sample_input_string():
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def test_word_count(sample_input_string):
    assert puzzle.word_count(sample_input_string) == [(0, 3), (1, 1), (2, 4), (3, 3), (4, 0), (4, 6), (5, 3), (6, 2), (6, 6), (7, 1), (8, 3), (8, 10)]

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    # assert 0 == answer

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    # assert 0 == answer