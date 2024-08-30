# Advent of Code 2023 - Day 14: Parabolic Reflector Dish

## Overview
This project implements a puzzle solver that processes a grid of rounded rocks ('O') and obstacles ('#'). The main functionalities include parsing the input, tilting the grid in various directions, and calculating the total load of the rocks after a series of tilts.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, which should be located in the same directory as the script.

2. **Parsing**: The `parse` function converts the input string into a 2D NumPy array, where:
   - 'O' is represented as `1`
   - '#' is represented as `2`
   - Empty spaces are represented as `0`

3. **Tilting Mechanism**:
   - The grid can be tilted in four directions: North, South, West, and East.
   - The `tilt_north` function moves the rocks upwards, filling any empty spaces below them.
   - The `tilt_south`, `tilt_west`, and `tilt_east` functions utilize the `tilt_north` function by flipping the grid to achieve the desired direction.

4. **Cycle Functionality**: The `cycle` function applies a series of tilts (North, West, South, East) to the grid, simulating a complete cycle of movements.

5. **Load Calculation**: The `calculate_total_load` function computes the total load of the rocks based on their positions in the grid. The load for each row is calculated as the height of the grid minus the row index, multiplied by the number of rounded rocks in that row.

6. **Solving Parts**:
   - `solve_part_one`: This function processes the input, applies the tilting, and calculates the total load after the first tilt.
   - `solve_part_two`: This function identifies cycles in the grid state and optimizes the calculation of the total load after a large number of cycles.

## Algorithm
The algorithm primarily relies on:
- **Grid Manipulation**: Using NumPy for efficient array operations.
- **Cycle Detection**: Storing seen states of the grid to identify when a cycle occurs, allowing for optimization in the number of iterations needed.

## Usage
To run the solver, ensure you have the required dependencies (e.g., NumPy, pytest) installed. Execute the script, and it will read from `input.txt` and print the results for both parts of the puzzle.

## Testing
The project includes unit tests using `pytest` to ensure the correctness of the parsing, tilting, and load calculation functionalities. You can run the tests with the command:
```

