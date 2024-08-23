# Puzzle Solution - AdventOfCode - Day 11

## Overview

This repository contains the solution to a grid-based puzzle where objects are placed in a grid, and we need to compute the sum of the shortest paths between all pairs of objects. The solution consists of two parts:

1. **Part 1**: Computes the sum of shortest paths between all pairs of objects in the original grid.
2. **Part 2**: Computes the sum of shortest paths after expanding the grid by a factor of 100, specifically accounting for empty rows and columns.

## Part 1 - Solution Explanation

### Problem Statement

In Part 1, we are given a grid where each cell is either empty (`.`) or contains an object (`#`). The goal is to compute the sum of the Manhattan distances between all pairs of objects.

### Approach

1. **Parse Input**:

   - The input is parsed to extract the positions of all objects (`#`) within the grid.

2. **Calculate Manhattan Distances**:

   - For each pair of objects, the Manhattan distance is computed, which is the sum of the absolute differences of their coordinates.

3. **Sum the Distances**:
   - The distances between all pairs of objects are summed to get the final result.

### Example

For a grid like this:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The solution involves:

- Finding the positions of all objects.
- Computing the Manhattan distances between each pair of objects.
- Summing these distances to obtain the final result.

### Code

```python
def solvePartOne():
    input_data = readInput()
    object_positions, rows, cols = parse_input(input_data)
    computed_sum = sum_of_shortest_paths(object_positions)
    return computed_sum
```

## Part 2 - Solution Explanation

### Problem Statement

In Part 2, the grid is conceptually expanded by a factor of 100. Specifically, for each empty row and column, we imagine it being replaced by 100 empty rows and columns, respectively. The goal is to compute the sum of the shortest paths between all pairs of objects in this expanded grid.

### Approach

1. **Parse Input**:

   - Similar to Part 1, the positions of all objects are extracted.

2. **Identify Empty Rows and Columns**:
   We determine which rows and columns in the grid do not contain any objects.

3. **Adjust Object Positions**:
   The position of each object is adjusted based on the number of empty rows and columns before it, scaled by the factor (100).

4. **Calculate and Sum Manhattan Distances**:
   The adjusted positions are used to compute the Manhattan distances between each pair of objects.
   These distances are summed to produce the final result.

### Example

Given the same grid as in Part 1, but now considering the conceptual expansion, the solution involves:

- Identifying the empty rows and columns.
- Adjusting the positions of objects based on these empty rows and columns.
- Computing the sum of the Manhattan distances between all pairs of adjusted positions.
