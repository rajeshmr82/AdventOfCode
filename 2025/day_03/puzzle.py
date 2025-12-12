"""
Advent of Code 2025 - Day 3
Author: Rajesh M R
"""
from pathlib import Path


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """
    Parse the raw input into a usable format.
    
    Common patterns:
    - lines = raw_input.splitlines()
    - numbers = [int(x) for x in raw_input.split()]
    - grid = [list(line) for line in raw_input.splitlines()]
    - blocks = raw_input.split('\\n\\n')
    """
    return [[int(char) for char in line.strip() if char.isdigit()] 
            for line in raw_input.strip().splitlines()]

def find_max_k_digits(line, k):
    result = 0
    start = 0
    
    for pos in range(k):
        # Must leave enough digits for remaining positions
        end = len(line) - (k - pos - 1)
        
        # Find largest digit in valid range
        max_digit = max(line[start:end])
        max_index = line.index(max_digit, start)
        
        result = result * 10 + max_digit
        start = max_index + 1
    
    return result

def solve_part_one(data):
    """
    Solve part one of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        The answer to part one
    """
    return sum(find_max_k_digits(line, k=2) for line in data)


def solve_part_two(data):
    """
    Solve part two of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        The answer to part two
    """
    return sum(find_max_k_digits(line, k=12) for line in data)


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)
    
    print("="*50)
    print(f"Advent of Code 2025 - Day 3")
    print("="*50)
    
    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")
    
    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")
    
    print("="*50)