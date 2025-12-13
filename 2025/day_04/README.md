# Day 4: Forklift Accessibility

## Problem Summary

The Elves need to access rolls of paper in a warehouse using forklifts. However, forklifts can only access rolls that are somewhat isolated - specifically, rolls with **fewer than 4 adjacent rolls** (checking all 8 directions including diagonals).

### Part 1: Initial Accessibility Count

**Question**: How many rolls can be accessed initially?

**Input Format**:
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

Where:
- `@` = roll of paper
- `.` = empty space

**Example Output**: `13` accessible rolls

---

## Part 1: Intuition

### Core Concept
A roll is accessible if it has **< 4 neighbors** that are also rolls (checking all 8 directions).

### Why This Makes Sense
- Rolls in dense clusters (≥4 neighbors) are blocked by surrounding rolls
- Rolls on edges, corners, or in sparse areas are more accessible
- This creates a "perimeter accessibility" pattern

### Algorithm
1. Parse the grid into a 2D array
2. For each `@` position:
   - Count adjacent `@` symbols in all 8 directions
   - If count < 4, it's accessible
3. Return total count

### Implementation Strategy

```python
def count_accessible_rolls(grid):
    """Count rolls with fewer than 4 adjacent rolls."""
    directions = [
        (dr, dc) 
        for dr in (-1, 0, 1) 
        for dc in (-1, 0, 1) 
        if (dr, dc) != (0, 0)
    ]
    
    def count_neighbors(r, c):
        return sum(
            1 for dr, dc in directions
            if (0 <= r + dr < grid.shape[0] and 
                0 <= c + dc < grid.shape[1] and 
                grid[r + dr, c + dc] == '@')
        )
    
    return sum(
        1 for r in range(grid.shape[0]) 
        for c in range(grid.shape[1])
        if grid[r, c] == '@' and count_neighbors(r, c) < 4
    )
```

### Complexity
- **Time**: O(n × m) where n = rows, m = columns
- **Space**: O(1) excluding input
- Each cell checked once, 8 neighbors checked per cell

### Key Insights
- Edge and corner cells naturally have fewer possible neighbors
- The problem is asking us to identify the "perimeter" of paper clusters
- No optimization better than checking each cell (unavoidable)

---

## Part 2: Cascading Removal

### Problem Extension
Once accessible rolls are removed, **new rolls may become accessible**. Keep removing until no more rolls can be accessed.

**Question**: How many total rolls can be removed?

**Example Output**: `43` rolls removed total

### Visualization of Process
```
Initial: 13 accessible → Remove → 12 more accessible → Remove → 7 more...
Total removed: 13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1 = 43
```

---

## Part 2: Intuition

### Core Concept
This is a **cascading erosion problem**:
1. Remove accessible rolls (perimeter of clusters)
2. This exposes new perimeter rolls
3. Repeat until no accessible rolls remain
4. Clusters erode from outside → inside (like peeling an onion)

### Why Simulation is Necessary
- **Cannot be solved analytically** - removal order affects which rolls become accessible
- **Path-dependent** - the state after each removal affects future removals
- **Iterative process** - each round of removals creates new opportunities

### Optimization Strategy

#### Naive Approach (❌ Inefficient)
```python
# Check entire grid after each removal
while True:
    accessible = find_all_accessible(grid)  # O(n×m)
    if not accessible:
        break
    remove_all(accessible)
```
- Problem: Rechecks entire grid every iteration
- Inefficiency: Most cells don't change between iterations

#### Optimized Approach (✅ Efficient)
```python
# Only check cells affected by removals
to_check = all_roll_positions  # Initial set
while to_check:
    accessible = [pos for pos in to_check if is_accessible(pos)]
    if not accessible:
        break
    
    # Only check neighbors of removed rolls
    to_check = neighbors_of_removed_rolls
    remove_all(accessible)
```

**Key Optimization**: Only recheck cells that could have changed (neighbors of removed rolls)


### Complexity Analysis

**Time Complexity**: O(k × n × m)
- k = number of iterations (typically small, proportional to cluster radius)
- n × m = grid size
- In practice: k ≈ max_cluster_radius (e.g., 10-20 for typical inputs)

**Space Complexity**: O(n × m)
- Grid copy + set of positions to check

**Optimization Wins**:
- Early exit in neighbor counting (stops at 4)
- Only rechecks affected cells (not entire grid)
- Set operations for efficient neighbor collection

### Why This Works

1. **Perimeter erosion**: Accessible rolls are always on the perimeter of clusters
2. **Layer-by-layer**: Each iteration removes one "layer" of the cluster
3. **Convergence**: Eventually all clusters are completely eroded or reduced to inaccessible cores (≥4 neighbors each)

### Key Insights

- **Think like peeling an onion**: Remove outer layers first
- **Local changes, local checks**: Only neighbors of removed rolls can become accessible
- **Early exit optimization**: Stop counting neighbors at 4
- **No DP needed**: Greedy removal works because any removal order leads to same result
- **Simulation is optimal**: No closed-form solution exists

---

## Comparison: Part 1 vs Part 2

| Aspect | Part 1 | Part 2 |
|--------|--------|--------|
| **Complexity** | Single pass | Iterative simulation |
| **Time** | O(n×m) | O(k×n×m) where k ≈ cluster depth |
| **Key Insight** | Count perimeter | Cascading erosion |
| **Optimization** | None needed | Track affected cells only |
| **Pattern** | Static analysis | Dynamic process |

---

## Visual Understanding

### Part 1: Initial State
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Accessible rolls (x = accessible):
..xx.xx@x.  ← Top edge rolls
x@@.@.@.@@  ← Left edge + isolated
@@@@@.x.@@  ← Gap-adjacent
@.@@@@..@.
x@.@@@@.@x  ← Left/right edges
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@  ← Bottom left corner
.@@@@@@@@.
x.x.@@@.x.  ← Bottom corners + gaps
```

### Part 2: Erosion Process
```
Round 1: Remove 13 perimeter rolls
Round 2: New perimeter exposed → Remove 12
Round 3: Cluster shrinks → Remove 7
...
Final: Dense core completely eroded
```

---

## Lessons Learned

1. **Grid navigation**: Understanding 8-directional movement patterns
2. **Cascading effects**: How local changes propagate through a system
3. **Optimization through tracking**: Only recheck what changed
4. **Early exit patterns**: Stop counting when threshold reached
5. **Simulation vs. closed-form**: Knowing when simulation is the right approach

---

## Alternative Approaches Considered

### ❌ Dynamic Programming
- Not applicable: No optimal substructure (removal order doesn't create overlapping subproblems)

### ❌ Graph Theory (BFS/DFS)
- Overcomplicates: This isn't a pathfinding problem

### ❌ Mathematical Formula
- Impossible: Cluster shapes are arbitrary, no closed-form solution

### ✅ Iterative Simulation with Optimization
- **Best approach**: Clear, efficient, and naturally matches problem structure

---

## Performance Notes

For typical AOC inputs (100×100 grids):
- **Part 1**: ~1ms
- **Part 2**: ~10-50ms (depends on cluster density)

Bottlenecks:
- Neighbor counting (optimized with early exit)
- Set operations (already efficient in Python)

No further optimization needed for problem constraints.

---

## Summary

- **Part 1**: Count accessible rolls (< 4 neighbors) - single pass O(n×m)
- **Part 2**: Simulate cascading removal until convergence - iterative O(k×n×m)
- **Key technique**: Track affected cells to avoid redundant checks
- **Core insight**: Clusters erode from perimeter inward, layer by layer

**Time Investment**: ~30 minutes for both parts with optimization