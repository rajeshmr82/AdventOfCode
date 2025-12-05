# Advent of Code 2025 - Day 1: Circular Dial Password

## Problem Summary

You have a circular dial with positions 0-99 that starts at position 50. You're given a series of rotations in the form of `L<n>` (rotate left/counter-clockwise) or `R<n>` (rotate right/clockwise).

### Part 1
Count how many times the dial **lands on position 0** at the end of a rotation.

### Part 2
Count how many times the dial **points at position 0** - including both when it lands on 0 AND when it passes through 0 during a rotation.

## Example

```
L68  - Rotate left 68 steps from position 50 → ends at 82, passes through 0 once
L30  - Rotate left 30 steps from position 82 → ends at 52
R48  - Rotate right 48 steps from position 52 → ends at 0 (lands on 0)
L5   - Rotate left 5 steps from position 0 → ends at 95
R60  - Rotate right 60 steps from position 95 → ends at 55, passes through 0 once
L55  - Rotate left 55 steps from position 55 → ends at 0 (lands on 0)
L1   - Rotate left 1 step from position 0 → ends at 99
L99  - Rotate left 99 steps from position 99 → ends at 0 (lands on 0)
R14  - Rotate right 14 steps from position 0 → ends at 14
L82  - Rotate left 82 steps from position 14 → ends at 32, passes through 0 once
```

**Part 1 Answer:** 3 (lands on 0 after R48, L55, L99)  
**Part 2 Answer:** 6 (3 landings + 3 passes during rotation)

## Approach

### Part 1: Landing on Zero

This is straightforward - simulate the dial rotations and count when `position == 0`.

```python
position = (position + delta) % 100  # where delta = ±distance
```

The modulo operation handles the circular wrapping.

### Part 2: Counting Zero Crossings

This requires counting how many times we point at 0 **during** the rotation, not just at the end.

#### Key Insights

1. **The dial is circular (0-99)**, so position 100 wraps back to 0
2. **Starting at 0 doesn't count** (unless we loop back to it)
3. **We need to count both passing through and landing on 0**

#### Algorithm for Counting Zeros

**Case 1: Starting at position 0**
- Only count if we make complete loops (distance ≥ 100)
- Count = `distance // 100`

**Case 2: Moving Right (clockwise)**
- We pass through 0 at positions 100, 200, 300, etc.
- Count multiples of 100 we pass: `(start + distance) // 100 - start // 100`
- Example: From position 95, moving right 60 → (155 // 100) - (95 // 100) = 1 - 0 = 1 ✓

**Case 3: Moving Left without wrapping**
- If `distance ≤ start`, we stay in positions [start-distance, start]
- Only count if we land exactly on 0: `start - distance == 0`

**Case 4: Moving Left with wrapping**
- If `distance > start`, we wrap past 0
- Count: Initial crossing + complete loops + final landing
  
  ```python
  zeros = 1 + (distance - start - 1) // 100
  
  # Special case: if we end exactly on 0, add 1 more
  if (start - distance) % 100 == 0:
      zeros += 1
  ```

#### Why the Special Case for Ending on 0?

Consider `L350` from position 50:
- Path: 50 → 0 (51 steps) → continues for 299 more steps
- Manual count: Pass 0, then loop 299 steps = 2 more times at -100 and -200
- Final position: (50 - 350) % 100 = 0 (we're at -300, which wraps to 0)
- **We need to count this final landing on 0!**

Without the special case: `1 + 299 // 100 = 1 + 2 = 3` ✗  
With the special case: `3 + 1 = 4` ✓

This is because `-300` is a multiple of 100, representing another crossing.

## Implementation Details

### Helper Functions

```python
def update_position(position, distance, direction):
    """Update position on circular dial after rotation."""
    delta = distance if direction == 'R' else -distance
    return (position + delta) % 100
```

This encapsulates the position update logic, making it reusable and clear.

### count_zeros_during_rotation

The core logic:

```python
def count_zeros_during_rotation(start, distance, direction):
    # Starting at 0: only count complete loops
    if start == 0:
        return distance // 100
    
    # Moving right: count multiples of 100
    if direction == 'R':
        return (start + distance) // 100 - start // 100
    
    # Moving left without wrapping
    if distance <= start:
        return 1 if start - distance == 0 else 0
    
    # Moving left with wrapping
    zeros = 1 + (distance - start - 1) // 100
    if (start - distance) % 100 == 0:
        zeros += 1
    
    return zeros
```

## Edge Cases Handled

1. **Starting at 0**: L5 from 0 → doesn't count (we're already there)
2. **Large distances**: R907 → correctly counts 9 crossings
3. **Landing exactly on 0 after wrapping**: L350 from 50 → counts 4 (not 3)
4. **Multiple complete rotations**: Distance 1000+ handled correctly

## Complexity

- **Time:** O(n) where n is the number of rotations
- **Space:** O(1) - only tracking current position

Each rotation is processed in constant time using mathematical formulas rather than simulating each step.

## Testing

The solution correctly handles:
- ✅ Sample input: Part 1 = 3, Part 2 = 6
- ✅ Full input: Part 1 = 1023, Part 2 = 5899
- ✅ Boundary case: L350 from 50 = 4 crossings
- ✅ Edge case: Rotations starting from 0
- ✅ Large rotations: Distances > 900

## Key Takeaway

The tricky part is recognizing that on a circular dial, when we move left and wrap past 0, landing exactly on a position that's a multiple of 100 (when unwrapped) represents an additional crossing of 0. This is why `L350` from position 50 counts as 4 crossings, not 3.