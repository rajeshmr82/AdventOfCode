import sys
import re
from functools import reduce
import numpy as np
import pandas as pd

# Constants for directions
DIRECTIONS = ['up', 'right', 'down', 'left']
DIRECTION_VECTORS = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}

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

        if is_valid(row, col, rows, cols):
            energized.add((row, col))
            print(f"At ({row}, {col}) going {direction}, tile: {grid[row][col]}")
            
            tile = grid[row][col]
            next_direction = direction  # Default to the current direction
            
            # Determine the next direction based on the tile
            if tile == '\\':
                next_direction = {'right': 'down', 'left': 'up', 
                                  'up': 'left', 'down': 'right'}[direction]
            elif tile == '/':
                next_direction = {'right': 'up', 'left': 'down', 
                                  'up': 'right', 'down': 'left'}[direction]
            elif tile == '|':
                # If it's a splitter, add both up and down paths
                stack.append((row - 1, col, 'up'))  # Move up
                stack.append((row + 1, col, 'down'))  # Move down
                continue  # Skip the rest of the processing for this tile
            elif tile == '-':
                # If it's a horizontal splitter, continue in the same direction
                stack.append((row, col - 1, 'left'))  # Move left
                stack.append((row, col + 1, 'right'))  # Move right
                continue
            
            # Move to the next position based on the next direction
            next_row, next_col = move(row, col, next_direction)

            # Check bounds before adding the next position to the stack
            if is_valid(next_row, next_col, rows, cols):
                stack.append((next_row, next_col, next_direction))  # Add next position to stack

    print_final_grid(energized, rows, cols)
    return len(energized)

def process_tile(tile, direction):
    """Determine the next direction based on the current tile and direction."""
    if tile == '\\':
        return {'right': 'down', 'left': 'up', 'up': 'left', 'down': 'right'}[direction]
    elif tile == '/':
        return {'right': 'up', 'left': 'down', 'up': 'right', 'down': 'left'}[direction]
    return direction  # Continue in the same direction for other tiles

def move(row, col, direction):
    """Calculate the next position based on the current direction."""
    delta_row, delta_col = DIRECTION_VECTORS[direction]
    return row + delta_row, col + delta_col

def print_final_grid(energized, rows, cols):
    """Print the final energized grid."""
    for r in range(rows):
        line = ""
        for c in range(cols):
            line += "#" if (r, c) in energized else "."
        print(line)

def is_valid(row, col, rows, cols):
    """Check if the position is within the grid bounds."""
    return 0 <= row < rows and 0 <= col < cols