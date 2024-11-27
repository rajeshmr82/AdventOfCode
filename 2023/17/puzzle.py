import sys
import re
from functools import reduce
import numpy as np
import pandas as pd

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input_string):
    # Split the input string into lines
    lines = input_string.strip().splitlines()
    # Convert each line into a list of integers
    matrix = [[int(char) for char in line] for line in lines]
    return matrix

import heapq

def calculate_least_heat_loss(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue for BFS (min-heap)
    pq = []
    # Start from the top-left corner (0, 0)
    heapq.heappush(pq, (0, 0, 0, -1, 0, [(0, 0)]))  # (current heat loss, x, y, last direction, steps in current direction, path)
    
    # Visited set to keep track of visited cells
    visited = set()
    
    while pq:
        current_loss, x, y, last_dir, steps, path = heapq.heappop(pq)
        
        # If we reach the bottom-right corner, return the heat loss and path
        if x == rows - 1 and y == cols - 1:
            print("Optimal path:", path)  # Print the optimal path
            return current_loss
        
        # If this cell has been visited in the same direction and steps, skip it
        if (x, y, last_dir, steps) in visited:
            continue
        visited.add((x, y, last_dir, steps))
        
        # Explore all directions
        for dir_index, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            # Check if within bounds
            if 0 <= new_x < rows and 0 <= new_y < cols:
                # If moving in the same direction, increment steps
                if dir_index == last_dir:
                    new_steps = steps + 1
                else:
                    new_steps = 1  # Reset steps if changing direction
                
                # Only allow up to 3 steps in the same direction
                if new_steps <= 3:
                    # Prevent moving back to the previous cell
                    if (new_x, new_y) not in path:  # Ensure we don't go back to any visited cell
                        new_loss = current_loss + grid[new_x][new_y]
                        new_path = path + [(new_x, new_y)]  # Update the path
                        heapq.heappush(pq, (new_loss, new_x, new_y, dir_index, new_steps, new_path))
    
    return float('inf')  # If no path is found


def solve_part_one(input):
    result = None
    return result


def solve_part_two(input):      
    
    result = None
    return result