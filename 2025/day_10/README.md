# Advent of Code 2025 - Day 10: Machine Button Optimization

## Problem Overview

This problem involves machines with indicator lights and buttons. Each button toggles specific lights (Part 1) or increments specific counters (Part 2). The goal is to find the minimum number of button presses needed to reach target configurations.

## Part 1: Toggle Lights to Target Pattern

### Problem Statement

Each machine has:
- A set of indicator lights that can be ON or OFF
- Multiple buttons, where each button toggles a specific set of lights
- A target configuration of lights (which should be ON/OFF)

Find the minimum number of button presses to reach the target configuration from the all-OFF starting state.

### Key Insight: Linear Algebra over GF(2)

This is a **system of linear equations over the binary field GF(2)**, where:
- Addition is XOR (⊕): `1 ⊕ 1 = 0`, `1 ⊕ 0 = 1`, `0 ⊕ 0 = 0`
- Toggling is XOR operation
- Pressing a button twice cancels out: `press ⊕ press = no change`

**Mathematical Formulation:**
```
Matrix × button_presses = target (mod 2)

Where:
- Matrix[i][j] = 1 if button j affects light i, else 0
- button_presses[j] = 1 if button j is pressed (odd times), else 0
- target[i] = 1 if light i should be ON, else 0
```

### Why This Works

Since pressing a button twice has no net effect, we only care about whether each button is pressed an **odd** or **even** number of times. This reduces to binary values: 0 (even/not pressed) or 1 (odd/pressed).

**Example:**
```
Machine: [.##.] with buttons (3), (1,3), (2), (2,3), (0,2), (0,1)

Lights:     0  1  2  3
Target:     0  1  1  0

Button effects matrix:
           B0 B1 B2 B3 B4 B5 | Target
Light 0:   0  0  0  0  1  1  |  0
Light 1:   0  1  0  0  0  1  |  1
Light 2:   0  0  1  1  1  0  |  1
Light 3:   1  1  0  1  0  0  |  0

We need to solve: Which buttons to press (mod 2)?
```

### Algorithm: Gaussian Elimination over GF(2)

This is standard Gaussian elimination, but with XOR instead of subtraction:

```python
1. Build augmented matrix [A | target]
2. Forward elimination to Reduced Row Echelon Form (RREF):
   - Use XOR for row operations
   - For each column, find a pivot row with a 1
   - XOR pivot row with all other rows that have 1 in that column
3. Check for inconsistency:
   - If any row is [0 0 0 ... 0 | 1], no solution exists
4. Identify free variables (columns without pivots)
5. If no free variables → unique solution
6. If free variables exist → try all 2^k combinations
7. Return solution with minimum button presses
```

**XOR Row Operation:**
```python
# Instead of: row_i = row_i - k × row_j (real numbers)
# Use:        row_i = row_i ⊕ row_j (binary)

matrix[row] = [a ^ b for a, b in zip(matrix[row], matrix[pivot_row])]
```

### Why Try All Free Variable Combinations?

When the system is **underdetermined** (more variables than equations):
- Multiple solutions exist
- Some solutions use fewer button presses than others
- We must find the **minimum** among all valid solutions

**Example with 2 free variables:**
- Try: `free = [0, 0]`, `[0, 1]`, `[1, 0]`, `[1, 1]`
- Calculate dependent variables for each
- Pick the solution with fewest total 1s (button presses)

### Complexity

- **Time**: O(n × m²) for Gaussian elimination + O(2^k × m) for free variables
  - n = number of lights
  - m = number of buttons
  - k = number of free variables (usually small)
- **Space**: O(n × m) for the matrix

For most inputs, k is small (0-3), making the exponential search feasible.

## Part 2: Increment Counters to Target Values

### Problem Statement

Now the machines work differently:
- Instead of toggle lights, buttons **increment** specific counters
- Counters start at 0 and can be any non-negative integer
- Each counter has a **target joltage value** (positive integer)
- Buttons can be pressed **multiple times** (0, 1, 2, 3, ...)

Find the minimum total button presses to reach all target joltage values.

### Key Difference from Part 1

| Aspect | Part 1 (Toggle) | Part 2 (Increment) |
|--------|----------------|-------------------|
| Operation | XOR (mod 2) | Addition (integers) |
| Button presses | 0 or 1 (binary) | 0, 1, 2, 3, ... (non-negative integers) |
| Math field | GF(2) (binary) | Integers (ℤ) |
| Problem type | Linear equations (mod 2) | Integer Linear Programming |

**The same intuition does NOT hold!** This is now an optimization problem over integers.

### Mathematical Formulation

This is an **Integer Linear Programming (ILP)** problem:

