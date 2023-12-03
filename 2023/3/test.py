import unittest
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


class TestDay(unittest.TestCase):
    def test_basic_parse(self):
        data = puzzle.parse(TEST_INPUT)
        self.assertEqual([['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'], 
                          ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'], 
                          ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'], 
                          ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], 
                          ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'], 
                          ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'], 
                          ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'], 
                          ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'], 
                          ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'], 
                          ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']], data)
        
    def test_getting_number_positions(self):
        data = puzzle.parse(TEST_INPUT)
        schematic = puzzle.get_schematic(data)
        positions = puzzle.get_number_positions(schematic)
        self.assertEqual([[1, 1, 3],
                        [1, 6, 3], 
                        [3, 3, 2],
                        [3, 7, 3], 
                        [5, 1, 3], 
                        [6, 8, 2], 
                        [7, 3, 3], 
                        [8, 7, 3], 
                        [10, 2, 3], 
                        [10, 6, 3]], positions)

    def test_basic_sum_of_part_numbers(self):
        data = puzzle.parse(TEST_INPUT)
        schematic = puzzle.get_schematic(data)
        answer = puzzle.solvePartOne(schematic)
        self.assertEqual(4361, answer)

    def test_pass_solveA(self):
        print('Solving Part One:')
        data = puzzle.parse(puzzle.readInput())
        schematic = puzzle.get_schematic(data)
        answer = puzzle.solvePartOne(schematic)
        print(f'Part One : {answer}')
        self.assertEqual(536202, answer)

    def test_find_star_positions(self):
        data = puzzle.parse(TEST_INPUT)
        schematic = puzzle.get_schematic(data)
        pairs = puzzle.find_star_positions(schematic)
        self.assertEqual([(2, 4), (5, 4), (9, 6)], pairs)

    def test_basic_sum_of_gear_ratios(self):
        data = puzzle.parse(TEST_INPUT)
        schematic = puzzle.get_schematic(data)
        answer = puzzle.solvePartTwo(schematic)
        self.assertEqual(467835, answer)        

    def test_pass_solveB(self):
        print('Solving Part Two:')
        data = puzzle.parse(puzzle.readInput())
        schematic = puzzle.get_schematic(data)
        answer = puzzle.solvePartTwo(schematic)
        print(f'Part Two : {answer}')
        self.assertEqual(78272573, answer)

if __name__ == '__main__':
    unittest.main()