import sys
import re
from functools import reduce
import numpy as np
from typing import List, Tuple, Dict

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input: str) -> np.ndarray:
    lines = input.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    
    # Create a 2D numpy array filled with zeros
    grid = np.zeros((height, width), dtype=int)
    
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'O':
                grid[i, j] = 1
            elif char == '#':
                grid[i, j] = 2
    
    return grid

def tilt_north(grid):
    height, width = grid.shape
    for col in range(width):
        for row in range(height):
            if grid[row, col] == 1:  # If it's a rounded rock
                new_row = row
                while new_row > 0 and grid[new_row - 1, col] == 0:
                    new_row -= 1
                if new_row != row:
                    grid[new_row, col] = 1
                    grid[row, col] = 0
    return grid

def tilt_south(grid):
    return np.flip(tilt_north(np.flip(grid, axis=0)), axis=0)

def tilt_west(grid):
    return tilt_north(grid.T).T

def tilt_east(grid):
    return tilt_south(grid.T).T

def cycle(grid):
    grid = tilt_north(grid)
    grid = tilt_west(grid)
    grid = tilt_south(grid)
    grid = tilt_east(grid)
    return grid

def calculate_total_load(grid):
    height, width = grid.shape
    total_load = 0
    for row in range(height):
        load_for_row = height - row
        rounded_rocks_in_row = np.sum(grid[row] == 1)
        total_load += load_for_row * rounded_rocks_in_row
    return total_load

def solve_part_one(input: str) -> int:
    grid = parse(input)
    tilted_grid = tilt_north(grid)
    
    # Print the resulting tilted grid for debugging
    print("Resulting Tilted Grid:")
    print(tilted_grid)
    
    return calculate_total_load(tilted_grid)

def solve_part_two(input):
    grid = parse(input)
    seen_states = {}
    cycle_count = 0
    target_cycles = 1000000000

    while cycle_count < target_cycles:
        grid_tuple = tuple(map(tuple, grid))
        if grid_tuple in seen_states:
            cycle_length = cycle_count - seen_states[grid_tuple]
            remaining_cycles = (target_cycles - cycle_count) % cycle_length
            for _ in range(remaining_cycles):
                grid = cycle(grid)
            break
        seen_states[grid_tuple] = cycle_count
        grid = cycle(grid)
        cycle_count += 1

    return calculate_total_load(grid)


