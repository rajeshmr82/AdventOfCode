import unittest
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
XXX = (XXX, XXX"""


class TestDay(unittest.TestCase):
    def test_parse(self):
        instructions, nodes = puzzle.parse(TEST_INPUT)
        self.assertEqual('RL', instructions)
        self.assertEqual({'AAA': ('BBB', 'CCC'), 
                          'BBB': ('DDD', 'EEE'), 
                          'CCC': ('ZZZ', 'GGG'), 
                          'DDD': ('DDD', 'DDD'), 
                          'EEE': ('EEE', 'EEE'), 
                          'GGG': ('GGG', 'GGG'), 
                          'ZZZ': ('ZZZ', 'ZZZ')}, nodes)

    def test_pass_basic_step_count(self):
        answer = puzzle.solvePartOne(TEST_INPUT)
        print(f'Part One : {answer}')
        self.assertEqual(2, answer)

    def test_pass_basic_step_count_with_looped_instruction_set(self):
        answer = puzzle.solvePartOne(TEST_INPUT2)
        print(f'Part One : {answer}')
        self.assertEqual(6, answer)        

    def test_pass_solveOne(self):
        print('Solving Part One:')
        input = puzzle.readInput()
        answer = puzzle.solvePartOne(input)
        print(f'Part One : {answer}')
        self.assertEqual(17621, answer)

    def test_pass_basic_step_count_all_together(self):
        answer = puzzle.solvePartTwo(TEST_INPUT3)
        self.assertEqual(6, answer)  

    def test_pass_solveTwo(self):
        print('Solving Part Two:')
        input = puzzle.readInput()
        answer = puzzle.solvePartTwo(input)
        print(f'Part Two : {answer}')
        self.assertEqual(20685524831999, answer)

if __name__ == '__main__':
    unittest.main()