# Day X: Junction Box Circuit Connection

## Problem Overview

You need to help Elves connect junction boxes to create electrical circuits by connecting pairs of boxes that are closest together. Junction boxes are positioned in 3D space with (X, Y, Z) coordinates, and connections are made based on Euclidean distance.

## Part 1: Counting Circuit Sizes After N Connections

### The Setup

You have a list of junction boxes at various 3D coordinates:
- Each junction box starts as its own separate circuit
- Connections are attempted in order of distance (shortest first)
- When two boxes connect, electricity can flow between them (they become part of the same circuit)
- If two boxes are already in the same circuit, attempting to connect them does nothing

### Key Insight

This is a **Minimum Spanning Tree (MST) problem** using **Kruskal's algorithm** with **Union-Find**:
- You're greedily selecting the shortest edges (connections)
- You stop after attempting a fixed number of connections (not necessarily making that many successful connections)
- The question asks: After N attempts, what are the sizes of the resulting circuits?

### Why "Attempts" Not "Connections"

This is crucial to understand:
```
Attempt #1: Connect boxes A-B (successful) → 1 connection made
Attempt #2: Connect boxes A-C (successful) → 2 connections made
Attempt #3: Connect boxes B-C (already connected!) → still 2 connections made
Attempt #4: Connect boxes D-E (successful) → 3 connections made
```

After **4 attempts**, you've only made **3 successful connections**. The problem counts attempts, not successes.

### The "Already Connected" Case

When you try to connect two boxes that are already in the same circuit:
- No new connection is made
- The circuit structures don't change
- This still counts as one of your N attempts
- This is why you can have more components than expected

### Approach

1. **Calculate all pairwise distances**: For N boxes, compute distances for all N(N-1)/2 pairs
2. **Sort by distance**: Create list of edges `(distance, box_i, box_j)` sorted ascending
3. **Initialize Union-Find**: Start with N separate components (each box is its own circuit)
4. **Process first N edges**: Iterate through the N shortest edges
   - Try to union the two boxes
   - Union-Find automatically handles the "already connected" case
5. **Count component sizes**: Group boxes by their root parent, count each group
6. **Multiply three largest**: Sort sizes descending, multiply top 3

### Why Union-Find?

Union-Find (Disjoint Set Union) is perfect for this problem because:
- **Fast connectivity check**: O(α(N)) ≈ O(1) to check if two boxes are in same circuit
- **Fast merging**: O(α(N)) ≈ O(1) to merge two circuits
- **Path compression**: Automatically optimizes repeated queries
- **Size tracking**: Can track component sizes during union operations

### Algorithm: Kruskal's MST (Partial)

This is a partial Minimum Spanning Tree:
```
1. Sort all edges by weight (distance)
2. For each edge in sorted order:
   a. Check if endpoints are in different components
   b. If yes, union them (add edge to MST)
   c. If no, skip (would create cycle)
3. Stop after K attempts (not after K successful unions!)
```

## Part 2: Finding the Final Connection

### The Question

Instead of stopping after N attempts, continue until **all boxes are in one giant circuit**. What are the X-coordinates of the two boxes in the **last connection** that completes the circuit?

### Key Insight

This is asking for the **complete Minimum Spanning Tree**:
- A tree connecting N nodes requires exactly **(N-1) edges**
- Keep adding shortest edges until you've made (N-1) successful unions
- The last edge added is the one that finally connects everything into one component

### Why N-1 Edges?

Graph theory fundamental:
- Start with N separate components (N disconnected nodes)
- Each successful union reduces component count by 1
- After 1 union: N-1 components
- After 2 unions: N-2 components
- After N-1 unions: 1 component (fully connected tree)

You cannot have fewer than N-1 edges in a connected tree with N nodes.

### Approach

1. **Same setup as Part 1**: Calculate and sort all edges
2. **Track successful unions**: Count only when union actually merges two different components
3. **Stop at N-1**: When you've made (N-1) successful unions, all boxes are connected
4. **Return the last edge**: Extract X-coordinates from the final edge that was added

### Implementation Strategy

**Option 1: Count successful unions**
```python
successful_unions = 0
for distance, i, j in sorted_edges:
    if uf.find(i) != uf.find(j):
        uf.union(i, j)
        successful_unions += 1
        
        if successful_unions == len(junctions) - 1:
            # This was the final edge!
            return junctions[i][0] * junctions[j][0]
```

**Option 2: Track component count in Union-Find**
```python
class UnionFind:
    def __init__(self, n):
        self.num_components = n
    
    def union(self, x, y):
        if root_x != root_y:
            # ... merge logic ...
            self.num_components -= 1
            return True  # Successful union
        return False  # Already connected

# Then check:
if uf.num_components == 1:
    # All connected!
```

