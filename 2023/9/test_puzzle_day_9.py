import pytest
import puzzle

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def test_parse():
    history = puzzle.parse(TEST_INPUT)
    assert [[0, 3, 6, 9, 12, 15], 
            [1, 3, 6, 10, 15, 21], 
            [10, 13, 16, 21, 30, 45]] == history

def test_predict_next():
    test_cases = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]
    expected = [18, 28, 68]
    for i, sequence in enumerate(test_cases):
        next_number = puzzle.predict_next_number(sequence)
        assert expected[i] == next_number

def test_basic_sum_of_prediction():
    answer = puzzle.solvePartOne(TEST_INPUT)
    assert 114 == answer

def test_solveOne(capsys):
    print("Solving Part One:")
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f"Part One : {answer}")
    assert 1696140818 == answer

def test_predict_previous():
    sequence = [10, 13, 16, 21, 30, 45]
    previous_number = puzzle.predict_previous_number(sequence)
    assert 5 == previous_number

def test_basic_sum_of_prev_prediction():
    answer = puzzle.solvePartTwo(TEST_INPUT)
    assert 2 == answer

def test_solveTwo(capsys):
    print("Solving Part Two:")
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f"Part Two : {answer}")
    assert 1152 == answer
