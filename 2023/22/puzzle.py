from dataclasses import dataclass
from typing import List, Tuple, Set
from collections import defaultdict

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

@dataclass
class Brick:
    start: Tuple[int, int, int]
    end: Tuple[int, int, int]
    id: str = ''  # Optional identifier for the brick

    def __post_init__(self):
        # Ensure start coordinates are <= end coordinates
        start_sum = sum(self.start)
        end_sum = sum(self.end)
        if start_sum > end_sum:
            self.start, self.end = self.end, self.start
   
    def get_positions(self) -> List[Tuple[int, int, int]]:
        """Returns all coordinate positions this brick occupies."""
        positions = []
        x1, y1, z1 = self.start
        x2, y2, z2 = self.end
        
        # Handle each possible axis of extension
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for z in range(min(z1, z2), max(z1, z2) + 1):
                    positions.append((x, y, z))
        
        return positions

class BrickStack:
    def __init__(self, bricks: List[Brick]):
        self.bricks = sorted(bricks, key=lambda b: min(b.start[2], b.end[2]))  # Sort by lowest z
        self.space = {}  # (x,y,z) -> brick_id
        self.supports = defaultdict(set)  # brick_id -> set of bricks it supports
        self.supported_by = defaultdict(set)  # brick_id -> set of bricks supporting it
        
        # Settle all bricks and build support relationships
        self.settle_bricks()
    
    def settle_bricks(self):
        """Simulate bricks falling and establish support relationships."""
        self.space.clear()
        self.supports.clear()
        self.supported_by.clear()
        
        for brick in self.bricks:
            # Find lowest possible z position for this brick
            drop_z = self._get_drop_height(brick)
            
            # Calculate offset to move brick down
            z_offset = min(brick.start[2], brick.end[2]) - drop_z
            
            # Update brick position
            brick.start = (brick.start[0], brick.start[1], brick.start[2] - z_offset)
            brick.end = (brick.end[0], brick.end[1], brick.end[2] - z_offset)
            
            # Place brick in space and update support relationships
            self._place_brick(brick)
    
    def _get_drop_height(self, brick: Brick) -> int:
        """Find the lowest possible z position for a brick."""
        min_z = 1  # Can't go below ground
        
        # Get x,y positions this brick occupies
        positions = brick.get_positions()
        lowest_points = {(x, y) for x, y, z in positions}
        
        # Find highest obstacle below brick
        max_obstacle_height = 0
        for x, y in lowest_points:
            z = min(brick.start[2], brick.end[2])
            # Check each position below brick until hit ground or obstacle
            while z > 1:
                z -= 1
                if (x, y, z) in self.space:
                    max_obstacle_height = max(max_obstacle_height, z)
                    break
        
        return max_obstacle_height + 1
    
    def _place_brick(self, brick: Brick):
        """Place brick in space and update support relationships."""
        positions = brick.get_positions()
        
        # First find what this brick is supported by
        supporters = set()
        lowest_z = min(brick.start[2], brick.end[2])
        for x, y, z in positions:
            if z == lowest_z:  # Check position below
                below_pos = (x, y, z-1)
                if below_pos in self.space:
                    supporters.add(self.space[below_pos])
        
        # Update support relationships
        for supporter_id in supporters:
            self.supports[supporter_id].add(brick.id)
            self.supported_by[brick.id].add(supporter_id)
        
        # Place brick in space
        for pos in positions:
            self.space[pos] = brick.id
    
    def find_removable_bricks(self) -> Set[str]:
        """Find bricks that can be safely removed (support no other bricks)."""
        removable = set()
        
        # A brick is removable if:
        # 1. It supports no other bricks (not in supports dict or supports empty set)
        # 2. OR all bricks it supports have multiple supporters
        for brick in self.bricks:
            can_remove = True
            for supported_brick in self.supports[brick.id]:
                # If any supported brick has only one supporter (this brick),
                # then this brick cannot be removed
                if len(self.supported_by[supported_brick]) < 2:
                    can_remove = False
                    break
            if can_remove:
                removable.add(brick.id)
        
        return removable
    
def parse_bricks(input_str: str) -> List[Brick]:

    bricks = []
    lines = input_str.strip().split('\n')
    
    for i, line in enumerate(lines):
        try:
            # Split into start and end coordinates
            start_str, end_str = line.strip().split('~')
            
            # Parse start coordinates
            start = tuple(map(int, start_str.split(',')))
            
            # Parse end coordinates
            end = tuple(map(int, end_str.split(',')))
            
            # Validate coordinate lengths
            if len(start) != 3 or len(end) != 3:
                raise ValueError(f"Invalid coordinate length in line {i + 1}: {line}")
            
            # Create brick with optional ID
            brick_id = chr(65 + i)  # A, B, C, etc.
            brick = Brick(start, end, brick_id)
            
            # Validate that brick extends in at most one dimension
            diffs = [abs(e - s) for s, e in zip(start, end)]
            if sum(1 for diff in diffs if diff > 0) > 1:
                raise ValueError(f"Invalid brick extension in line {i + 1}: {line}")
            
            bricks.append(brick)
            
        except Exception as e:
            raise ValueError(f"Error parsing line {i + 1}: {line}") from e
            
    return bricks


def solve_part_one(input):
    bricks = parse_bricks(input)
    stack = BrickStack(bricks)
    removable = stack.find_removable_bricks()
    return len(removable)


def solve_part_two(input):      
    
    result = None
    return result