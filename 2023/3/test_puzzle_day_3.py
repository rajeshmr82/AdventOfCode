import pytest
import puzzle

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_getting_number_positions():
    data = puzzle.parse(TEST_INPUT)
    schematic = puzzle.get_schematic(data)
    positions = puzzle.get_number_positions(schematic)
    assert positions == [[1, 1, 3],
                        [1, 6, 3], 
                        [3, 3, 2],
                        [3, 7, 3], 
                        [5, 1, 3], 
                        [6, 8, 2], 
                        [7, 3, 3], 
                        [8, 7, 3], 
                        [10, 2, 3], 
                        [10, 6, 3]]

def test_basic_sum_of_part_numbers():
    data = puzzle.parse(TEST_INPUT)
    schematic = puzzle.get_schematic(data)
    answer = puzzle.solvePartOne(schematic)
    assert answer == 4361

def test_pass_solveA(capsys):
    print('Solving Part One:')
    data = puzzle.parse(puzzle.readInput())
    schematic = puzzle.get_schematic(data)
    answer = puzzle.solvePartOne(schematic)
    print(f'Part One : {answer}')
    assert answer == 536202

def test_find_star_positions():
    data = puzzle.parse(TEST_INPUT)
    schematic = puzzle.get_schematic(data)
    pairs = puzzle.find_star_positions(schematic)
    assert pairs == [(2, 4), (5, 4), (9, 6)]

def test_basic_sum_of_gear_ratios():
    data = puzzle.parse(TEST_INPUT)
    schematic = puzzle.get_schematic(data)
    answer = puzzle.solvePartTwo(schematic)
    assert answer == 467835

def test_pass_solveB(capsys):
    print('Solving Part Two:')
    data = puzzle.parse(puzzle.readInput())
    schematic = puzzle.get_schematic(data)
    answer = puzzle.solvePartTwo(schematic)
    print(f'Part Two : {answer}')
    assert answer == 78272573