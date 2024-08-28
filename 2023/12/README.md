# Puzzle Solution - AdventOfCode - Day 12

This Python script solves a puzzle related to hot springs and damaged springs. It calculates the number of possible arrangements of operational and damaged springs based on given conditions.

## Implementation Details

### File Structure
- `puzzle.py`: Contains the main implementation
- `test.py`: Contains tests for the implementation
- `input.txt`: Contains the puzzle input (not shown in the provided code)

### Key Functions

1. `readInput()`
   - Reads the puzzle input from `input.txt`

2. `parse_rows(input_string)`
   - Parses the input string into a list of dictionaries
   - Each dictionary contains a "row" (spring conditions) and "rules" (grouping rules)

3. `count_combinations(row, rules)`
   - Core function that calculates the number of valid arrangements
   - Uses dynamic programming with memoization (@lru_cache) for efficiency
   - Recursively explores possible arrangements, considering:
     - Operational springs ('.')
     - Damaged springs ('#')
     - Unknown springs ('?')

4. `solvePartOne(input)`
   - Solves the first part of the puzzle
   - Calculates the sum of valid arrangements for each row in the input

5. `solvePartTwo(input)`
   - Solves the second part of the puzzle
   - Similar to Part One, but expands each row and rule set by a factor of 5

### Algorithm Explanation

The `count_combinations` function uses a recursive approach with memoization:
- It processes the row character by character
- For each character, it considers the possible states (operational, damaged, or unknown)
- It keeps track of the current group index and the count of consecutive damaged springs
- The base cases handle when all groups are processed or the row is fully explored
- The function returns the total number of valid arrangements

## Usage

To use this script:
1. Ensure you have the input in `input.txt`
2. Run `puzzle.py` to solve both parts of the puzzle
3. Use `test.py` to run the provided tests and verify the implementation

## Performance

The use of `@lru_cache` for memoization significantly improves the performance, especially for Part Two where the input is expanded.
