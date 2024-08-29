import numpy as np
from typing import List, Tuple, Optional

VERTICAL = 'V'
HORIZONTAL = 'H'

class Puzzle:
    def __init__(self, data: np.ndarray):
        self.data = data

    @classmethod
    def from_string(cls, input_str: str) -> 'Puzzle':
        return cls(np.array([list(line) for line in input_str.strip().split('\n')]))

    def find_reflections(self) -> List[Tuple[str, int]]:
        """Find all reflections in the puzzle."""
        reflections = []
        rows, cols = self.data.shape

        # Check for horizontal reflections
        for i in range(1, rows):
            top = self.data[:i][::-1]  # Reverse the top part
            bottom = self.data[i:]
            min_rows = min(len(top), len(bottom))
            if np.array_equal(top[:min_rows], bottom[:min_rows]):
                reflections.append((HORIZONTAL, i))

        # Check for vertical reflections
        for i in range(1, cols):
            left = np.fliplr(self.data[:, :i])  # Reverse the left part
            right = self.data[:, i:]
            min_cols = min(left.shape[1], right.shape[1])
            if np.array_equal(left[:, :min_cols], right[:, :min_cols]):
                reflections.append((VERTICAL, i))

        return reflections

    def find_smudged_reflection(self) -> Optional[Tuple[str, int]]:
        """Find a new reflection after fixing a smudge."""
        original_reflections = self.find_reflections()
        rows, cols = self.data.shape

        for i in range(rows):
            for j in range(cols):
                # Create a copy of the data and flip the bit at (i, j)
                smudged_data = self.data.copy()
                smudged_data[i, j] = '#' if smudged_data[i, j] == '.' else '.'

                # Create a new Puzzle with the smudged data
                smudged_puzzle = Puzzle(smudged_data)
                new_reflections = smudged_puzzle.find_reflections()

                # Check if we found a new reflection that's different from the original
                for new_reflection in new_reflections:
                    if new_reflection not in original_reflections:
                        return new_reflection

        return None

def parse(input: str) -> List[Puzzle]:
    """Parse the input string into a list of Puzzle objects."""
    return [Puzzle.from_string(pattern) for pattern in input.split('\n\n') if pattern.strip()]

def calculate_reflection_sum(puzzles: List[Puzzle], use_smudge: bool = False) -> int:
    """Calculate the sum of reflection values for all puzzles."""
    total = 0
    for puzzle in puzzles:
        if use_smudge:
            reflection = puzzle.find_smudged_reflection()
        else:
            reflections = puzzle.find_reflections()
            reflection = reflections[0] if reflections else None
        
        if reflection:
            direction, index = reflection
            total += index if direction == VERTICAL else 100 * index
    return total

def readInput() -> str:
    """Read the input from the file."""
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()

def solvePartOne(input_str: str) -> int:
    """Solve Part One of the puzzle."""
    puzzles = parse(input_str)
    return calculate_reflection_sum(puzzles)

def solvePartTwo(input_str: str) -> int:
    """Solve Part Two of the puzzle."""
    puzzles = parse(input_str)
    return calculate_reflection_sum(puzzles, use_smudge=True)