**Option 3: Check unique roots**
```python
def is_fully_connected(uf, n):
    return len({uf.find(i) for i in range(n)}) == 1
```

Option 1 is cleanest because it leverages the mathematical property directly.

## Common Pitfalls

### Part 1
- ✗ Counting successful connections instead of attempts (will give wrong component count)
- ✗ Not sorting edges by distance (won't get shortest connections first)
- ✗ Using actual distance instead of squared distance (slower, but won't affect correctness)
- ✗ Iterating `for box in junctions` instead of `for i in range(len(junctions))` when counting components

### Part 2
- ✗ Not tracking whether union was successful (will stop too early if you count skipped edges)
- ✗ Off-by-one errors (need exactly N-1 edges, not N)
- ✗ Processing all edges instead of stopping at completion
- ✗ Forgetting that "last connection" means the edge that was added, not just attempted

## Complexity Analysis

### Part 1
- **Distance calculation**: O(N²) to compute all pairwise distances
- **Sorting**: O(N² log N) to sort all edges
- **Union-Find operations**: O(K × α(N)) ≈ O(K) for K attempts
- **Component counting**: O(N) to iterate through all boxes
- **Overall**: O(N² log N) dominated by sorting

### Part 2
- **Same as Part 1**: O(N² log N)
- **Worst case processes all edges**: O(N² × α(N)) but typically stops much earlier
- **Overall**: O(N² log N)

### Space Complexity
- **Edge list**: O(N²) to store all possible edges
- **Union-Find**: O(N) for parent and size arrays
- **Overall**: O(N²)

## Optimizations

### 1. Use Squared Distance
```python
# Instead of:
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

# Use:
distance_squared = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
```
Sorting by squared distance gives the same order, but avoids expensive sqrt() calls.

### 2. Union-Find with Path Compression
```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]
```
Flattens tree structure, making future finds nearly O(1).

### 3. Union by Size/Rank
```python
def union(self, x, y):
    # Always attach smaller tree under larger tree
    if self.size[root_x] < self.size[root_y]:
        root_x, root_y = root_y, root_x
    
    self.parent[root_y] = root_x
    self.size[root_x] += self.size[root_y]
```
Keeps trees shallow, improving find() performance.

### 4. Early Termination in Part 2
```python
if successful_unions == n - 1:
    break  # Don't process remaining edges
```

## Data Structures

### Input Parsing
```python
def parse(raw_input: str) -> list[tuple[int, int, int]]:
    return [tuple(map(int, line.split(","))) 
            for line in raw_input.splitlines()]
```

### Edge Representation
```python
# List of tuples: (distance, box_index_i, box_index_j)
edges = [(distance, i, j), ...]
```

### Component Tracking
```python
# Option 1: Dictionary of root -> count
component_sizes = defaultdict(int)
for i in range(n):
    component_sizes[uf.find(i)] += 1

# Option 2: List comprehension
sizes = sorted(Counter(uf.find(i) for i in range(n)).values())
```

## Solution Strategy Summary

### Part 1: Partial MST with Fixed Attempts
1. Parse input into list of 3D coordinates
2. Calculate all pairwise Euclidean distances
3. Sort edges by distance (ascending)
4. Initialize Union-Find with N components
5. Process first K edges (attempt K connections)
6. Count final component sizes
7. Return product of three largest sizes

### Part 2: Complete MST
1. Reuse setup from Part 1
2. Process edges until (N-1) successful unions
3. Track the last edge that was successfully added
4. Return product of X-coordinates of that edge's endpoints

## Key Takeaways

**Part 1** is about understanding the difference between *attempting* connections and *making* connections. The Union-Find structure naturally handles already-connected cases.

**Part 2** leverages the fundamental graph property that a tree with N nodes has exactly N-1 edges. Once you've made N-1 successful unions, you're guaranteed to have a single connected component.

Both parts are classic applications of **Kruskal's algorithm** for finding Minimum Spanning Trees, using **Union-Find** for efficient connectivity queries and component merging.

## Test Case Walkthrough

### Example: 20 Junction Boxes, 10 Attempts

```
Attempt 1: Connect 0-19 (distance 316.90) ✓ Connected → 19 components
Attempt 2: Connect 0-7  (distance 321.56) ✓ Connected → 18 components
Attempt 3: Connect 2-13 (distance 322.37) ✓ Connected → 17 components
Attempt 4: Connect 7-19 (distance 328.12) ✗ Skip (already connected) → 17 components
Attempt 5: Connect 17-18 (distance 333.66) ✓ Connected → 16 components
...
Attempt 10: Connect 3-19 (distance 367.98) ✓ Connected → 11 components
```

After 10 attempts:
- 9 successful connections made
- 20 - 9 = 11 components remaining
- Component sizes: [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]
- Answer: 5 × 4 × 2 = 40

This illustrates why counting attempts (not successes) matters!
