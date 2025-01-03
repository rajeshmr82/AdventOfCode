from typing import Dict, Set, Tuple, List, DefaultDict
from collections import defaultdict, deque
from dataclasses import dataclass
from enum import Enum
def read_input():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


class TileType(Enum):
    PATH = "."
    FOREST = "#"
    SLOPE_UP = "^"
    SLOPE_RIGHT = ">"
    SLOPE_DOWN = "v"
    SLOPE_LEFT = "<"


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


class HikingTrail:
    def __init__(
        self, grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
    ):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if grid else 0
        self.start = start
        self.end = end

        # Validate grid dimensions
        if any(len(row) != self.width for row in grid):
            raise ValueError("Grid rows must have equal width")

    def is_valid_position(self, pos: Tuple[int, int]) -> bool:
        """Check if the given position is within grid bounds and not a forest tile."""
        row, col = pos
        return (
            0 <= row < self.height
            and 0 <= col < self.width
            and self.grid[row][col] != TileType.FOREST.value
        )

    def get_tile_type(self, pos: Tuple[int, int]) -> TileType:
        """Get the type of tile at the given position."""
        row, col = pos
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise ValueError("Position out of bounds")

        tile = self.grid[row][col]
        return next(t for t in TileType if t.value == tile)

    def get_valid_neighbors(
        self,
        pos: Tuple[int, int],
        visited: Set[Tuple[int, int]],
        ignore_slopes: bool = False,
    ) -> List[Tuple[int, int]]:
        """Get valid neighboring positions that haven't been visited yet.

        Args:
            pos: Current position
            visited: Set of already visited positions
            ignore_slopes: If True, treat all slopes as regular paths
        """
        row, col = pos
        current_tile = self.get_tile_type(pos)

        # Define possible moves based on current tile type and slope rules
        if not ignore_slopes and current_tile != TileType.PATH:
            if current_tile == TileType.SLOPE_UP:
                possible_moves = [(row - 1, col)]
            elif current_tile == TileType.SLOPE_RIGHT:
                possible_moves = [(row, col + 1)]
            elif current_tile == TileType.SLOPE_DOWN:
                possible_moves = [(row + 1, col)]
            elif current_tile == TileType.SLOPE_LEFT:
                possible_moves = [(row, col - 1)]
        else:  # PATH tile or ignoring slopes
            possible_moves = [
                (row - 1, col),  # up
                (row, col + 1),  # right
                (row + 1, col),  # down
                (row, col - 1),  # left
            ]

        # Filter valid moves
        valid_moves = []
        for next_pos in possible_moves:
            if self.is_valid_position(next_pos) and next_pos not in visited:
                valid_moves.append(next_pos)

        return valid_moves

    def find_longest_path(self, ignore_slopes: bool = False) -> int:
        """
        Find the length of the longest possible path from start to end
        without revisiting any tiles and following slope rules.
        Returns -1 if no valid path exists.
        """
        exploration_stack = [(self.start, 0, frozenset([self.start]))]  # (current node, current path length, visited set)
        max_length = float('-inf')  # Track the maximum path length found

        while exploration_stack:
            current, path_length, visited = exploration_stack.pop()

            # Update max_length if we reach the end
            if current == self.end:
                max_length = max(max_length, path_length)

            self.add_neighbors_to_stack(current, path_length, visited, exploration_stack)

        return max_length if max_length != float('-inf') else -1

    def add_neighbors_to_stack(self, current: Node, path_length: int, visited: frozenset, stack: list):
        """Add valid neighbors to the exploration stack."""
        for next_node, distance in sorted(self.connections[current].items()):
            if next_node not in visited:
                new_visited = visited | frozenset([next_node])  # Create a new frozenset for visited
                stack.append((next_node, path_length + distance, new_visited))

    def print_path(self, best_path: List[Tuple[int, int]]):
        """Print the grid with the path followed."""
        # Create a grid representation
        grid_representation = [["#" for _ in range(self.width)] for _ in range(self.height)]

        # Mark the path
        for row in range(self.height):
            for col in range(self.width):
                if (row, col) in best_path:
                    grid_representation[row][col] = "O"  # Mark the path
                elif self.grid[row][col] == TileType.PATH.value:
                    grid_representation[row][col] = "."  # Mark the original path
                else:
                    grid_representation[row][col] = "#"  # Mark walls

        # Mark the start and end positions
        start_row, start_col = self.start
        end_row, end_col = self.end
        grid_representation[start_row][start_col] = "S"  # Start
        grid_representation[end_row][end_col] = ">"  # End

        # Print the grid
        for row in grid_representation:
            print("".join(row))

def parse_hiking_trail(input_str: str) -> HikingTrail:
    """
    Parse the input string into a HikingTrail object.

    Args:
        input_str: Multiline string representing the hiking trail map

    Returns:
        HikingTrail object with the parsed grid and start/end positions

    Raises:
        ValueError: If the input is invalid or missing start/end positions
    """
    # Split input into lines and create grid
    lines = input_str.strip().split("\n")
    grid = [list(line.strip()) for line in lines]

    if not grid or not grid[0]:
        raise ValueError("Empty grid")

    # Find start position (single path in top row)
    start_col = grid[0].index(TileType.PATH.value)
    start = (0, start_col)

    # Find end position (single path in bottom row)
    end_col = grid[-1].index(TileType.PATH.value)
    end = (len(grid) - 1, end_col)

    # Validate that start and end positions are unique in their rows
    if grid[0].count(TileType.PATH.value) != 1:
        raise ValueError("Multiple or no start positions found")
    if grid[-1].count(TileType.PATH.value) != 1:
        raise ValueError("Multiple or no end positions found")

    return HikingTrail(grid, start, end)

