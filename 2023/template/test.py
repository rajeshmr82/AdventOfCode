import unittest
import puzzle

TEST_INPUT = """"""


class TestDay(unittest.TestCase):
    def test_parse(self):
        self.assertEqual([], None)

    def test_pass_solveOne(self):
        print('Solving Part One:')
        input = puzzle.readInput()
        answer = puzzle.solvePartOne(input)
        print(f'Part One : {answer}')
        # self.assertEqual(0, answer)


    def test_pass_solveTwo(self):
        print('Solving Part Two:')
        input = puzzle.readInput()
        answer = puzzle.solvePartTwo(input)
        print(f'Part Two : {answer}')
        # self.assertEqual(0, answer)

if __name__ == '__main__':
    unittest.main()