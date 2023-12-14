import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
from math import gcd

class Node:
  def __init__(self, left, right):
    self.left = left
    self.right = right

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    instructions = input.split('\n')[0].strip()
    # Define the pattern to match node connections
    # pattern = r'([A-Z]+)\s*=\s*\(([A-Z]+),\s*([A-Z]+)\)'
    pattern = r'([A-Z0-9]+)\s*=\s*\(([A-Z0-9]+),\s*([A-Z0-9]+)\)'

    # Find all matches using regex
    matches = re.findall(pattern, input)

    # Creating a dictionary to hold nodes and their connections
    nodes = {node: (left, right) for node, left, right in matches}

    return instructions, nodes

def follow_instructions(start_node, instructions, connections):
    current_node = start_node
    steps = 0

    while current_node != 'ZZZ':        
        if instructions[steps % len(instructions)] == 'L':
            current_node = connections[current_node][0]
        elif instructions[steps % len(instructions)] == 'R':
            current_node = connections[current_node][1]
        steps += 1
    return steps

def follow_instruction(instructions, connections, current_node):
    idx = 0
    while idx < len(instructions):
        if instructions[idx] == 'L':
            current_node = connections[current_node][0]  # Move to the left node
        elif instructions[idx] == 'R':
            current_node = connections[current_node][1]  # Move to the right node
        idx += 1
    return current_node

def lcm(a, b):
    return a * b // gcd(a, b)

def follow_instructions_all(start_nodes, instructions, connections):
    current_nodes = [node for node in start_nodes if node.endswith('A')]
    steps_needed = []  # List to store the steps needed for each node to reach 'Z'
    steps = 0  # Total steps taken

    while len(current_nodes) > 0:
        new_current_nodes = []  # List to store nodes that haven't reached 'Z'
        steps += len(instructions) 

        # Loop through each current node
        for current_node in current_nodes:
            for instruction in instructions:
                if instruction == 'L':
                    current_node = connections[current_node][0]  # Move to the left node
                elif instruction == 'R':
                    current_node = connections[current_node][1]  # Move to the right node
            
            if current_node.endswith('Z'):
                steps_needed.append(steps)  # Add steps needed to reach 'Z' for this node
            else:
                new_current_nodes.append(current_node)  # Node hasn't reached 'Z', continue processing

        current_nodes = new_current_nodes  # Update current nodes to those not yet reaching 'Z'

    # Calculate LCM of all step counts to find the minimum steps for all 'A'-ending nodes to reach 'Z'
    result = reduce(lcm, steps_needed)
    return result


def solvePartOne(input):
    instructions, nodes = parse(input)
    steps_taken = follow_instructions('AAA', instructions, nodes)
    return steps_taken


def solvePartTwo(input):
    instructions, nodes = parse(input)
    steps_taken = follow_instructions_all(nodes.keys(),instructions, nodes)
    return steps_taken