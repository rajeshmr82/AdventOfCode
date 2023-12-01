import unittest
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

class TestDay(unittest.TestCase):
    def test_basic_parse(self):
        data = puzzle.parse(TEST_INPUT)
        self.assertEqual(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f","treb7uchet"], data)

    def test_basic_sum_of_calibrationvalues(self):
        data = puzzle.parse(TEST_INPUT)
        self.assertEqual(142, puzzle.solvePartA(data))

    def test_double_digit_sum_of_calibrationvalues(self):
        data = puzzle.parse(TEST_INPUT_DOUBLED_IGIT)
        self.assertEqual(198, puzzle.solvePartA(data))

    def test_single_digit_sum_of_calibrationvalues(self):
        data = puzzle.parse(TEST_INPUT_SINGLE_IGIT)
        self.assertEqual(286, puzzle.solvePartA(data))             

    def test_pass_solveA(self):
        print('Solve Part A:')
        input = puzzle.readInput()
        answer = puzzle.solvePartA(input)
        print(answer)
        self.assertEqual(55488, answer)

    def test_sum_of_calibrationvalues_with_digits_as_text(self):
        testInput = puzzle.parse(TEST_INPUT_DIGITS_AS_TEXT)
        answer = puzzle.solvePartB(testInput)
        self.assertEqual(281, answer)      

    def test_sum_of_calibrationvalues_with_two_digits_overlap_as_text(self):
        testInput = puzzle.parse(TEST_INPUT_DIGITS_OVERLAPPING_WORDS_AS_TEXT)
        answer = puzzle.solvePartB(testInput)
        self.assertEqual(162, answer)   

    def test_pass_solveB(self):
        print('Solve Part B:')
        input = puzzle.readInput()
        answer = puzzle.solvePartB(input)
        print(answer)
        self.assertEqual(55614, answer)         


if __name__ == '__main__':
    unittest.main()