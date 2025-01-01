# 🧱 Sand Slabs

## Overview

This project simulates a 3D space containing bricks that fall and settle based on gravity and support structures. Each brick is defined by two endpoints representing its start and end positions in 3D space.

### Input Format

Each brick is represented by a line in the format:
```
x1,y1,z1~x2,y2,z2
```
where:
- `(x1,y1,z1)` is the starting point
- `(x2,y2,z2)` is the ending point
- Each brick extends in only one dimension (x, y, or z)
- Ground level is at z=0

Example input:
```
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
```

## Solution Components

### 1. Core Data Structures

#### Brick Class
```python
@dataclass
class Brick:
    start: Tuple[int, int, int]
    end: Tuple[int, int, int]
    id: str = ''
```

#### Support Graph
```python
class BrickStack:
    def __init__(self):
        self.supports = defaultdict(set)      # brick -> bricks it supports
        self.supported_by = defaultdict(set)  # brick -> bricks supporting it
        self.space = {}                       # (x,y,z) -> brick_id
```

### 2. Main Algorithms

#### Part 1: Finding Safe Bricks

The first part identifies bricks that can be safely removed without causing others to fall.

1. **Settlement Phase**
   ```python
   def settle_bricks(self):
       # Sort bricks by height (lowest z first)
       bricks = sorted(bricks, key=lambda b: min(b.start[2], b.end[2]))
       
       for brick in bricks:
           # Find lowest possible position
           lowest_z = self._get_drop_height(brick)
           # Move brick down
           self._place_brick(brick, lowest_z)
   ```

2. **Support Detection**
   ```python
   def _place_brick(self, brick, height):
       # Record all positions brick occupies
       for pos in brick.get_positions():
           self.space[pos] = brick.id
           
       # Find and record support relationships
       for supporter in self._find_supporters(brick):
           self.supports[supporter].add(brick.id)
           self.supported_by[brick.id].add(supporter)
   ```

3. **Safe Removal Check**
   ```python
   def is_safe_to_remove(self, brick_id):
       # A brick is safe to remove if:
       # 1. It supports no other bricks, or
       # 2. All bricks it supports have multiple supporters
       for supported in self.supports[brick_id]:
           if len(self.supported_by[supported]) < 2:
               return False
       return True
   ```

#### Part 2: Chain Reaction Analysis

The second part calculates how many bricks would fall if each brick were removed.

1. **Chain Reaction Detection**
   ```python
   def calculate_chain_reactions(self):
       results = {}
       for brick in self.bricks:
           falling = self.would_fall(brick.id)
           results[brick.id] = len(falling)
       return results
   ```

2. **Fall Detection (BFS)**
   ```python
   def would_fall(self, removed_brick):
       queue = deque([b for b in self.supports[removed_brick]])
       falling = set()
       
       while queue:
           brick = queue.popleft()
           if self._would_brick_fall(brick, falling | {removed_brick}):
               falling.add(brick)
               queue.extend(self.supports[brick])
               
       return falling
   ```

## Complexity Analysis

### Time Complexity
- Part 1: O(n * xyz) where:
  - n = number of bricks
  - x,y,z = dimensions of space
- Part 2: O(n²) worst case

### Space Complexity
- Support Graph: O(n)
- 3D Space Grid: O(xyz)
- Additional Working Space: O(n)

## Usage

### Basic Usage
```python
# Parse input
input_str = """
1,0,1~1,2,1
0,0,2~2,0,2
"""
bricks = parse_input(input_str)

# Create stack
stack = BrickStack(bricks)

# Part 1: Find safe bricks
removable = stack.find_removable_bricks()
print(f"Safe to remove: {removable}")

# Part 2: Calculate chain reactions
chain_reactions = stack.calculate_chain_reactions()
total_falls = sum(chain_reactions.values())
print(f"Total falling bricks: {total_falls}")
```

### Running Tests
```python
python -m pytest test_bricks.py
```

## Example Results

For the sample input:
```
Part 1: 5 bricks can be safely removed
Part 2: Total sum of falling bricks = 7
  - Removing brick A causes 6 other bricks to fall
  - Removing brick F causes 1 other brick to fall
  - Other bricks cause no falls
```