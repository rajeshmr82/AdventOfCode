# Graph Partitioning Algorithm

## Problem Description
The algorithm solves the problem of finding three edges (wires) in an undirected graph that, when removed, partition the graph into exactly two disconnected components, with the goal of finding the product of the sizes of these components.

## Algorithm Overview
The solution uses Karger's Algorithm, which is a randomized algorithm for finding minimum cuts in a graph. The implementation includes several optimizations and reliability improvements.

### Key Components

1. **Karger's Algorithm Core Concept**
   - Repeatedly contracts random edges until only two vertices remain
   - The edges between these two vertices form a cut
   - Multiple iterations increase the probability of finding the minimum cut

2. **Union-Find Data Structure**
   - Used for efficiently tracking connected components
   - Implements path compression for faster lookups
   - Uses union by rank for balanced trees

## Implementation Details

### Data Structures

1. **Edge Class**
```python
@dataclass
class Edge:
    start: str
    end: str
```

2. **Graph Representation**
   - Edges stored as a list of Edge objects
   - Vertices stored as a set of strings
   - Union-Find structure using dictionary with (parent, rank) tuples

### Key Functions

1. **Union-Find Operations**
   - `_union_find_find`: Finds set representative with path compression
   - `_union_find_union`: Merges sets using rank-based union

2. **Karger's Algorithm Implementation**
   - `_karger_iteration`: Performs one iteration of edge contractions
   - `find_min_cut`: Main function that runs multiple iterations

### Optimizations

1. **Iteration Control**
   - Maximum iterations calculated using `log(n) * n^2`
   - Ensures algorithm terminates
   - Provides good probability of finding solution

2. **Deterministic Randomization**
   - Uses seeded random number generator
   - Makes results reproducible
   - Helps with debugging

3. **Edge Handling**
   - Prevents duplicate edges
   - Maintains consistent edge ordering
   - Uses efficient set operations

### Verification

1. **Cut Validation**
   - Verifies cuts create exactly two components
   - Uses BFS to find component sizes
   - Checks solution validity

2. **Component Size Calculation**
   - Efficiently calculates sizes using BFS
   - Builds adjacency list for fast traversal
   - Returns product of component sizes

## Time Complexity

- Single Karger iteration: O(V + E)
- Finding component sizes: O(V + E)
- Overall algorithm: O(log(V) * V^2 * (V + E))
  - Where V is number of vertices
  - E is number of edges

## Space Complexity

- Graph storage: O(V + E)
- Union-Find structure: O(V)
- Component tracking: O(V)
- Overall: O(V + E)

## Example Usage

```python
# Initialize solver with input
solver = OptimizedKarger(input_text)

# Find minimum cut
wires, product = solver.find_min_cut()

# Output results
print("Wires to cut:")
for wire in wires:
    print(f"  {wire.start} -- {wire.end}")
print(f"Product of component sizes: {product}")
```

## Error Handling

1. **Maximum Iterations**
   - Raises RuntimeError if no solution found
   - Includes iteration count in error message

2. **Input Validation**
   - Handles malformed input
   - Skips empty lines
   - Normalizes vertex names

## Improvements Over Basic Karger's Algorithm

1. **Reliability**
   - Deterministic seeding
   - Maximum iteration limit
   - Solution verification

2. **Performance**
   - Efficient data structures
   - Path compression
   - Early termination checks

3. **Memory Usage**
   - Reuses data structures
   - Avoids unnecessary copies
   - Efficient set operations

## References

1. Karger, D. R. (1993). "Global Min-cuts in RNC and Other Ramifications of a Simple Min-Cut Algorithm"
2. Karger, D. R., & Stein, C. (1996). "A New Approach to the Minimum Cut Problem"
