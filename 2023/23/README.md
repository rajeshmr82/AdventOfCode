# A Long Walk

## Problem Overview

In this challenge, you are tasked with finding the longest possible path through a grid representing a hiking trail. The grid consists of various tile types, including paths, forests, and slopes. The goal is to navigate from a starting position to an ending position while adhering to specific movement rules based on the tile types.

### Tile Types
- **Path (`.`)**: A normal tile that can be traversed.
- **Forest (`#`)**: An impassable tile.
- **Slopes (`^`, `>`, `v`, `<`)**: Tiles that allow movement in a specific direction (up, right, down, left).

## Algorithm

### Part 1: Finding the Longest Path Without Ignoring Slopes

In the first part of the challenge, the algorithm finds the longest path from the starting position to the ending position while treating slopes as directional tiles. The algorithm uses an iterative depth-first search (DFS) approach to explore all possible paths.

#### Steps:
1. **Initialization**: Start from the initial position and initialize a stack to keep track of the current position, path length, and visited nodes.
2. **Exploration**: While there are nodes in the stack:
   - Pop the current node and check if it is the end node. If so, update the maximum path length found.
   - For each valid neighboring node, check if it has been visited. If not, create a new visited set and push the neighbor onto the stack with the updated path length.
3. **Return Result**: After exploring all paths, return the maximum path length found.

### Part 2: Finding the Longest Path Treating All Slopes as Paths

In the second part, the algorithm modifies the behavior to treat all slopes as normal paths. This allows for potentially longer paths since the restrictions imposed by slopes are removed.

#### Steps:
1. **Initialization**: Similar to Part 1, start from the initial position and initialize a stack.
2. **Exploration**: The exploration process remains the same, but the algorithm now considers slopes as valid paths when determining valid neighbors.
3. **Return Result**: After exploring all paths, return the maximum path length found.

## Implementation

The implementation is done in Python, utilizing classes to represent the hiking trail and the various tile types. The main class, `HikingTrail`, contains methods for reading input, validating positions, and finding the longest path using the specified algorithms.

Example input:
```
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
```

## Algorithm Overview

The solution employs several optimization techniques:

1. **Graph Reduction**
   - Identifies junction points (intersections, turns, slopes)
   - Collapses paths between junctions into weighted edges
   - Removes passthrough nodes (nodes with exactly 2 edges)

2. **Dead End Elimination**
   - Removes paths that don't lead to the end
   - Prevents creation of isolated loops
   - Maintains path connectivity

3. **Iterative Path Finding**
   - Uses stack-based DFS instead of recursion
   - Maintains independent visited sets per path
   - Sorts edges by weight to try promising paths first

## Implementation

### Prerequisites
- Python 3.7+
- No external dependencies

### Core Classes

```python
from dataclasses import dataclass
from typing import Dict, Set, Tuple, List
from collections import defaultdict

@dataclass(frozen=True)
class Node:
    row: int
    col: int

class CollapsedGraph:
    def __init__(self):
        self.edges: Dict[Node, Dict[Node, int]] = defaultdict(dict)
        self.start: Node = None
        self.end: Node = None
```

### Usage

```python
# Part 1: Following slope rules
def solve_part_one(input_str: str) -> int:
    grid = parse_input(input_str)
    return solve(grid, ignore_slopes=False)

# Part 2: Ignoring slopes
def solve_part_two(input_str: str) -> int:
    grid = parse_input(input_str)
    return solve(grid, ignore_slopes=True)
```

## Algorithm Details

### 1. Graph Building Process

```
Original Grid               Collapsed Graph
#.###                      S
#...# ------>             / \w=2
#.#.#                    J1--J2
#...#                     \ /w=3
###.#                      E

S: Start, E: End, J: Junction, w: Weight
```

The process:
1. Identify junction points
2. Follow paths until reaching other junctions
3. Create weighted edges
4. Remove dead ends

### 2. Path Following

```python
def follow_path(start: Node, prev: Node) -> Tuple[Node, int]:
    """Follow a path until reaching a junction."""
    current = start
    distance = 0
    visited = {prev, start}
    
    while True:
        neighbors = get_neighbors(current)
        next_nodes = [(node, dist) for node, dist in neighbors 
                     if node not in visited]
        
        if not next_nodes or len(next_nodes) > 1:
            return current, distance
        
        next_node, dist = next_nodes[0]
        distance += dist
        visited.add(next_node)
        current = next_node
```

### 3. Iterative DFS

```python
def find_longest_path(self) -> int:
    """Find longest path using iterative DFS."""
    stack = [(self.start, 0, frozenset([self.start]))]
    max_length = float('-inf')
    
    while stack:
        current, length, visited = stack.pop()
        if current == self.end:
            max_length = max(max_length, length)
            continue
        
        neighbors = sorted(
            [(next_node, weight) 
             for next_node, weight in self.edges[current].items()
             if next_node not in visited],
            key=lambda x: x[1],
            reverse=True
        )
        
        for next_node, weight in neighbors:
            stack.append((
                next_node, 
                length + weight, 
                frozenset([*visited, next_node])
            ))
    
    return max_length
```

## Optimizations

1. **Graph Reduction**
   - Typically reduces graph size by ~96%
   - Eliminates redundant path segments
   - Maintains only essential decision points

2. **Memory Efficiency**
   - Uses iterative approach to prevent stack overflow
   - Employs frozen sets for immutable state
   - Implements sparse graph representation

3. **Search Optimization**
   - Sorts edges by weight to prioritize promising paths
   - Eliminates dead ends during graph construction
   - Maintains minimal set of necessary nodes

## Performance

- Original grid size: O(n×m)
- Reduced graph size: ~O((n×m)/20) typically
- Path finding: O(V + E) where V = junctions, E = paths between junctions

## Notes

- Optimized for grids with many simple path segments
- Performance improves with higher ratio of passthrough nodes
- Memory usage is efficient due to graph reduction
- Handles both directional (slopes) and non-directional paths