import pytest
import puzzle

TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def test_basic_parse():
    card_map = puzzle.parse(TEST_INPUT)
    assert card_map == {
        1: {'winning': {41, 48, 17, 83, 86}, 'set': {6, 9, 48, 17, 83, 53, 86, 31}},
        2: {'winning': {32, 13, 16, 20, 61}, 'set': {32, 68, 17, 82, 19, 24, 61, 30}}, 
        3: {'winning': {1, 44, 53, 21, 59}, 'set': {1, 69, 72, 14, 16, 82, 21, 63}}, 
        4: {'winning': {69, 73, 41, 84, 92}, 'set': {5, 76, 51, 84, 83, 54, 58, 59}}, 
        5: {'winning': {32, 83, 87, 26, 28}, 'set': {36, 70, 12, 82, 22, 88, 93, 30}}, 
        6: {'winning': {72, 13, 18, 56, 31}, 'set': {35, 67, 36, 74, 10, 11, 77, 23}}
    }

def test_basic_totalpoints():
    card_map = puzzle.parse(TEST_INPUT)
    answer = puzzle.solvePartOne(card_map)
    assert answer == 13

def test_pass_solveOne(capsys):
    print('Solving Part One:')
    card_map = puzzle.parse(puzzle.readInput())
    answer = puzzle.solvePartOne(card_map)
    print(f'Part One : {answer}')
    assert answer == 23750

def test_basic_recursive():
    card_map = puzzle.parse(TEST_INPUT)
    answer = puzzle.solvePartTwo(card_map)
    assert answer == 30

def test_pass_solveTwo(capsys):
    print('Solving Part Two:')
    card_map = puzzle.parse(puzzle.readInput())
    answer = puzzle.solvePartTwo(card_map)
    print(f'Part Two : {answer}')
    assert answer == 13261850