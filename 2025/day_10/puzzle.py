"""
Advent of Code 2025 - Day 10
Author: Rajesh M R
"""

from pathlib import Path
import re
from ortools.linear_solver import pywraplp


class Machine:
    """
    Represents a machine with indicator lights and buttons.

    This is a system of linear equations over GF(2) (binary field),
    where toggling is XOR operation.
    """

    def __init__(self, target, buttons, joltages=None):
        """
        Initialize a machine.

        Args:
            target: List of bools representing target state (True = on, False = off)
            buttons: List of lists, where each inner list contains light indices
            joltages: Optional list of joltage requirements (can be ignored)
        """
        self.target = target
        self.num_lights = len(target)
        self.buttons = buttons
        self.joltages = joltages or []

    @classmethod
    def from_line(cls, line):
        """
        Parse a line and create a Machine instance.

        Format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

        Args:
            line: String containing machine configuration

        Returns:
            Machine instance
        """
        # Parse target state from [.##.]
        target_match = re.search(r"\[([.#]+)\]", line)
        if not target_match:
            raise ValueError(f"No target state found in line: {line}")
        target = [char == "#" for char in target_match.group(1)]

        # Parse buttons from (3) (1,3) (2) etc.
        button_matches = re.findall(r"\(([0-9,]+)\)", line)
        buttons = []
        for button_str in button_matches:
            # Split by comma and convert to integers
            indices = [int(x) for x in button_str.split(",")]
            buttons.append(indices)

        # Parse joltages from {3,5,4,7}
        joltage_match = re.search(r"\{([0-9,]+)\}", line)
        joltages = []
        if joltage_match:
            joltages = [int(x) for x in joltage_match.group(1).split(",")]

        return cls(target, buttons, joltages)

    def fewest_buttons(self):
        """
        Find the minimum number of button presses needed to reach target state.

        Solves: Matrix × button_presses = target (mod 2) using Gaussian elimination.

        Returns:
            Minimum number of button presses needed
        """
        num_buttons = len(self.buttons)

        # Build augmented matrix [A | target]
        matrix = [
            [int(light_idx in button) for button in self.buttons]
            + [int(self.target[light_idx])]
            for light_idx in range(self.num_lights)
        ]

        solution = self._solve_gf2(matrix, num_buttons)
        return sum(solution) if solution else float("inf")

    def _solve_gf2(self, augmented_matrix, num_vars):
        """
        Solve system of linear equations over GF(2) using Gaussian elimination.

        Returns:
            List of button presses [0/1] with minimum presses, or None if no solution
        """
        matrix = [row[:] for row in augmented_matrix]
        pivot_row = 0
        pivot_cols = []

        # Forward elimination to reduced row echelon form
        for col in range(num_vars):
            # Find pivot and swap
            for row in range(pivot_row, len(matrix)):
                if matrix[row][col] == 1:
                    matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]
                    pivot_cols.append(col)
                    break
            else:
                continue  # No pivot in this column

            # Eliminate all other 1s in this column using XOR
            for row in range(len(matrix)):
                if row != pivot_row and matrix[row][col] == 1:
                    matrix[row] = [
                        a ^ b for a, b in zip(matrix[row], matrix[pivot_row])
                    ]

            pivot_row += 1

        # Check for inconsistency: row of all 0s with target = 1
        if any(all(val == 0 for val in row[:-1]) and row[-1] == 1 for row in matrix):
            return None

        # Identify free variables
        free_vars = [i for i in range(num_vars) if i not in pivot_cols]

        if not free_vars:
            # Unique solution
            return [
                matrix[pivot_cols.index(col)][-1] if col in pivot_cols else 0
                for col in range(num_vars)
            ]

        # Multiple solutions: try all combinations of free variables
        best_solution = None
        min_presses = float("inf")

        for combo in range(1 << len(free_vars)):
            solution = [0] * num_vars

            # Set free variables
            for i, var_idx in enumerate(free_vars):
                solution[var_idx] = (combo >> i) & 1

            # Calculate dependent variables
            for i, pivot_col in enumerate(pivot_cols):
                solution[pivot_col] = (
                    matrix[i][-1]
                    ^ sum(
                        matrix[i][j] & solution[j]
                        for j in range(num_vars)
                        if j != pivot_col
                    )
                    % 2
                )

            # Track minimum
            presses = sum(solution)
            if presses < min_presses:
                min_presses = presses
                best_solution = solution

        return best_solution

    def fewest_buttons_joltage(self):
        """
        Find minimum button presses to reach joltage requirements.

        Solves: Matrix × button_presses = joltages (over integers, not mod 2)

        Returns:
            Minimum number of button presses needed
        """
        num_buttons = len(self.buttons)
        num_counters = len(self.joltages)

        # Build incidence matrix [A | joltages]
        matrix = [
            [int(counter_idx in button) for button in self.buttons]
            + [self.joltages[counter_idx]]
            for counter_idx in range(num_counters)
        ]

        return self._solve_integer(matrix, self.joltages, num_buttons, num_counters)

    def _solve_integer(self, incidence_matrix, joltages, num_buttons, num_counters):
        """
        Solve Ax = b for non-negative integers minimizing sum(x).

        Args:
            incidence_matrix: 2D list/array where incidence_matrix[counter_i][button_j] = 1
                            if button j affects counter i, else 0
                            Shape: (num_counters, num_buttons)
            joltages: List of target joltage values for each counter
                    Length: num_counters
            num_buttons: Number of buttons (variables)
            num_counters: Number of counters (constraints)

        Returns:
            Minimum number of button presses (integer)
            OR None if no solution exists
        """
        solver = pywraplp.Solver.CreateSolver("SCIP")

        # Decision variables: x[j] = number of times button j is pressed
        # Each variable is a non-negative integer
        x = []
        for j in range(num_buttons):
            x.append(solver.IntVar(0, solver.infinity(), f"x{j}"))

        # Objective function: minimize sum of all button presses
        objective = solver.Objective()
        for j in range(num_buttons):
            objective.SetCoefficient(x[j], 1)
        objective.SetMinimization()

        # Constraints: for each counter i, the sum of contributions must equal joltages[i]
        for i in range(num_counters):
            # Create constraint: sum of button presses that affect counter i == joltages[i]
            constraint = solver.Constraint(joltages[i], joltages[i], f"counter_{i}")

            for j in range(num_buttons):
                if incidence_matrix[i][j] == 1:
                    constraint.SetCoefficient(x[j], 1)

        # Solve the problem
        status = solver.Solve()

        # Check if optimal solution was found
        if status == pywraplp.Solver.OPTIMAL:
            # Return the minimum number of button presses
            total_presses = sum(int(x[j].solution_value()) for j in range(num_buttons))
            return total_presses
        else:
            # No feasible solution found
            return None

    def __repr__(self):
        """String representation for debugging."""
        target_str = "".join("#" if x else "." for x in self.target)
        return f"Machine(target=[{target_str}], lights={self.num_lights}, buttons={len(self.buttons)})"


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
