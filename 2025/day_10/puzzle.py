"""
Advent of Code 2025 - Day 10
Author: Rajesh M R
"""

import re
from pathlib import Path
from ortools.linear_solver import pywraplp


class Machine:
    """Represents a machine with indicator lights and buttons."""

    def __init__(self, target, buttons, joltages=None):
        """
        Initialize a machine.

        Args:
            target: List of bools representing target state (True = on, False = off)
            buttons: List of lists, where each inner list contains light indices
            joltages: Optional list of joltage requirements
        """
        self.target = target
        self.buttons = buttons
        self.joltages = joltages or []

    @classmethod
    def from_line(cls, line):
        """
        Parse a line and create a Machine instance.

        Format: [.##.] (3) (1,3) (2) {3,5,4,7}
        """
        # Parse target state from [.##.]
        target = [c == "#" for c in re.search(r"\[([.#]+)\]", line).group(1)]

        # Parse buttons from (3) (1,3) (2) etc.
        buttons = [[int(x) for x in m.split(",")] for m in re.findall(r"\(([0-9,]+)\)", line)]

        # Parse joltages from {3,5,4,7}
        joltage_match = re.search(r"\{([0-9,]+)\}", line)
        joltages = [int(x) for x in joltage_match.group(1).split(",")] if joltage_match else []

        return cls(target, buttons, joltages)

    def fewest_buttons(self):
        """
        Find minimum button presses to reach target state.
        Solves: Matrix × button_presses = target (mod 2)
        """
        # Build augmented matrix [A | target]
        matrix = [
            [int(light_idx in button) for button in self.buttons] + [int(self.target[light_idx])]
            for light_idx in range(len(self.target))
        ]

        solution = self._solve_gf2(matrix, len(self.buttons))
        return sum(solution) if solution else float("inf")

    def _solve_gf2(self, augmented_matrix, num_vars):
        """Solve Ax = b (mod 2) using Gaussian elimination over GF(2)."""
        matrix = [row[:] for row in augmented_matrix]
        pivot_row = 0
        pivot_cols = []

        # Forward elimination to RREF
        for col in range(num_vars):
            # Find pivot and swap
            for row in range(pivot_row, len(matrix)):
                if matrix[row][col]:
                    matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]
                    pivot_cols.append(col)
                    break
            else:
                continue

            # Eliminate using XOR
            for row in range(len(matrix)):
                if row != pivot_row and matrix[row][col]:
                    matrix[row] = [a ^ b for a, b in zip(matrix[row], matrix[pivot_row])]

            pivot_row += 1

        # Check for inconsistency
        if any(not any(row[:-1]) and row[-1] for row in matrix):
            return None

        free_vars = [i for i in range(num_vars) if i not in pivot_cols]

        if not free_vars:
            return [matrix[pivot_cols.index(col)][-1] if col in pivot_cols else 0
                    for col in range(num_vars)]

        # Try all 2^k combinations of free variables
        best_solution, min_presses = None, float("inf")

        for combo in range(1 << len(free_vars)):
            solution = [0] * num_vars
            for i, var_idx in enumerate(free_vars):
                solution[var_idx] = (combo >> i) & 1

            for i, pivot_col in enumerate(pivot_cols):
                solution[pivot_col] = (matrix[i][-1] ^ sum(matrix[i][j] & solution[j]
                                       for j in range(num_vars) if j != pivot_col)) % 2

            if sum(solution) < min_presses:
                min_presses = sum(solution)
                best_solution = solution

        return best_solution

    def fewest_buttons_joltage(self):
        """Find minimum button presses to reach joltage requirements using ILP."""
        solver = pywraplp.Solver.CreateSolver("SCIP")
        num_buttons = len(self.buttons)

        # Decision variables: x[j] = number of times button j is pressed
        x = [solver.IntVar(0, solver.infinity(), f"x{j}") for j in range(num_buttons)]

        # Objective: minimize sum of all button presses
        solver.Minimize(sum(x))

        # Constraints: for each counter i, sum of contributions == joltages[i]
        for counter_idx, target_joltage in enumerate(self.joltages):
            solver.Add(sum(x[j] for j in range(num_buttons)
                          if counter_idx in self.buttons[j]) == target_joltage)

        # Solve and return result
        status = solver.Solve()
        return sum(int(x[j].solution_value()) for j in range(num_buttons)) if status == pywraplp.Solver.OPTIMAL else float("inf")

    def __repr__(self):
        """String representation for debugging."""
        target_str = "".join("#" if x else "." for x in self.target)
        return f"Machine(target=[{target_str}], buttons={len(self.buttons)})"


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """Parse the raw input into a list of Machine objects."""
    return [Machine.from_line(line) for line in raw_input.splitlines() if line.strip()]


def solve_part_one(machines):
    """Solve part one: sum of minimum button presses for all machines."""
    return sum(machine.fewest_buttons() for machine in machines)


def solve_part_two(machines):
    """Solve part two: sum of minimum button presses for joltage configuration."""
    return sum(machine.fewest_buttons_joltage() for machine in machines)


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 10")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {answer_one}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {answer_two}")

    print("=" * 50)
