# Never Tell Me The Odds

This project solves a complex 3D collision detection problem involving hailstones moving through space.

## Problem Description

### Part 1: 2D Collision Detection
Given a set of hailstones with initial positions and velocities, determine how many pairs of hailstones will have their paths intersect within a specified test area, considering only their X and Y coordinates.

Each hailstone is described by:
- Initial position (px, py, pz)
- Velocity vector (vx, vy, vz)

For example:
```
19, 13, 30 @ -2,  1, -2  # Position @ Velocity
18, 19, 22 @ -1, -1, -2
```

### Part 2: Magic Rock Trajectory
Find the initial position and velocity of a rock that will collide with every hailstone. The rock:
- Must be thrown from an integer position (x, y, z)
- Must have integer velocity components
- Must perfectly collide with each hailstone at some point in time
- Maintains constant velocity (no acceleration/deceleration)

## Solution Approach

### Part 1: Path Intersection
1. For each pair of hailstones:
   - Convert paths to line equations (y = mx + b)
   - Find intersection point using simultaneous equations
   - Check if intersection:
     - Occurs in the future for both hailstones
     - Falls within test area boundaries
2. Count valid intersections

```python
def find_intersection_2d(h1: Hailstone, h2: Hailstone) -> Optional[Point]:
    # Convert to y = mx + b form
    m1 = h1.velocity.y / h1.velocity.x
    m2 = h2.velocity.y / h2.velocity.x
    b1 = h1.position.y - m1 * h1.position.x
    b2 = h2.position.y - m2 * h2.position.x
    
    # Find intersection
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    
    # Verify future collision
    t1 = (x - h1.position.x) / h1.velocity.x
    t2 = (x - h2.position.x) / h2.velocity.x
    
    return Point(x, y) if t1 > 0 and t2 > 0 else None
```

### Part 2: Rock Trajectory
Uses Z3 SMT solver to find a solution satisfying all constraints:

1. Create variables:
   - Rock position (rx, ry, rz)
   - Rock velocity (rvx, rvy, rvz)
   - Collision times (t1, t2, ..., tn) for each hailstone

2. Add constraints:
   - All variables must be integers
   - All collision times must be positive
   - For each hailstone i at time ti:
     ```
     rx + rvx * ti = hx[i] + hvx[i] * ti
     ry + rvy * ti = hy[i] + hvy[i] * ti
     rz + rvz * ti = hz[i] + hvz[i] * ti
     ```

3. Optimizations:
   - Initially solve with subset of hailstones
   - Verify solution against all hailstones
   - Use relative velocity for efficient collision checks

## Performance Considerations

- Part 1: O(n²) complexity due to checking all hailstone pairs
- Part 2: Uses Z3 solver with sampling to handle large inputs
- Memory usage proportional to number of hailstones

## Usage

```python
# Part 1
hailstones = parse_hailstones(data)
collisions = count_collisions(hailstones, x_min, x_max, y_min, y_max)

# Part 2
position, velocity = find_rock_trajectory(hailstones)
result = position.x + position.y + position.z
```