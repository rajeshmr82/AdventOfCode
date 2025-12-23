"""
Advent of Code 2025 - Day 6
Author: Rajesh M R
"""

from math import prod
from pathlib import Path
import re


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """
    Parse the raw input into a usable format.
    """
    lines = raw_input.strip().split("\n")

    # Extract all number lines and operator line
    number_lines = lines[:-1]
    operator_line = lines[-1]

    num_problems = len(re.findall(r"\d+", number_lines[0]))

    problems = [{"operands": [], "operator": None} for _ in range(num_problems)]

    for line in number_lines:
        numbers = [int(n) for n in re.findall(r"\d+", line)]
        for i, number in enumerate(numbers):
            problems[i]["operands"].append(number)

    operators = re.findall(r"[+*\-/]", operator_line)
    for i, operator in enumerate(operators):
        problems[i]["operator"] = operator

    return problems


def solve_part_one(data):
    """
    Solve part one of the puzzle.

    Evaluates arithmetic problems and returns the sum of all results.

    Args:
        data: List of dicts containing 'operands' (list of ints) and 'operator' ('+' or '*')

    Returns:
        int: Sum of all problem results

    Example:
        [{"operands": [2, 3], "operator": "*"}] → 6
        [{"operands": [10, 5], "operator": "+"}] → 15
    """
    operations = {"+": sum, "*": prod}

    return sum(operations[problem["operator"]](problem["operands"]) for problem in data)


def parse_to_cephal_format(raw_input):
    """Parse Cephalopod format: read columns right-to-left within each problem."""
    *number_lines, operator_line = raw_input.strip().split("\n")

    if not number_lines:
        return []

    max_length = max(len(line) for line in number_lines)
    padded = [line.ljust(max_length) for line in number_lines]

    problems = []
    operands = []

    for i in range(max_length - 1, -1, -1):
        col = [padded[j][i] for j in range(len(padded))]

        if all(c == " " for c in col):
            if operands:
                problems.append(
                    {
                        "operands": operands,
                        "operator": operator_line[i + 1].strip()
                        if i + 1 < len(operator_line)
                        else "",
                    }
                )
                operands = []
        else:
            digits = "".join(c for c in col if c.isdigit())
            if digits:
                operands.append(int(digits))

    if operands:
        problems.append(
            {
                "operands": operands,
                "operator": operator_line[0].strip() if operator_line else "",
            }
        )

    return problems


def solve_part_two(data):
    """
    Solve part two of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part two
    """
    operations = {"+": sum, "*": prod}

    return sum(operations[problem["operator"]](problem["operands"]) for problem in data)


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 6")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {{answer_one}}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {{answer_two}}")

    print("=" * 50)
