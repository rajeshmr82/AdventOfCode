import sys
import re
from functools import reduce
import numpy as np
import pandas as pd


def readInput():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse_sequence(sequence_str):
    return list(map(int, sequence_str.split()))


def parse(input):
    individual_sequences = input.split("\n")
    list_of_sets = [parse_sequence(sequence) for sequence in individual_sequences]
    return list_of_sets


def calculate_differences(nums):
    differences = []
    for i in range(len(nums) - 1):
        differences.append(nums[i + 1] - nums[i])
    return differences


def predict_next_number(sequence):
    result = sequence[-1]
    while len(set(sequence)) > 1:
        sequence = calculate_differences(sequence)

        result += sequence[-1]
    return result


def solvePartOne(input):
    result = 0
    history = parse(input)
    for sequence in history:
        next_number = predict_next_number(sequence)
        result += next_number
    return result


def predict_previous_number(sequence):
    sequence = sequence[::-1]  # Reverse the sequence
    result = predict_next_number(sequence)
    return result


def solvePartTwo(input):
    result = 0
    history = parse(input)
    for sequence in history:
        next_number = predict_previous_number(sequence)
        result += next_number
    return result
