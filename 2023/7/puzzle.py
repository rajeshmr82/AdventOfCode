import re
from enum import Enum
from collections import Counter
from functools import cmp_to_key

class HandType(Enum):
  FIVE_OF_A_KIND = 7
  FOUR_OF_A_KIND = 6
  FULL_HOUSE = 5
  THREE_OF_A_KIND = 4
  TWO_PAIR = 3
  ONE_PAIR = 2
  HIGH_CARD = 1

CARD_ORDER = ' 23456789TJQKA'  

CARD_ORDER_WITH_JOKER = 'J23456789TQKA'

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    pattern = r"(?P<hand>\w{5})\s+(?P<bid>\d+)"
    matches = re.finditer(pattern, input, re.MULTILINE)

    result = [{'hand': match.group('hand'), 'bid': int(match.group('bid'))} for match in matches]
    return result


def identify_hand_type(hand):
    card_counts = Counter(hand)
    # Check for Five of a Kind
    if len(card_counts) == 1:
        return HandType.FIVE_OF_A_KIND
    # Check for FOUR_OF_A_KIND
    if 4 in card_counts.values():
        return HandType.FOUR_OF_A_KIND
    # Check for Full House
    if len(card_counts) == 2 and any(count == 3 for count in card_counts.values()):
        return HandType.FULL_HOUSE
    # Check for ONE_PAIR
    if len(card_counts) == 4 and any(count == 2 for count in card_counts.values()):
        return HandType.ONE_PAIR
    # Check for Three of a Kind
    if any(count == 3 for count in card_counts.values()) and len(card_counts) != 2:
        return HandType.THREE_OF_A_KIND
    # Check for HIGH_CARD
    if len(card_counts) == 5:
        return HandType.HIGH_CARD
    # Check for Two Pair
    if len(card_counts) == 3 and len(set(card_counts.values())) == 2:
        return HandType.TWO_PAIR
    # Default to HIGH_CARD
    return HandType.HIGH_CARD

def identify_hand_type_with_joker(hand):
    counts = Counter(card for card in hand if card != "J")
    counts = sorted(Counter(counts).values(), reverse=True)

    joker_count = hand.count("J")

    if not counts:
        counts = [0]

    # Check for Five of a Kind (with or without Jokers)
    if counts[0] + joker_count == 5:
        return HandType.FIVE_OF_A_KIND
    
    # Check for FOUR_OF_A_KIND (with or without Jokers)
    if counts[0] + joker_count == 4:
        return HandType.FOUR_OF_A_KIND
        
    # Check for Full House (with or without Jokers)
    if counts[0] + joker_count == 3 and counts[1] == 2:
        return HandType.FULL_HOUSE
    
    # Check for Three of a Kind (with or without Jokers)
    if counts[0] + joker_count == 3:
        return HandType.THREE_OF_A_KIND
    
     # Check for Two Pair (with or without Jokers)
    if counts[0] == 2 and (joker_count or counts[1] == 2):
        return HandType.TWO_PAIR
    
    if counts[0] == 2 or joker_count:
        return HandType.ONE_PAIR
    
    # Default to HIGH_CARD
    return HandType.HIGH_CARD


def compare(hand_A, hand_B):
    hand1_type = identify_hand_type(hand_A['hand'])
    hand2_type = identify_hand_type(hand_B['hand'])
    
    if hand1_type.value > hand2_type.value:
        return 1
    elif hand1_type.value < hand2_type.value:
        return -1
    
    # If hand types are the same, compare individual cards
    for card_A, card_B in zip(hand_A['hand'], hand_B['hand']):
        if card_A == card_B:
            continue
        if CARD_ORDER.index(card_A) > CARD_ORDER.index(card_B):
            return 1
        else:
            return -1
    
    # If all cards are identical, it's a tie
    return 0

def compare_with_joker(hand_A, hand_B):
    hand1_type = identify_hand_type_with_joker(hand_A['hand'])
    hand2_type = identify_hand_type_with_joker(hand_B['hand'])
    
    if hand1_type.value > hand2_type.value:
        return 1
    elif hand1_type.value < hand2_type.value:
        return -1
    
    # If hand types are the same, compare individual cards
    for card_A, card_B in zip(hand_A['hand'], hand_B['hand']):
        if card_A == card_B:
            continue
        if CARD_ORDER_WITH_JOKER.index(card_A) > CARD_ORDER_WITH_JOKER.index(card_B):
            return 1
        else:
            return -1
    
    # If all cards are identical, it's a tie
    return 0


def rank_hands(hands):
    hands.sort(key=cmp_to_key(compare))
    
    for i, hand in enumerate(hands):
        hand["rank"] = i + 1

    return hands

def rank_hands_with_joker(hands):
    hands.sort(key=cmp_to_key(compare_with_joker))
    
    for i, hand in enumerate(hands):
        hand["rank"] = i + 1

    return hands

def solvePartOne(hands):
    ranked_hands =  rank_hands(hands)
    result = sum(item['rank'] * item['bid'] for item in ranked_hands)
    return result


def solvePartTwo(hands):
    ranked_hands =  rank_hands_with_joker(hands)
    result = sum(item['rank'] * item['bid'] for item in ranked_hands)
    return result