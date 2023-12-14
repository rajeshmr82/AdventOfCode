import unittest
import puzzle

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


class TestDay(unittest.TestCase):
    def test_parse(self):
        hands = puzzle.parse(TEST_INPUT)
        self.assertEqual([{'hand':'32T3K', 'bid': 765},
                          {'hand':'T55J5', 'bid': 684},
                          {'hand':'KK677', 'bid': 28},
                          {'hand':'KTJJT', 'bid': 220},
                          {'hand':'QQQJA', 'bid': 483}
                          ], hands)

    def test_identify_hand_type_FIVE_OF_A_KIND(self):
        hand = puzzle.identify_hand_type('AAAAA')
        self.assertEqual(puzzle.HandType.FIVE_OF_A_KIND, hand)

    def test_identify_hand_type_FOUR_OF_A_KIND(self):
        hand = puzzle.identify_hand_type('AA8AA')
        self.assertEqual(puzzle.HandType.FOUR_OF_A_KIND, hand)

    def test_identify_hand_type_FULL_HOUSE(self):
        hand = puzzle.identify_hand_type('23332')
        self.assertEqual(puzzle.HandType.FULL_HOUSE, hand)

    def test_identify_hand_type_THREE_OF_A_KIND(self):
        hand = puzzle.identify_hand_type('TTT98')
        self.assertEqual(puzzle.HandType.THREE_OF_A_KIND, hand)

    def test_identify_hand_type_TWO_PAIR(self):
        hand = puzzle.identify_hand_type('23432')
        self.assertEqual(puzzle.HandType.TWO_PAIR, hand)

    def test_identify_hand_type_ONE_PAIR(self):
        hand = puzzle.identify_hand_type('A23A4')
        self.assertEqual(puzzle.HandType.ONE_PAIR, hand)

    def test_identify_hand_type_HIGH_CARD(self):
        hand = puzzle.identify_hand_type('23456')
        self.assertEqual(puzzle.HandType.HIGH_CARD, hand)


    def test_rank_hands(self):
        hands = puzzle.parse(TEST_INPUT)
        ranked_hands =  puzzle.rank_hands(hands)

        expected = [{'hand':'32T3K', 'bid': 765, 'rank':1},
                    {'hand':'KTJJT', 'bid': 220,'rank':2},
                    {'hand':'KK677', 'bid': 28, 'rank':3},
                    {'hand':'T55J5', 'bid': 684, 'rank':4},
                    {'hand':'QQQJA', 'bid': 483, 'rank':5}
                ]

        for item1, item2 in zip(ranked_hands, expected):
            self.assertEqual(item1['hand'], item2['hand'])
            self.assertEqual(item1['rank'], item2['rank'])

    def test_pass_basic_winning(self):
        hands = puzzle.parse(TEST_INPUT)
        answer = puzzle.solvePartOne(hands)
        self.assertEqual(6440, answer)

    def test_pass_solveOne(self):
        print('Solving Part One:')
        input = puzzle.readInput()
        hands = puzzle.parse(input)
        answer = puzzle.solvePartOne(hands)
        print(f'Part One : {answer}')
        self.assertEqual(246424613, answer)

    def test_identify_hand_type_with_joker_FIVE_OF_A_KIND(self):
        hand = puzzle.identify_hand_type_with_joker('QJJQJ')
        self.assertEqual(puzzle.HandType.FIVE_OF_A_KIND, hand)

    def test_identify_hand_type_with_joker_FOUR_OF_A_KIND(self):
        hand = puzzle.identify_hand_type_with_joker('T55J5')
        self.assertEqual(puzzle.HandType.FOUR_OF_A_KIND, hand)

    def test_identify_hand_type_with_joker_TWO_PAIR(self):
        hand = puzzle.identify_hand_type_with_joker('KK677')
        self.assertEqual(puzzle.HandType.TWO_PAIR, hand)

    def test_identify_hand_type_with_joker_ONE_PAIR(self):
        hand = puzzle.identify_hand_type_with_joker('32T3K')
        self.assertEqual(puzzle.HandType.ONE_PAIR, hand)

    def test_pass_basic_winning_with_joker(self):
        hands = puzzle.parse(TEST_INPUT)
        answer = puzzle.solvePartTwo(hands)
        self.assertEqual(5905, answer)

    def test_pass_solveTwo(self):
        print('Solving Part Two:')
        input = puzzle.readInput()
        hands = puzzle.parse(input)
        answer = puzzle.solvePartTwo(hands)
        print(f'Part Two : {answer}')
        self.assertEqual(248256639, answer)

if __name__ == '__main__':
    unittest.main()