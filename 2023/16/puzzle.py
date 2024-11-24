import sys
import re
from functools import reduce
import numpy as np
import pandas as pd

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    return input.strip().splitlines()

def solve_part_one(input):
    grid = parse(input)
    start = (0, 0, 'right')
    return calculate_energized_tiles(grid, start)

def solve_part_two(input):
    result = None
    return result

def calculate_energized_tiles(grid, start):
    rows = len(grid)
    cols = len(grid[0])
    
    visited = set()
    energized = set()
    
    stack = [start]  # Use a stack to manage the positions to visit

    while stack:
        row, col, direction = stack.pop()  # Get the current position and direction
        beam_state = (row, col, direction)
        
        if beam_state in visited:
            continue  # Skip if already visited
        
        visited.add(beam_state)
        
        # Check if the current position is valid before adding to energized
        if is_valid(row, col, rows, cols):
            energized.add((row, col))
            print(f"At ({row}, {col}) going {direction}, tile: {grid[row][col]}")
        
            tile = grid[row][col]
            
            if tile == '\\':
                next_direction = {'right': 'down', 'left': 'up', 
                                  'up': 'left', 'down': 'right'}[direction]
            elif tile == '/':
                next_direction = {'right': 'up', 'left': 'down', 
                                  'up': 'right', 'down': 'left'}[direction]
            elif tile == '|' and direction in ('left', 'right'):
                stack.append((row - 1, col, 'up'))  # Move up
                stack.append((row + 1, col, 'down'))  # Move down
                continue  # Skip the rest of the processing for this tile
            elif tile == '-' and direction in ('up', 'down'):
                stack.append((row, col - 1, 'left'))  # Move left
                stack.append((row, col + 1, 'right'))  # Move right
                continue  # Skip the rest of the processing for this tile
            else:
                next_direction = direction  # Continue in the same direction
            
            next_row = row + (1 if next_direction == 'down' else -1 if next_direction == 'up' else 0)
            next_col = col + (1 if next_direction == 'right' else -1 if next_direction == 'left' else 0)
            
            # Check bounds before adding the next position to the stack
            if is_valid(next_row, next_col, rows, cols):
                stack.append((next_row, next_col, next_direction))  # Add next position to stack
    
    return len(energized)

def is_valid(row, col, rows, cols):
    """Check if the position is within the grid bounds."""
    return 0 <= row < rows and 0 <= col < cols