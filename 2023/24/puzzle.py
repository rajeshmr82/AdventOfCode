import dataclasses
from typing import List, Tuple, Optional
from z3 import Solver, Int,sat

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()
    
@dataclasses.dataclass
class Point3D:
    x: float
    y: float
    z: float

@dataclasses.dataclass
class Hailstone:
    position: Point3D
    velocity: Point3D
    
    def position_at(self, time: float) -> Point3D:
        """Calculate position at given time (nanoseconds)"""
        return Point3D(
            self.position.x + self.velocity.x * time,
            self.position.y + self.velocity.y * time,
            self.position.z + self.velocity.z * time
        )

def parse_hailstones(data: str) -> List[Hailstone]:
    """
    Parse the input data into a list of Hailstone objects.
    
    Args:
        data (str): Multi-line string containing hailstone data
        
    Returns:
        List[Hailstone]: List of parsed Hailstone objects
    """
    hailstones = []
    
    for line in data.strip().splitlines():
        # Split position and velocity parts
        pos_str, vel_str = line.split('@')
        
        # Parse position coordinates
        px, py, pz = map(int, pos_str.strip().split(','))
        
        # Parse velocity components
        vx, vy, vz = map(int, vel_str.strip().split(','))
        
        hailstone = Hailstone(
            position=Point3D(px, py, pz),
            velocity=Point3D(vx, vy, vz)
        )
        hailstones.append(hailstone)
    
    return hailstones

def find_intersection_2d(h1: Hailstone, h2: Hailstone) -> tuple[float, float, float] :
    """
    Find intersection of two hailstones in 2D (x,y plane).
    Returns (x, y, t) where t is time of intersection, or None if no intersection.
    """
    # Get line equations in the form y = mx + b
    try:
        m1 = h1.velocity.y / h1.velocity.x
        m2 = h2.velocity.y / h2.velocity.x
    except ZeroDivisionError:
        return None
    
    # If slopes are equal, lines are parallel
    if m1 == m2:
        return None
        
    b1 = h1.position.y - m1 * h1.position.x
    b2 = h2.position.y - m2 * h2.position.x
    
    # Find intersection point
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    
    # Calculate time of intersection for both hailstones
    if h1.velocity.x != 0:
        t1 = (x - h1.position.x) / h1.velocity.x
    else:
        t1 = (y - h1.position.y) / h1.velocity.y
        
    if h2.velocity.x != 0:
        t2 = (x - h2.position.x) / h2.velocity.x
    else:
        t2 = (y - h2.position.y) / h2.velocity.y
    
    # If intersection is in the past for either hailstone, return None
    if t1 < 0 or t2 < 0:
        return None
        
    return (x, y, t1)

def count_collisions(hailstones: list[Hailstone], x_min: float, x_max: float, 
                     y_min: float, y_max: float) -> int:
    """
    Count number of hailstone pairs that collide within the given boundary.
    """
    collision_count = 0
    
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            intersection = find_intersection_2d(hailstones[i], hailstones[j])
            
            if intersection is None:
                continue
                
            x, y, _ = intersection
            
            if (x_min <= x <= x_max and y_min <= y <= y_max):
                collision_count += 1
                
    return collision_count


def solve_part_one(input):
    hailstones = parse_hailstones(input)
    return count_collisions(hailstones, 200000000000000, 400000000000000, 200000000000000, 400000000000000)

def find_rock_trajectory(hailstones: List[Hailstone], max_samples: int = 5) -> Optional[Tuple[Point3D, Point3D]]:
    """
    Find initial rock position and velocity that intersects all hailstones.
    Uses sampling to reduce problem size for large inputs.
    """
    # Sample a subset of hailstones for initial solving
    sample_size = min(max_samples, len(hailstones))
    sample_stones = hailstones[:sample_size]
    
    solver = Solver()
    
    # Rock position and velocity variables
    rx, ry, rz = Int('rx'), Int('ry'), Int('rz')
    rvx, rvy, rvz = Int('rvx'), Int('rvy'), Int('rvz')
    
    # Add equations for sampled hailstones
    for i, h in enumerate(sample_stones):
        t = Int(f't{i}')
        solver.add(t >= 0)
        
        # Position equations at collision time
        solver.add(rx + rvx * t == h.position.x + h.velocity.x * t)
        solver.add(ry + rvy * t == h.position.y + h.velocity.y * t)
        solver.add(rz + rvz * t == h.position.z + h.velocity.z * t)
    
    if solver.check() == sat:
        model = solver.model()
        position = Point3D(
            model[rx].as_long(),
            model[ry].as_long(),
            model[rz].as_long()
        )
        velocity = Point3D(
            model[rvx].as_long(),
            model[rvy].as_long(),
            model[rvz].as_long()
        )
        
        # Verify solution against all hailstones
        if verify_solution(position, velocity, hailstones):
            return position, velocity
    
    return None

def will_collide(rock_pos: Point3D, rock_vel: Point3D, hailstone: Hailstone) -> bool:
    """Check if rock will collide with a hailstone."""
    # Solve for intersection time using any non-zero relative velocity component
    if rock_vel.x != hailstone.velocity.x:
        t = (hailstone.position.x - rock_pos.x) / (rock_vel.x - hailstone.velocity.x)
    elif rock_vel.y != hailstone.velocity.y:
        t = (hailstone.position.y - rock_pos.y) / (rock_vel.y - hailstone.velocity.y)
    else:
        t = (hailstone.position.z - rock_pos.z) / (rock_vel.z - hailstone.velocity.z)
    
    if t < 0:
        return False
    
    return True

def verify_solution(position: Point3D, velocity: Point3D, hailstones: List[Hailstone]) -> bool:
    """Verify if the rock's trajectory intersects all hailstones."""
    for h in hailstones:
        if not will_collide(position, velocity, h):
            return False
    return True    

def solve_part_two(input):      
    hailstones = parse_hailstones(input)
    position, velocity = find_rock_trajectory(hailstones)
    return position.x + position.y + position.z
