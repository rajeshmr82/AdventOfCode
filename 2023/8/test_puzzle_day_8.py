import pytest
import puzzle

TEST_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def test_parse():
    instructions, nodes = puzzle.parse(TEST_INPUT)
    assert instructions == 'RL'
    assert nodes == {'AAA': ('BBB', 'CCC'), 
                    'BBB': ('DDD', 'EEE'), 
                    'CCC': ('ZZZ', 'GGG'), 
                    'DDD': ('DDD', 'DDD'), 
                    'EEE': ('EEE', 'EEE'), 
                    'GGG': ('GGG', 'GGG'), 
                    'ZZZ': ('ZZZ', 'ZZZ')}

def test_basic_step_count(capsys):
    answer = puzzle.solvePartOne(TEST_INPUT)
    print(f'Part One : {answer}')
    assert answer == 2

def test_basic_step_count_with_looped_instruction_set(capsys):
    answer = puzzle.solvePartOne(TEST_INPUT2)
    print(f'Part One : {answer}')
    assert answer == 6

def test_solveOne(capsys):
    print('Solving Part One:')
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f'Part One : {answer}')
    assert answer == 17621

def test_basic_step_count_all_together():
    answer = puzzle.solvePartTwo(TEST_INPUT3)
    assert answer == 6

def test_solveTwo(capsys):
    print('Solving Part Two:')
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f'Part Two : {answer}')
    assert answer == 20685524831999