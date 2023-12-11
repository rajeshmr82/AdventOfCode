import unittest
import puzzle

TEST_INPUT = """
Time:      7  15   30
Distance:  9  40  200
"""


class TestDay(unittest.TestCase):
    def test_parse(self):
        races = puzzle.parse(TEST_INPUT)
        self.assertEqual([{'Time': 7, 'Distance': 9}, {'Time': 15, 'Distance': 40}, {'Time': 30, 'Distance': 200}], races)     

    def test_max_distance_ways(self):
        max_dist, ways = puzzle.max_distance_ways(7, 7, 9, 0)
        self.assertEqual(4, ways)        

    def test_basic_count_ways_product(self):
        answer = puzzle.solvePartOne(TEST_INPUT)
        self.assertEqual(288, answer)            
    
    def test_pass_solveOne(self):
        print('Solving Part One:')
        input = puzzle.readInput()
        answer = puzzle.solvePartOne(input)
        print(f'Part One : {answer}')
        self.assertEqual(771628, answer)

    def test_parse_kerning(self):
        race = puzzle.parse_with_kerning(TEST_INPUT)
        self.assertEqual({'Time': 71530, 'Distance': 940200}, race)

    def test_basic_count_ways(self):
        answer = puzzle.solvePartTwo(TEST_INPUT)
        self.assertEqual(71503, answer)            

    def test_pass_solveTwo(self):
        print('Solving Part Two:')
        input = puzzle.readInput()
        answer = puzzle.solvePartTwo(input)
        print(f'Part Two : {answer}')
        # self.assertEqual(0, answer)

if __name__ == '__main__':
    unittest.main()