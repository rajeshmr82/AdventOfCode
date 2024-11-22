import pytest
import puzzle

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def test_parse():
    hands = puzzle.parse(TEST_INPUT)
    assert hands == [{'hand':'32T3K', 'bid': 765},
                    {'hand':'T55J5', 'bid': 684},
                    {'hand':'KK677', 'bid': 28},
                    {'hand':'KTJJT', 'bid': 220},
                    {'hand':'QQQJA', 'bid': 483}]

def test_identify_hand_type_FIVE_OF_A_KIND():
    hand = puzzle.identify_hand_type('AAAAA')
    assert puzzle.HandType.FIVE_OF_A_KIND == hand

def test_identify_hand_type_FOUR_OF_A_KIND():
    hand = puzzle.identify_hand_type('AA8AA')
    assert puzzle.HandType.FOUR_OF_A_KIND == hand

def test_identify_hand_type_FULL_HOUSE():
    hand = puzzle.identify_hand_type('23332')
    assert puzzle.HandType.FULL_HOUSE == hand

def test_identify_hand_type_THREE_OF_A_KIND():
    hand = puzzle.identify_hand_type('TTT98')
    assert puzzle.HandType.THREE_OF_A_KIND == hand

def test_identify_hand_type_TWO_PAIR():
    hand = puzzle.identify_hand_type('23432')
    assert puzzle.HandType.TWO_PAIR == hand

def test_identify_hand_type_ONE_PAIR():
    hand = puzzle.identify_hand_type('A23A4')
    assert puzzle.HandType.ONE_PAIR == hand

def test_identify_hand_type_HIGH_CARD():
    hand = puzzle.identify_hand_type('23456')
    assert puzzle.HandType.HIGH_CARD == hand

def test_rank_hands():
    hands = puzzle.parse(TEST_INPUT)
    ranked_hands = puzzle.rank_hands(hands)

    expected = [{'hand':'32T3K', 'bid': 765, 'rank':1},
                {'hand':'KTJJT', 'bid': 220,'rank':2},
                {'hand':'KK677', 'bid': 28, 'rank':3},
                {'hand':'T55J5', 'bid': 684, 'rank':4},
                {'hand':'QQQJA', 'bid': 483, 'rank':5}]

    for item1, item2 in zip(ranked_hands, expected):
        assert item1['hand'] == item2['hand']
        assert item1['rank'] == item2['rank']

def test_pass_basic_winning():
    hands = puzzle.parse(TEST_INPUT)
    answer = puzzle.solvePartOne(hands)
    assert 6440 == answer

def test_pass_solveOne(capsys):
    print('Solving Part One:')
    input = puzzle.readInput()
    hands = puzzle.parse(input)
    answer = puzzle.solvePartOne(hands)
    print(f'Part One : {answer}')
    assert 246424613 == answer

def test_identify_hand_type_with_joker_FIVE_OF_A_KIND():
    hand = puzzle.identify_hand_type_with_joker('QJJQJ')
    assert puzzle.HandType.FIVE_OF_A_KIND == hand

def test_identify_hand_type_with_joker_FOUR_OF_A_KIND():
    hand = puzzle.identify_hand_type_with_joker('T55J5')
    assert puzzle.HandType.FOUR_OF_A_KIND == hand

def test_identify_hand_type_with_joker_TWO_PAIR():
    hand = puzzle.identify_hand_type_with_joker('KK677')
    assert puzzle.HandType.TWO_PAIR == hand

def test_identify_hand_type_with_joker_ONE_PAIR():
    hand = puzzle.identify_hand_type_with_joker('32T3K')
    assert puzzle.HandType.ONE_PAIR == hand

def test_pass_basic_winning_with_joker():
    hands = puzzle.parse(TEST_INPUT)
    answer = puzzle.solvePartTwo(hands)
    assert 5905 == answer

def test_pass_solveTwo(capsys):
    print('Solving Part Two:')
    input = puzzle.readInput()
    hands = puzzle.parse(input)
    answer = puzzle.solvePartTwo(hands)
    print(f'Part Two : {answer}')
    assert 248256639 == answer