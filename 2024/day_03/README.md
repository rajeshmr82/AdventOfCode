# --- Day 3: Mull It Over ---

## Overview

This repository contains a solution for a puzzle that involves processing a set of instructions defined in a specific format. The main goal is to evaluate mathematical operations based on these instructions while considering enabling and disabling conditions.


## Logic Breakdown

### Functions

1. **`read_input()`**
   - Reads the input from a file named `input.txt` located in the same directory as the script.
   - Returns the content of the file as a string.

2. **`get_pattern(input)`**
   - Uses a regular expression to find all multiplication operations in the input.
   - Each operation is in the format `mul(x, y)`, where `x` and `y` are integers.
   - Calculates the sum of the products of all found pairs.

3. **`get_all_instructions(input)`**
   - This function processes the input string to evaluate the instructions.
   - It maintains an `enabled` state that determines whether multiplication operations should be executed.
   - The function uses a regular expression to find matches for both multiplication and control commands (`don't`, `do`, `undo`).

### Detailed Logic of `get_all_instructions`

- **Initialization**: 
  - `enabled` is set to `True` initially, allowing multiplication operations to be executed.
  - `result` is initialized to `0` to accumulate the total from valid multiplications.

- **Processing Instructions**:
  - The function iterates through all matches found in the input string.
  - For each match:
    - If it matches a multiplication operation (`mul(x, y)`):
      - If `enabled` is `True`, it extracts the integers `x` and `y`, computes their product, and adds it to `result`.
    - If it matches a control command:
      - If the command is `don't`, it sets `enabled` to `False`, disabling further multiplications.
      - If the command is `do` or `undo`, it sets `enabled` to `True`, allowing multiplications to be executed again.

