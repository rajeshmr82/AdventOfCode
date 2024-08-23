import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
from collections import deque


def readInput():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse(input):
    grid = input.strip().split("\n")
    return grid


def parse_input(grid):
    rows = len(grid)
    cols = len(grid[0])
    object_positions = {"rows": [], "cols": []}

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                object_positions["rows"].append(i)
                object_positions["cols"].append(j)

    object_positions["rows"] = set(object_positions["rows"])
    object_positions["cols"] = set(object_positions["cols"])

    return object_positions, rows, cols


def double_size(grid, rows_to_double, cols_to_double):
    # Double the rows
    new_grid = []
    for i, row in enumerate(grid):
        new_grid.append(row)
        if i in rows_to_double:
            new_grid.append(row)  # Append the same row again

    # Double the columns
    for i, row in enumerate(new_grid):
        new_row = ""
        for j, char in enumerate(row):
            new_row += char
            if j in cols_to_double:
                new_row += char  # Append the same character again
        new_grid[i] = new_row

    return new_grid


def expand_grid(input_grid):
    # Step 1: Parse the input to find object positions
    object_positions, rows, cols = parse_input(input_grid)

    # Step 2: Identify rows and columns without objects
    rows_to_double = [i for i in range(rows) if i not in object_positions["rows"]]
    cols_to_double = [j for j in range(cols) if j not in object_positions["cols"]]

    # Step 3: Double the size of rows and columns without objects
    result_grid = double_size(input_grid, rows_to_double, cols_to_double)

    return result_grid


def find_object_positions(grid):
    object_positions = []
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == "#":
                object_positions.append((row_idx, col_idx))
    return object_positions


def bfs(grid, start, end):
    if start == end:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((start[0], start[1], 0))  # (row, col, distance)
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        row, col, dist = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
                and grid[new_row][new_col] == "."
            ):
                if (new_row, new_col) == end:
                    return dist + 1

                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))

    return -1  # No path found


def compute_all_distances(grid, object_positions):
    distances = {}
    num_objects = len(object_positions)

    for i in range(num_objects):
        for j in range(i + 1, num_objects):
            start = object_positions[i]
            end = object_positions[j]
            distance = bfs(grid, start, end)
            distances[(i, j)] = distance

    return distances


def compute_all_distances_manhattan(object_positions):
    distances = {}
    num_objects = len(object_positions)

    for i in range(num_objects):
        for j in range(i + 1, num_objects):
            x1, y1 = object_positions[i]
            x2, y2 = object_positions[j]
            distance = abs(x2 - x1) + abs(y2 - y1)
            distances[(i, j)] = distance

    return distances


def sum_of_shortest_paths(object_positions):
    total_sum = 0
    num_objects = len(object_positions)

    for i in range(num_objects):
        for j in range(i + 1, num_objects):
            x1, y1 = object_positions[i]
            x2, y2 = object_positions[j]
            distance = abs(x2 - x1) + abs(y2 - y1)
            total_sum += distance

    return total_sum


def solvePartOne(input_data):
    # # Step 1: Parse the input
    # input_data = readInput()
    parsed = parse(input_data)
    grid = expand_grid(parsed)

    # Step 2: Find the object positions
    object_positions = find_object_positions(grid)

    # Step 3: Compute the sum of all shortest paths using Manhattan distance
    total_sum = sum_of_shortest_paths(object_positions)

    return total_sum


def sum_of_shortest_paths_with_factor_expansion(input_grid, factor):
    # Step 1: Parse the input to find object positions and grid dimensions
    positions, rows, cols = parse_input(input_grid)

    # Step 2: Identify rows and columns without objects
    empty_rows = [i for i in range(rows) if i not in positions["rows"]]
    empty_columns = [j for j in range(cols) if j not in positions["cols"]]
    object_positions = find_object_positions(input_grid)

    # Step 3: Calculate new positions of objects based on the empty rows and columns
    galaxies = []
    for i, j in object_positions:
        new_i = i + sum(1 for x in empty_rows if x < i) * (factor - 1)
        new_j = j + sum(1 for x in empty_columns if x < j) * (factor - 1)
        galaxies.append((new_i, new_j))

    # Step 4: Compute the sum of Manhattan distances between all pairs of objects
    total_sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total_sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )

    return total_sum


def solvePartTwo(input_data):
    parsed = parse(input_data)

    # Calculate the sum of the shortest paths after expanding the grid by a factor of 100
    computed_sum = sum_of_shortest_paths_with_factor_expansion(parsed, 1000000)

    return computed_sum
