import unittest
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


class TestDay(unittest.TestCase):
    def test_parse(self):
        seeds,maps = puzzle.parse(TEST_INPUT)
        self.assertEqual([79 ,14 ,55, 13], seeds)
        
    def test_basic_seed_mappings(self):
        answer = puzzle.solvePartOne(TEST_INPUT)
        self.assertEqual(35, answer)

    def test_pass_solveOne(self):
        print('Solving Part One:')
        input = puzzle.readInput()
        answer = puzzle.solvePartOne(input)
        print(f'Part One : {answer}')
        self.assertEqual(196167384, answer)

    def test_basic_seed_pair_mappings(self):
        answer = puzzle.solvePartTwo(TEST_INPUT)
        self.assertEqual(46, answer)

    def test_pass_solveTwo(self):
        print('Solving Part Two:')
        input = puzzle.readInput()
        answer = puzzle.solvePartTwo(input)
        print(f'Part Two : {answer}')
        self.assertEqual(125742456, answer)

if __name__ == '__main__':
    unittest.main()