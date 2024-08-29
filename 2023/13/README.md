# Advent of Code 2023 - Day 13: Point of Incidence

## Problem Description

This solution addresses the Day 13 puzzle of Advent of Code 2023, titled "Point of Incidence". The puzzle involves analyzing patterns of ash (.) and rocks (#) to find lines of reflection.

### Part One
Find the line of reflection in each pattern and calculate a summary based on the position of these lines.

### Part Two
Find a new line of reflection after fixing exactly one smudge (changing a . to a # or vice versa) in each pattern.

## Implementation

The solution is implemented in Python and consists of two main files:

1. `puzzle.py`: Contains the core logic for solving the puzzle.
2. `test.py`: Contains unit tests to verify the correctness of the implementation.

### Key Components

#### Puzzle Class
The `Puzzle` class represents a single pattern and contains methods to find reflections:

- `find_reflections()`: Finds all lines of reflection in the pattern.
- `find_smudged_reflection()`: Finds a new line of reflection after fixing a single smudge.

#### Helper Functions
- `parse()`: Parses the input string into a list of `Puzzle` objects.
- `calculate_reflection_sum()`: Calculates the sum of reflection values for all puzzles.
- `readInput()`: Reads the input from the file.
- `solvePartOne()`: Solves Part One of the puzzle.
- `solvePartTwo()`: Solves Part Two of the puzzle.

### Algorithm

1. Parse the input into `Puzzle` objects.
2. For each puzzle:
   a. Find all reflections (vertical and horizontal).
   b. For Part Two, try changing each character and find a new reflection.
3. Calculate the sum based on the position of the reflection lines.

### Testing

The `test.py` file contains comprehensive unit tests for all components of the solution:

- `TestPuzzleParsing`: Tests the parsing of input strings into `Puzzle` objects.
- `TestReflections`: Tests finding reflections in various patterns.
- `TestSmudgedReflections`: Tests finding new reflections after fixing smudges.
- `TestReflectionSum`: Tests the calculation of reflection sums.
- `TestSolutions`: Tests the complete solutions for Part One and Part Two.


## Notes

- The solution uses numpy for efficient array operations.
- The implementation is designed to be modular and easily extendable for similar problems.
- Edge cases, such as reflections at the edges of the pattern, are handled in the implementation and tested thoroughly.
