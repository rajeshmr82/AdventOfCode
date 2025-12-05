"""
Advent of Code 2025 - Day 1
Author: Rajesh M R
"""
from pathlib import Path


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """Parse the raw input into list of (direction, distance) tuples."""
    lines = raw_input.splitlines()
    if not lines or lines == ['']:
        return []
    return [(line[0], int(line[1:])) for line in lines]


def update_position(position, distance, direction):
    """Update position on circular dial after a rotation."""
    delta = distance if direction == 'R' else -distance
    return (position + delta) % 100


def solve_part_one(data):
    """Count how many times we land exactly on position 0."""
    position = 50
    count = 0
    
    for direction, distance in data:
        position = update_position(position, distance, direction)
        if position == 0:
            count += 1
    
    return count


def count_zeros_during_rotation(start, distance, direction):
    """
    Count how many times the dial points at 0 during a rotation.
    
    On a circular dial (0-99), count each time we pass through or land on 0.
    Don't count if we're already starting at 0 (unless we loop back).
    """
    if distance == 0 or start == 0:
        return distance // 100 if start == 0 else 0
    
    if direction == 'R':
        # Moving clockwise: count multiples of 100 we pass
        return (start + distance) // 100 - start // 100
    
    # Moving counter-clockwise (left)
    if distance <= start:
        # Don't wrap around
        return 1 if start - distance == 0 else 0
    
    # Wrap past 0: count initial crossing plus complete loops
    zeros = 1 + (distance - start - 1) // 100
    
    # If we end exactly on 0, count that too
    if (start - distance) % 100 == 0:
        zeros += 1
    
    return zeros


def solve_part_two(data):
    """Count how many times the dial points at 0 (including during rotations)."""
    position = 50
    total_zeros = 0
    
    for direction, distance in data:
        total_zeros += count_zeros_during_rotation(position, distance, direction)
        position = update_position(position, distance, direction)
    
    return total_zeros


if __name__ == "__main__":
    raw = read_input()
    data = parse(raw)
    
    print("="*50)
    print(f"Advent of Code 2025 - Day 1")
    print("="*50)
    
    answer_one = solve_part_one(data)
    print(f"Part One: {answer_one}")
    
    answer_two = solve_part_two(data)
    print(f"Part Two: {answer_two}")
    
    print("="*50)