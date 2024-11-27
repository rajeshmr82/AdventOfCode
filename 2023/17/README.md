# Advent of Code 2023 - Day 17: Ultra Crucible Movement

## Overview
This project simulates the movement of an ultra crucible through a grid, aiming to minimize heat loss while adhering to specific movement constraints. The main functionalities include calculating the least heat loss based on the crucible's path and ensuring that the movement rules are followed.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing a grid representation of heat values.

2. **Grid Representation**:
   - Each cell in the grid represents a heat value, which contributes to the total heat loss as the ultra crucible moves through it.
   - The grid is defined as a 2D array where each element corresponds to a specific heat value.

3. **Movement Constraints**:
   - The ultra crucible can move in four directions: right, down, left, and up.
   - It must move at least 4 steps in one direction before it can turn.
   - It can move a maximum of 10 consecutive steps in a single direction.

4. **Heat Loss Calculation**:
   - The total heat loss is calculated based on the path taken by the ultra crucible through the grid.
   - The algorithm tracks the heat loss as the crucible moves from the starting position to the end position.

## Algorithm
The solution employs several key components:
- **Grid Parsing**: Efficient parsing of the input grid to identify heat values.
- **Movement Logic**: Implementation of the ultra crucible's movement rules, ensuring that the constraints are respected.
- **Path Tracking**: Keeping track of visited cells to accurately calculate the total heat loss.
- **Priority Queue**: A priority queue (min-heap) is used to explore paths with the least heat loss first, optimizing the search for the best path.

## Usage
To run the solver:
1. Ensure `input.txt` is present in the correct directory.
2. Run the script to get solutions for both parts.
3. Part 1 calculates the least heat loss for a single configuration.
4. Part 2 finds the optimal path to minimize heat loss while adhering to movement constraints.

## Testing
The project includes comprehensive pytest-based tests covering:
- Grid parsing and handling.
- Ultra crucible movement logic.
- Heat loss calculations.
- End-to-end solution verification.

Run tests with: