# Day 7: Tachyon Manifold Beam Splitting

## Problem Overview

You need to repair a teleporter by understanding how tachyon beams interact with a manifold containing beam splitters. The manifold is represented as a 2D grid where:
- `S` represents the source where a tachyon beam enters from above
- `^` represents splitters that divide beams
- `.` represents empty space

## Part 1: Counting Unique Splitter Activations

### The Physics

A tachyon beam starts at source `S` and travels **downward**. When it hits a splitter (`^`):
1. The original beam **stops**
2. Two new beams are created at positions **left and right** of the splitter
3. Both new beams continue traveling **downward** (same direction as original)
4. This process repeats until all beams exit the manifold

### Key Insight

The question asks: **How many times is a beam split?**

This is asking for the **number of unique splitters that get hit by at least one beam**, not the total number of beam-splitter collision events.

### Why "Unique" Matters

Multiple beams can pass through the same splitter position. Consider:
```
......|^|......  Row 2 - One splitter creates two beams
......|.|......
.....|^|^|.....  Row 4 - Two splitters, but middle column has beams from both
```

At row 4, the middle position receives beams from **both** the left and right splitters above it. However, the splitters at row 4 are still only counted **once each**, regardless of how many beams hit them.

### Approach

1. **Use BFS/Queue**: Process each beam position one at a time
2. **Track visited positions**: Use `(row, col)` to avoid processing the same beam position twice
   - We don't need direction because all beams always go down
   - A position can only be visited once since beams never move upward
3. **Track hit splitters**: Maintain a set of splitter positions that have been activated
4. **For each beam**:
   - Find the next splitter directly below it in the same column
   - If found, mark that splitter as "hit" and create two new beams (left and right of splitter)
   - If not found, the beam exits the manifold

### Optimization Opportunity

Instead of stepping through each row one-by-one, you can **jump directly to the next splitter**:
- Pre-index splitters by column (for downward movement)
- Use binary search or filtering to find the nearest splitter below current position
- This is especially helpful for large grids with sparse splitters

## Part 2: Counting Quantum Timelines

### The Quantum Twist

Part 2 reveals the quantum nature of the manifold: when a particle reaches a splitter, **time itself splits**:
- In one timeline, the particle went left
- In another timeline, the particle went right
- Both timelines exist simultaneously

### The Question

**How many distinct timelines exist after the particle completes all possible journeys?**

A timeline is a complete path from source to exit, where at each splitter encountered, you made a specific choice (left or right).

### Key Insight

This is a **path counting problem** through a binary tree:
- Each splitter is a branching point where paths split into two
- Some branches terminate early (exit the manifold)
- We need to count all valid complete paths from source to any exit point

### Why Not 2^n?

If you hit `n` splitters and make binary choices at each, you might think there are `2^n` timelines. However:
- Not all choice combinations lead to valid paths
- Some choices lead to immediate exits (hitting boundaries)
- Some splitters may not be reachable with certain choice combinations

The actual number is the count of **leaf nodes** in the path tree.

### Approach

Use **recursive path counting with memoization**:

1. **Recursive function**: `count_paths_from(row, col)` returns the number of distinct paths from that position to any exit
2. **Base case**: If no splitter is found below, the beam exits → return 1 (one complete timeline)
3. **Recursive case**: If a splitter is found:
   - Count paths if we go left: `count_paths_from(splitter_row, splitter_col - 1)`
   - Count paths if we go right: `count_paths_from(splitter_row, splitter_col + 1)`
   - Return the sum (total paths is sum of both branches)
4. **Memoization**: Cache results for each `(row, col)` position to avoid recalculating

### Visualization

Think of it as a tree where:
```
                    Source
                      |
                  Splitter 1
                   /      \
                Left      Right
                 |          |
            Splitter 2   Splitter 3
             /    \       /    \
           Exit  Exit   Exit  Exit
```

Each path from root to a leaf is one timeline. Count all the leaves!

### Why Memoization Works

The same position `(row, col)` might be reached through different paths (different choices at earlier splitters). But once you're at `(row, col)`, the number of ways to reach an exit from there is the same regardless of how you got there. This is why caching works perfectly.

## Common Pitfalls

### Part 1
- ❌ Counting every beam-splitter collision event (will overcount if multiple beams hit same splitter)
- ❌ Not tracking visited positions (will infinite loop or reprocess beams)
- ❌ Thinking beams change direction at splitters (they always go down, just split spatially)

### Part 2
- ❌ Trying to enumerate all paths explicitly (exponential memory)
- ❌ Forgetting to handle boundary cases (beams going out of bounds)
- ❌ Not using memoization (will be too slow for large inputs)
- ❌ Counting states instead of complete paths (need to count exits, not intermediate positions)

## Complexity Analysis

### Part 1
- **Time**: O(splitters × beam_positions) with optimization, O(grid_size × beam_positions) without
- **Space**: O(beam_positions) for the visited set and queue

### Part 2
- **Time**: O(unique_positions × average_splitters_per_path) with memoization
- **Space**: O(unique_positions) for the memoization cache

The memoization in Part 2 is crucial because it transforms an exponential problem into a polynomial one by reusing subproblem solutions.

## Solution Strategy Summary

### Part 1: BFS + Set Tracking
1. Parse input to find source and all splitter positions
2. Use BFS to simulate beam propagation
3. Track visited beam positions to avoid reprocessing
4. Track unique splitters that get hit
5. Return count of unique hit splitters

### Part 2: Recursive Path Counting
1. Reuse parsing from Part 1
2. Implement recursive function to count paths from any position
3. Use memoization to cache results for each position
4. Base case: reaching exit = 1 path
5. Recursive case: sum of paths from left and right branches
6. Return total path count from source

## Key Takeaway

Part 1 is about **graph traversal and state tracking** - simulating the physical beam splitting process.

Part 2 is about **combinatorial path counting** - calculating how many different ways the quantum particle can traverse the manifold.

Both parts benefit from the optimization of jumping directly to the next splitter rather than stepping cell-by-cell.