def solve_part_one(input):
    trail = parse_hiking_trail(input)
    return trail.find_longest_path(ignore_slopes=False)

def parse_input(input_str: str) -> List[List[str]]:
    """Parse the input string into a grid."""
    return [list(line.strip()) for line in input_str.strip().split('\n')]

@dataclass(frozen=True)
class Node:
    row: int
    col: int
    
    def __hash__(self):
        return hash((self.row, self.col))
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

class CollapsedGraph:
    def __init__(self):
        self.edges: Dict[Node, Dict[Node, int]] = defaultdict(dict)
        self.start: Node = None
        self.end: Node = None

    def add_edge(self, from_node: Node, to_node: Node, weight: int):
        """Add a weighted edge between nodes."""
        self.edges[from_node][to_node] = weight

    def get_neighbors(self, node: Node) -> Dict[Node, int]:
        """Get all neighboring nodes and their weights."""
        return self.edges[node]

    def find_longest_path(self) -> int:
        """Find the longest path from start to end using iterative DFS."""
        # Stack entries: (current_node, path_length, visited_nodes)
        stack = [(self.start, 0, frozenset([self.start]))]
        max_length = float('-inf')
        
        while stack:
            current, path_length, visited = stack.pop()
            
            if current == self.end:
                max_length = max(max_length, path_length)
                continue
            
            # Add all unvisited neighbors to the stack
            # Sort by weight to try heavier paths first (potential optimization)
            neighbors = sorted(
                [(next_node, weight) for next_node, weight in self.edges[current].items()
                 if next_node not in visited],
                key=lambda x: x[1],
                reverse=True
            )
            
            for next_node, weight in neighbors:
                new_visited = frozenset([*visited, next_node])
                stack.append((next_node, path_length + weight, new_visited))
        
        return max_length if max_length != float('-inf') else -1

def build_collapsed_graph(grid: List[List[str]], ignore_slopes: bool = False) -> CollapsedGraph:
    """Build a graph with all passthrough nodes collapsed."""
    height = len(grid)
    width = len(grid[0])
    graph = CollapsedGraph()
    
    def get_neighbors(node: Node) -> List[Tuple[Node, int]]:
        """Get valid neighboring nodes and movement cost."""
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row = node.row + dr
            new_col = node.col + dc
            if (0 <= new_row < height and 0 <= new_col < width and 
                grid[new_row][new_col] != '#'):
                
                # Handle slopes if not ignoring them
                if not ignore_slopes:
                    current_tile = grid[node.row][node.col]
                    if current_tile in ('^', '>', 'v', '<'):
                        slope_dirs = {'^': (-1, 0), '>': (0, 1), 
                                    'v': (1, 0), '<': (0, -1)}
                        if slope_dirs[current_tile] != (dr, dc):
                            continue
                
                neighbors.append((Node(new_row, new_col), 1))
        return neighbors

    def is_junction(node: Node) -> bool:
        """Check if a node is a junction (not a passthrough node)."""
        neighbors = get_neighbors(node)
        if len(neighbors) != 2:
            return True
        if not ignore_slopes and grid[node.row][node.col] in ('^', '>', 'v', '<'):
            return True
        return False

    def follow_path(start: Node, prev: Node) -> Tuple[Node, int]:
        """Follow a path of passthrough nodes until reaching a junction."""
        current = start
        distance = 0
        visited = {prev, start}
        
        while True:
            neighbors = get_neighbors(current)
            # Filter out the previous node and already visited nodes
            next_nodes = [(node, dist) for node, dist in neighbors 
                         if node not in visited]
            
            if not next_nodes or len(next_nodes) > 1 or is_junction(current):
                return current, distance
            
            next_node, dist = next_nodes[0]
            distance += dist
            visited.add(next_node)
            current = next_node
        
        return current, distance

    # Find start and end nodes
    start_col = grid[0].index('.')
    end_col = grid[-1].index('.')
    graph.start = Node(0, start_col)
    graph.end = Node(height - 1, end_col)
    
    # Find all junctions and build collapsed edges
    junctions = set()
    processed = set()
    
    # First identify all junctions
    for row in range(height):
        for col in range(width):
            if grid[row][col] != '#':
                node = Node(row, col)
                if is_junction(node):
                    junctions.add(node)
    
    # Then build edges between junctions
    for junction in junctions:
        if junction in processed:
            continue
            
        for next_node, initial_dist in get_neighbors(junction):
            if next_node not in processed:
                end_node, additional_dist = follow_path(next_node, junction)
                total_dist = initial_dist + additional_dist
                
                if end_node in junctions:
                    graph.add_edge(junction, end_node, total_dist)
                    graph.add_edge(end_node, junction, total_dist)
        
        processed.add(junction)
    
    return graph

def solve(grid: List[List[str]], ignore_slopes: bool = False) -> int:
    """Find the longest possible path in the grid."""
    graph = build_collapsed_graph(grid, ignore_slopes)
    return graph.find_longest_path()



def solve_part_two(input_str: str) -> int:
    """Solve part two - treating slopes as regular paths."""
    grid = parse_input(input_str)
    return solve(grid, ignore_slopes=True)
