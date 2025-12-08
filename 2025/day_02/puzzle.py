"""
Advent of Code 2025 - Day 2
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
    
    """
    return [tuple(map(int, pair.split('-'))) for pair in raw_input.split(',')]

def sum_invalid_ids(start, end):
    total = 0
    k = 1
    
    while True:
        multiplier = 10 ** k + 1
        min_doubled = (10 ** (k - 1)) * multiplier
        
        # If smallest possible doubled number exceeds end, we're done
        if min_doubled > end:
            break
        
        # Range of valid k-digit patterns (no leading zeros)
        min_pattern = 10 ** (k - 1)
        max_pattern = 10 ** k - 1
        
        # Find patterns whose doubled values fall in [start, end]
        first_pattern = max(min_pattern, (start + multiplier - 1) // multiplier)
        last_pattern = min(max_pattern, end // multiplier)
        
        if first_pattern <= last_pattern:
            # Sum of patterns from first_pattern to last_pattern
            # Using arithmetic series: sum = n * (first + last) / 2
            n = last_pattern - first_pattern + 1
            sum_of_patterns = n * (first_pattern + last_pattern) // 2
            
            # Each pattern contributes: pattern × multiplier
            total += sum_of_patterns * multiplier
        
        k += 1
    
    return total

def solve_part_one(data):
    """
    Solve part one of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        The answer to part one
    """
    return sum(sum_invalid_ids(start, end) for start, end in data)


def solve_part_two(data):
    """
    Solve part two of the puzzle.
    
    Args:
        data: Parsed input data
    
    Returns:
        The answer to part two
    """
    # TODO: Implement solution
    result = None
    return result


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)
    
    print("="*50)
    print(f"Advent of Code 2025 - Day 2")
    print("="*50)
    
    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")
    
    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")
    
    print("="*50)