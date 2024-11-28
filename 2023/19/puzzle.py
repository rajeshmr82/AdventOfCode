import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
from collections import deque

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

class Pipeline:
    def __init__(self):
        self.workflows = {}

    def register_workflow(self, name, rules):
        self.workflows[name] = rules

    def evaluate_part(self, part):
        queue = deque(['in'])  # Start from the 'in' workflow

        while queue:
            current_workflow = queue.popleft()  # Get the next workflow to evaluate
            rules = self.workflows.get(current_workflow, [])

            for rule in rules:
                # Parse the rule
                if ':' in rule:
                    condition, destination = rule.split(':', 1)
                else:
                    condition = None
                    destination = rule

                # Evaluate the condition if it exists
                if condition:
                    # Replace the variable names with the part's values
                    condition = condition.replace('x', str(part['x'])) \
                                         .replace('m', str(part['m'])) \
                                         .replace('a', str(part['a'])) \
                                         .replace('s', str(part['s']))

                    # Evaluate the condition
                    if eval(condition):  # This is safe here since we control the input
                        # If the destination is a workflow, enqueue that workflow
                        if destination.strip() in self.workflows:
                            queue.append(destination.strip())
                            break  # Break to continue with the next workflow
                        else:
                            # If it's not a workflow, handle acceptance or rejection
                            if destination.strip() == 'R':
                                return False  # Part is rejected
                            elif destination.strip() == 'A':
                                return True  # Part is accepted
                else:
                    # If no condition exists, check for acceptance or rejection directly
                    if destination.strip() == 'R':
                        return False  # Part is rejected
                    elif destination.strip() == 'A':
                        return True  # Part is accepted
                    elif destination.strip() in self.workflows:
                        # If the destination is a workflow, enqueue that workflow
                        queue.append(destination.strip())

        return False  # If we exhaust the queue without accepting, the part is rejected

def parse(input_string):
    # Split the input into workflows and parts
    sections = input_string.strip().split("\n\n")
    workflows_section = sections[0].strip().splitlines()
    parts_section = sections[1].strip().splitlines()

    pipeline = Pipeline()
    for line in workflows_section:
        name, rules = line.split("{")
        name = name.strip()
        rules = rules.rstrip("}").strip().split(",")
        pipeline.register_workflow(name, [rule.strip() for rule in rules])

    parts = []
    for line in parts_section:
        # Replace '=' with ':' to convert to valid dictionary format
        line = line.strip().replace('=', ':')
        # Manually parse the string to create a dictionary
        part_dict = {}
        for item in line.strip('{}').split(','):
            key, value = item.split(':')
            part_dict[key.strip()] = int(value.strip())  # Convert value to int
        parts.append(part_dict)

    return pipeline, parts

def calculate_sum(pipeline, parts):
    total_sum = 0

    for part in parts:
        if pipeline.evaluate_part(part):
            total_sum += sum(part.values())  # Add the ratings to the total sum

    return total_sum

def solve_part_one(input):
    pipeline, parts = parse(input)
    return calculate_sum(pipeline, parts)

def solve_part_two(input):      
    result = None
    return result