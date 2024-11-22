import pytest
import puzzle

TEST_INPUT = """
Time:      7  15   30
Distance:  9  40  200
"""

def test_parse():
    races = puzzle.parse(TEST_INPUT)
    assert races == [{'Time': 7, 'Distance': 9}, {'Time': 15, 'Distance': 40}, {'Time': 30, 'Distance': 200}]

def test_max_distance_ways():
    max_dist, ways = puzzle.max_distance_ways(7, 7, 9, 0)
    assert ways == 4

def test_basic_count_ways_product():
    answer = puzzle.solvePartOne(TEST_INPUT)
    assert answer == 288

def test_pass_solveOne(capsys):
    print('Solving Part One:')
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f'Part One : {answer}')
    assert answer == 771628

def test_parse_kerning():
    race = puzzle.parse_with_kerning(TEST_INPUT)
    assert race == {'Time': 71530, 'Distance': 940200}

def test_basic_count_ways():
    answer = puzzle.solvePartTwo(TEST_INPUT)
    assert answer == 71503

def test_pass_solveTwo(capsys):
    print('Solving Part Two:')
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f'Part Two : {answer}')
    # assert answer == 0  # Commented out as in original