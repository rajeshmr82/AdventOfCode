import unittest
import puzzle

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


class TestDay(unittest.TestCase):
    def test_parse(self):
        history = puzzle.parse(TEST_INPUT)
        self.assertEqual(
            [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]],
            history,
        )

    def test_predict_next(self):
        test_cases = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]
        expected = [18, 28, 68]
        for i, sequence in enumerate(test_cases):
            next_number = puzzle.predict_next_number(sequence)
            self.assertEqual(expected[i], next_number)

    def test_pass_basic_sum_of_prediction(self):
        answer = puzzle.solvePartOne(TEST_INPUT)
        self.assertEqual(114, answer)

    def test_pass_solveOne(self):
        print("Solving Part One:")
        input = puzzle.readInput()
        answer = puzzle.solvePartOne(input)
        print(f"Part One : {answer}")
        self.assertEqual(1696140818, answer)

    def test_predict_previous(self):
        sequence = [10, 13, 16, 21, 30, 45]
        previous_number = puzzle.predict_previous_number(sequence)
        self.assertEqual(5, previous_number)

    def test_pass_basic_sum_of_prev_prediction(self):
        answer = puzzle.solvePartTwo(TEST_INPUT)
        self.assertEqual(2, answer)

    def test_pass_solveTwo(self):
        print("Solving Part Two:")
        input = puzzle.readInput()
        answer = puzzle.solvePartTwo(input)
        print(f"Part Two : {answer}")
        self.assertEqual(1152, answer)


if __name__ == "__main__":
    unittest.main()
