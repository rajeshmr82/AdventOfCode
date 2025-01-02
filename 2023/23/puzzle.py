from typing import List, Tuple, Set
from enum import Enum

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()


class TileType(Enum):
    PATH = '.'
    FOREST = '#'
    SLOPE_UP = '^'
    SLOPE_RIGHT = '>'
    SLOPE_DOWN = 'v'
    SLOPE_LEFT = '<'

class HikingTrail:
    def __init__(self, grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]):
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
        return (0 <= row < self.height and 
                0 <= col < self.width and 
                self.grid[row][col] != TileType.FOREST.value)

    def get_tile_type(self, pos: Tuple[int, int]) -> TileType:
        """Get the type of tile at the given position."""
        row, col = pos
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise ValueError("Position out of bounds")
        
        tile = self.grid[row][col]
        return next(t for t in TileType if t.value == tile)

    def get_valid_neighbors(self, pos: Tuple[int, int], visited: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions that haven't been visited yet."""
        row, col = pos
        current_tile = self.get_tile_type(pos)
        
        # Define possible moves based on current tile type
        if current_tile == TileType.SLOPE_UP:
            possible_moves = [(row - 1, col)]
        elif current_tile == TileType.SLOPE_RIGHT:
            possible_moves = [(row, col + 1)]
        elif current_tile == TileType.SLOPE_DOWN:
            possible_moves = [(row + 1, col)]
        elif current_tile == TileType.SLOPE_LEFT:
            possible_moves = [(row, col - 1)]
        else:  # PATH tile
            possible_moves = [
                (row - 1, col),  # up
                (row, col + 1),  # right
                (row + 1, col),  # down
                (row, col - 1)   # left
            ]
        
        # Filter valid moves
        valid_moves = []
        for next_pos in possible_moves:
            if (self.is_valid_position(next_pos) and 
                next_pos not in visited):
                valid_moves.append(next_pos)
        
        return valid_moves

    def find_longest_path(self) -> int:
        """
        Find the length of the longest possible path from start to end
        without revisiting any tiles and following slope rules.
        Returns -1 if no valid path exists.
        """
        stack = [(self.start, set([self.start]))]
        max_length = 0
        while stack:
            pos, visited = stack.pop()
            if pos == self.end:
                max_length = max(max_length, len(visited))
                continue
        
            
            for next_pos in self.get_valid_neighbors(pos, visited):
                # Create a new visited set for the next position
                new_visited = visited.copy()
                new_visited.add(next_pos)
                stack.append((next_pos, new_visited))

            max_length = max(max_length, len(visited)) 

        return max_length -1

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
    lines = input_str.strip().split('\n')
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
    return trail.find_longest_path() 


def solve_part_two(input):      
    
    result = None
    return result