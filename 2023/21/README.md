# Puzzle Solution README

## Overview

This repository contains a solution for a grid-based puzzle that involves navigating through a grid and calculating reachable positions based on specific movement rules. 

## Part 1: Counting Reachable Positions

### Problem Statement

In part 1, the goal is to determine how many unique positions can be reached from a starting position in a grid after a specified number of steps. The grid may contain walls that block movement.

### Algorithm

1. **Input Parsing**:
   - The input grid is read and parsed to identify the layout and the starting position. The grid is represented as a list of strings, where each character represents either an open space or a wall.

2. **Breadth-First Search (BFS)**:
   - A BFS algorithm is employed to explore the grid from the starting position. BFS is chosen because it explores all positions at the present depth level before moving on to positions at the next depth level, ensuring that all reachable positions are found.
   - A queue is initialized with the starting position, and a set is used to track visited positions to avoid revisiting them.

3. **Exploration Logic**:
   - For each position dequeued, the algorithm checks the four possible movement directions: up, down, left, and right.
   - If a neighboring position is within the grid bounds and not blocked by a wall, it is added to the queue for further exploration.
   - The algorithm continues until all reachable positions within the specified number of steps have been explored.

4. **Counting Reachable Positions**:
   - After exploring the grid, the algorithm counts the number of unique positions that have been visited and returns this count as the output for part 1.


## Part 2: Special Case Handling and Infinite Grid

### Problem Statement

In part 2, the challenge is to determine the number of reachable positions after a larger number of steps, specifically 26,501,365 steps. Additionally, the algorithm must identify if the grid configuration falls into a special case that requires different handling.

### Algorithm

1. **Input Parsing**:
   - Similar to part 1, the input grid is parsed to identify the starting position and the layout of the grid.

2. **Reachable Positions Calculation**:
   - The algorithm uses a modified BFS to calculate reachable positions based on the number of steps. It keeps track of positions reached at both odd and even steps separately.
   - The BFS is implemented in a way that allows it to explore all reachable positions efficiently, leveraging memoization to cache results for previously computed states.

3. **Special Case Detection**:
   - The algorithm checks if the grid meets specific conditions to determine if it falls into a special case. The conditions include:
     - The grid must be square (same number of rows and columns).
     - The grid size must be odd.
     - The number of steps must satisfy a specific modular condition.
   - If the grid is determined to be a special case, the algorithm performs additional checks (e.g., verifying a diamond pattern) to confirm the special case.

4. **Output**:
   - If the grid is a special case, a message indicating that special case handling is needed is returned.
   - Otherwise, the algorithm returns the count of reachable positions after the specified number of steps.


