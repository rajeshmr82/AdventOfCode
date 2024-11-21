import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
from typing import List, Tuple, Optional

def hash(s: str) -> int:
    """
    Calculate the HASH value of a string.
    Each character is processed by:
    1. Adding its ASCII value
    2. Multiplying by 17
    3. Taking modulo 256
    """
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse_step(step: str) -> Tuple[str, str, Optional[int]]:
    """Parse a step into (label, operation, focal_length)"""
    if step.endswith('-'):
        return step[:-1], '-', None
    label, focal_length = step.split('=')
    return label, '=', int(focal_length)

def process_sequence(sequence: str) -> List[List[Tuple[str, int]]]:
    """Process sequence and return final state of boxes"""
    boxes = [[] for _ in range(256)]
    for step in sequence.split(','):
        label, op, focal_length = parse_step(step)
        box_num = hash(label)
        
        if op == '-':
            # Remove lens with matching label if it exists
            boxes[box_num] = [(l, f) for l, f in boxes[box_num] if l != label]
        else:
            # Check if label exists
            for i, (l, _) in enumerate(boxes[box_num]):
                if l == label:
                    boxes[box_num][i] = (label, focal_length)
                    break
            else:
                # Label not found, append new lens
                boxes[box_num].append((label, focal_length))
    
    return boxes

def calculate_focusing_power(boxes: List[List[Tuple[str, int]]]) -> int:
    """Calculate total focusing power of all lenses"""
    total = 0
    for box_num, box in enumerate(boxes):
        for slot_num, (_, focal_length) in enumerate(box, 1):
            power = (box_num + 1) * slot_num * focal_length
            total += power
    return total

def solve_part_one(input: str) -> int:
    """
    Calculate the sum of HASH values for each step in the initialization sequence.
    Steps are comma-separated, ignoring newlines.
    """
    steps = [step for step in input.replace('\n', '').split(',') if step]
    return sum(hash(step) for step in steps)

def solve_part_two(input: str) -> int:
    """
    Process the initialization sequence and calculate total focusing power.
    """
    boxes = process_sequence(input.strip())
    return calculate_focusing_power(boxes)

def hash_with_steps(s: str) -> list[int]:
    """
    Returns a list of intermediate values during HASH calculation.
    For each character, returns two values:
    1. After adding ASCII value
    2. After multiplying by 17 and taking modulo 256
    """
    current = 0
    steps = []
    for c in s:
        current += ord(c)
        steps.append(current)
        current *= 17
        current %= 256
        steps.append(current)
    return steps