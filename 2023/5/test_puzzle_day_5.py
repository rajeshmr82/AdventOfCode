import pytest
import puzzle
import pandas as pd

TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def test_parse():
    seeds, maps = puzzle.parse(TEST_INPUT)
    assert seeds == [79, 14, 55, 13]

def test_basic_seed_mappings():
    answer = puzzle.solvePartOne(TEST_INPUT)
    assert answer == 35

def test_pass_solveOne(capsys):
    print('Solving Part One:')
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f'Part One : {answer}')
    assert answer == 196167384

def test_basic_seed_pair_mappings():
    answer = puzzle.solvePartTwo(TEST_INPUT)
    assert answer == 46

def test_pass_solveTwo(capsys):
    print('Solving Part Two:')
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f'Part Two : {answer}')
    assert answer == 125742456