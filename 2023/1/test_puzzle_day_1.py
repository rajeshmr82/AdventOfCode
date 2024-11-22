import pytest
import puzzle

TEST_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_INPUT_DOUBLED_IGIT = """7jlncfksix7rjgrpglmn9
vcgkgxninerqjltdbhqzzpd4nine23
7qlfhcsnxn7fpfhjcgr6eightsevenjlpchjtzpztwo"""

TEST_INPUT_SINGLE_IGIT = """7jlncfksix7rjgrpglmn9
vcgkgxninerqjltdbhqzzpd4nine23
7qlfhcsnxn7fpfhjcgr6eightsevenjlpchjtzpztwo
8nrbjbpjpnineseven"""

TEST_INPUT_DIGITS_AS_TEXT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

TEST_INPUT_DIGITS_OVERLAPPING_WORDS_AS_TEXT = """eighthree
sevenine"""

def test_basic_parse():
    data = puzzle.parse(TEST_INPUT)
    assert data == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f","treb7uchet"]

def test_basic_sum_of_calibrationvalues():
    data = puzzle.parse(TEST_INPUT)
    assert puzzle.solvePartA(data) == 142

def test_double_digit_sum_of_calibrationvalues():
    data = puzzle.parse(TEST_INPUT_DOUBLED_IGIT)
    assert puzzle.solvePartA(data) == 198

def test_single_digit_sum_of_calibrationvalues():
    data = puzzle.parse(TEST_INPUT_SINGLE_IGIT)
    assert puzzle.solvePartA(data) == 286

def test_pass_solveA():
    print('Solve Part A:')
    input = puzzle.readInput()
    answer = puzzle.solvePartA(input)
    print(answer)
    assert answer == 55488

def test_sum_of_calibrationvalues_with_digits_as_text():
    testInput = puzzle.parse(TEST_INPUT_DIGITS_AS_TEXT)
    answer = puzzle.solvePartB(testInput)
    assert answer == 281

def test_sum_of_calibrationvalues_with_two_digits_overlap_as_text():
    testInput = puzzle.parse(TEST_INPUT_DIGITS_OVERLAPPING_WORDS_AS_TEXT)
    answer = puzzle.solvePartB(testInput)
    assert answer == 162

def test_pass_solveB():
    print('Solve Part B:')
    input = puzzle.readInput()
    answer = puzzle.solvePartB(input)
    print(answer)
    assert answer == 55614