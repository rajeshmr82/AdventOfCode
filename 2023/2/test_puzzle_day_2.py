import pytest
import puzzle

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def test_basic_parse():
    data = puzzle.parse(TEST_INPUT)
    assert data == ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def test_basic_sum_of_ids():
    data = puzzle.parse(TEST_INPUT)
    assert puzzle.solvePartA(data) == 8

def test_pass_solveA():
    print('Solving Part A:')
    input = puzzle.parse(puzzle.readInput())
    answer = puzzle.solvePartA(input)
    print("Part One : "+ str(answer))
    assert answer == 2265

def test_basic_sum_of_power_of_sets():
    data = puzzle.parse(TEST_INPUT)
    answer = puzzle.solvePartB(data)
    assert answer == 2286

def test_pass_solveB():
    print('Solving Part B:')
    input = puzzle.parse(puzzle.readInput())
    answer = puzzle.solvePartB(input)
    print("Part Two : "+ str(answer))
    assert answer == 64097