import unittest
import puzzle

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


class TestDay(unittest.TestCase):
    def test_basic_parse(self):
        data = puzzle.parse(TEST_INPUT)
        self.assertEqual(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"], data)

    def test_basic_sum_of_ids(self):
        data = puzzle.parse(TEST_INPUT)
        self.assertEqual(8, puzzle.solvePartA(data))

    def test_pass_solveA(self):
        print('Solving Part A:')
        input = puzzle.parse(puzzle.readInput())
        answer = puzzle.solvePartA(input)
        print("Part One : "+ str(answer))
        self.assertEqual(2265, answer)

    def test_basic_sum_of_power_of_sets(self):
        data = puzzle.parse(TEST_INPUT)
        answer = puzzle.solvePartB(data)
        self.assertEqual(2286, answer)

    def test_pass_solveB(self):
        print('Solving Part B:')
        input = puzzle.parse(puzzle.readInput())
        answer = puzzle.solvePartB(input)
        print("Part Two : "+ str(answer))
        self.assertEqual(64097, answer)

if __name__ == '__main__':
    unittest.main()