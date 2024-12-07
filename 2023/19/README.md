# Advent of Code 2023 - Day 19: Workflow Combinations

## Overview
This project calculates the total number of accepted combinations based on a set of workflows and conditions. The main functionalities include parsing workflow data, processing conditions, and counting valid combinations.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing workflow definitions and conditions.

2. **Workflow Definitions**:
   - Each workflow consists of a series of conditions that dictate how variables can be manipulated.
   - Conditions can include comparisons (e.g., `<`, `>`) and can lead to other workflows or acceptance.

3. **Combination Counting**:
   - The total number of accepted combinations is calculated based on the conditions defined in the workflows.
   - The algorithm tracks variable ranges and applies conditions recursively to determine valid combinations.

## Logic Explanation
The logic for counting accepted combinations involves the following key steps:

1. **Initialization**: The algorithm starts by initializing ranges for the relevant variables (e.g., `x`, `m`, `a`, `s`), typically set to a default range (e.g., 1 to 4000).

2. **Recursive Processing**: The main function processes each workflow recursively. For each condition in a workflow:
   - The condition is evaluated to determine if it leads to acceptance, rejection, or another workflow.
   - If the condition is met, the corresponding variable ranges are updated.

3. **Range Updates**: The algorithm updates the ranges based on the conditions:
   - For a condition like `x < 2000`, the upper limit of `x` is adjusted accordingly.
   - For a condition like `m > 1000`, the lower limit of `m` is adjusted.

4. **Counting Valid Combinations**: When a condition leads to acceptance, the algorithm counts the valid combinations based on the current ranges of the variables.

5. **Handling Nested Workflows**: If a condition leads to another workflow, the algorithm recursively processes that workflow, applying the same logic.

## Usage
To run the solver:
1. Ensure `input.txt` is present in the correct directory.
2. Run the script to get the total number of accepted combinations.
3. The program processes the workflows and outputs the result.

## Testing
The project includes comprehensive pytest-based tests covering:
- Input parsing and handling.
- Condition processing logic.
- Combination counting.
- End-to-end solution verification.

Run tests with:
```
pytest
```
