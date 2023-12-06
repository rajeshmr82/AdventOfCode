import re
from functools import reduce
import numpy as np

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    lines = input.splitlines()
    card_map = {}
    for line in lines:
        if line.strip():
            card_number, cards = line.split(':')
            card_number = int(card_number.split()[1])
            cards = cards.strip().split('|')
            winning = list(map(int, cards[0].split()))
            mycard = list(map(int, cards[1].split()))
            card_map[card_number] = {'winning': set(winning), 'set': set(mycard)}
    return card_map


def solvePartOne(card_map):
    total = 0

    for card, values in card_map.items():
        matching_cards = len(values['winning'].intersection(values['set']))
        if matching_cards > 0:
            total += 2 ** (matching_cards - 1)

    return total

def solvePartTwo(card_map):
    total = 0
    instances = {key: 1 for key in card_map.keys()}
    for card, values in card_map.items():
        matching_cards = len(values['winning'].intersection(values['set']))
        if matching_cards > 0:
            for i in range(1, matching_cards+1):
                instances[int(card)+i] += instances[int(card)]

    total = sum(instances.values())
    return total