```
Minimize: sum(x[j] for j in buttons)

Subject to:
  For each counter i:
    sum(x[j] for j where button j affects counter i) = target_joltage[i]

  x[j] >= 0 for all j (non-negative integers)
```

**Example:**
```
Machine with counters at joltages {3, 5, 4, 7}
Buttons: (0), (1,0), (2), (2,0), (0,2), (0,1)

Counter effects matrix:
             B0 B1 B2 B3 B4 B5 | Target
Counter 0:   1  1  0  1  1  1  |  3
Counter 1:   0  1  0  0  0  1  |  5
Counter 2:   0  0  1  1  1  0  |  4
Counter 3:   0  0  0  0  0  0  |  7  ← Impossible! No buttons affect it

Need to find: How many times to press each button?
```

### Why Not Use Gaussian Elimination?

Gaussian elimination over **real numbers** would give us a solution, but:
1. The solution might have **fractional values** (e.g., press button 2.5 times)
2. Rounding might **violate constraints** (computed ≠ target)
3. Rounding might **not be optimal** (not minimum presses)

**Example of failure:**
```
LP solution: x = [14.8, 0.0, 5.2, 12.8, ...]
Rounded:     x = [15,   0,   5,   13,   ...]

Verification:
  Counter 2: Expected 66, got 67 ✗ VIOLATED
  Counter 3: Expected 109, got 110 ✗ VIOLATED
```

### Solution: Integer Linear Programming

We need a proper **ILP solver** that guarantees:
- Solutions are integers
- Constraints are satisfied
- Solution is optimal (minimum)

**Using OR-Tools (Google's optimization library):**

```python
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("SCIP")

# Variables: x[j] = times button j is pressed
x = [solver.IntVar(0, solver.infinity(), f"x{j}")
     for j in range(num_buttons)]

# Objective: minimize sum of button presses
solver.Minimize(sum(x))

# Constraints: each counter must reach target
for counter_idx, target_joltage in enumerate(joltages):
    solver.Add(
        sum(x[j] for j in range(num_buttons)
            if counter_idx in buttons[j]) == target_joltage
    )

# Solve
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    return sum(int(x[j].solution_value()) for j in range(num_buttons))
```

### Why OR-Tools?

OR-Tools uses sophisticated algorithms like:
- **Branch and Bound**: Systematically explore integer solutions
- **Cutting Planes**: Add constraints to eliminate fractional solutions
- **Heuristics**: Find good solutions quickly

It's designed for exactly this type of problem and handles thousands of variables efficiently.

### Alternative: scipy.optimize.milp

Python's scipy library also has MILP (Mixed Integer Linear Programming):

```python
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

# Similar setup but with numpy arrays
result = milp(c=c, constraints=constraints, bounds=bounds,
              integrality=integrality)
```

Both work, but OR-Tools tends to be faster for larger problems.

### Complexity

For ILP problems:
- **Worst case**: Exponential O(2^m) where m is number of variables
- **Practical**: Modern solvers use sophisticated techniques
- **This problem**: Usually solves in seconds for ~100 machines with ~10 buttons each

The complexity depends heavily on the problem structure. Our problems are well-behaved because:
- Coefficients are 0 or 1 (binary matrix)
- All constraints are equalities
- Variables are non-negative integers

## Common Pitfalls

### Part 1
- ✗ Using regular arithmetic instead of XOR (mod 2 operations)
- ✗ Not trying all free variable combinations (might miss minimum)
- ✗ Forgetting that pressing a button twice = not pressing it
- ✗ Using float arithmetic (should be pure integer/binary)

### Part 2
- ✗ Thinking it's the same as Part 1 with mod 2
- ✗ Using continuous LP and rounding (won't satisfy constraints!)
- ✗ Not using a proper ILP solver
- ✗ Treating it as a binary problem (buttons can be pressed multiple times)

## Results

- **Part 1**: 449
- **Part 2**: 17,848

Both solutions sum the minimum button presses across all 162 machines in the input.

## Key Takeaways

**Part 1** is a beautiful application of linear algebra over finite fields (GF(2)). The key insight is recognizing that toggle operations are XOR, and XOR arithmetic follows different rules than regular arithmetic.

**Part 2** demonstrates why problem constraints matter. The shift from binary toggle to integer increment completely changes the problem class from "linear algebra over GF(2)" to "integer linear programming", requiring entirely different solution techniques.

**General Lesson**: Always identify the mathematical structure of your problem:
- Is it mod 2? → Use XOR and binary arithmetic
- Is it integers with optimization? → Use ILP solvers
- Is it continuous? → Use LP or calculus-based methods

The right tool makes the difference between an elegant O(n³) solution and an intractable exponential search!
