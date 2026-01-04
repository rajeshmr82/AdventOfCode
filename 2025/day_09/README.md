# Advent of Code 2025 - Day 9

## Problem Overview

This problem involves finding the largest axis-aligned rectangle that can be formed using a list of coordinate points under different constraints.

## Part 1: Maximum Rectangle from Any Two Red Tiles

### Problem Statement
Given a list of red tiles (coordinate points), find the largest axis-aligned rectangle where two red tiles are at opposite corners.

### Intuition

The key insight is straightforward:
- Any two points can define a rectangle by treating them as opposite corners
- The rectangle is axis-aligned (sides parallel to x and y axes)
- We just need to check all possible pairs of red tiles

### Algorithm

```
For each pair of red tiles (p1, p2):
    width = |p2.x - p1.x| + 1
    height = |p2.y - p1.y| + 1
    area = width × height
    max_area = max(max_area, area)
```

### Complexity
- **Time**: O(n²) where n is the number of red tiles
- **Space**: O(1)

This is very efficient since we're only iterating through all pairs and computing areas.

## Part 2: Maximum Rectangle Using Only Red or Green Tiles

### Problem Statement
Now there's an additional constraint:
- Red tiles form the vertices of a closed polygon
- Green tiles are all points **on the polygon boundary** or **inside the polygon**
- The rectangle must use **only red or green tiles** (no tiles outside the polygon)
- Two red tiles must still be at opposite corners

### Key Insight: Rectilinear Polygon

The critical observation is that **all polygon edges are axis-aligned** (horizontal or vertical). This makes it a **rectilinear polygon**, which enables efficient validation.

### Why This Matters

For a rectilinear polygon, we can efficiently check if a rectangle is fully inside without examining every single point:

**Theorem**: A rectangle is fully contained within a rectilinear polygon if and only if:
1. All 4 corners of the rectangle are inside or on the polygon boundary
2. No polygon edges pass through the rectangle's interior

### Algorithm

```python
# Precompute: Build a cache for "is this point green or red?"
cache = memoized function for is_green_or_red(point)

For each pair of red tiles (p1, p2):
    # Check if rectangle is valid
    if all 4 corners are green/red:
        if no polygon edges cross through interior:
            area = width × height
            max_area = max(max_area, area)
```

### Edge Intersection Detection

To check if a polygon edge crosses through a rectangle's interior:

**For vertical edges** (x constant):
- Edge must be strictly inside rectangle's x-range: `rect_min_x < edge_x < rect_max_x`
- Edge must have points strictly inside rectangle's y-range
- Calculate overlap: `interior_overlap = [max(edge_min_y, rect_min_y), min(edge_max_y, rect_max_y)]`
- If `interior_min < interior_max`, the edge crosses through

**For horizontal edges** (y constant):
- Similar logic with x and y swapped

**Important**: Edges that merely touch the rectangle boundary are allowed!

### Optimizations

1. **Memoization**: Cache polygon membership checks since we test many rectangles
   - Without caching: Each point check is O(n) for polygon with n vertices
   - With caching: First check is O(n), subsequent checks are O(1)

2. **Early Rejection**: Check corners first
   - If any corner is outside, immediately reject without checking edges

3. **Geometric Theorem**: Avoid checking every point in the rectangle
   - For huge rectangles (e.g., 89,531 × 16,419 = 1.47 billion points!)
   - Only need to check corners + edge crossings

### Complexity

- **Time**: O(n² × (m + n))
  - n² pairs of red tiles
  - m checks per rectangle (corners + edge intersections)
  - n vertices in polygon for each check
- **Space**: O(k) where k is the number of unique points checked (cached)

### Why Simple Approaches Fail

**Naive approach**: Check every point in every rectangle
- For the actual input: ~495 red tiles → ~122,760 pairs
- Largest rectangle: ~1.47 billion points
- Would require checking trillions of points!

**Sampling approach**: Only check some points
- Might miss "holes" or indentations in the polygon
- Not mathematically guaranteed to be correct

**The correct approach** uses geometric properties of rectilinear polygons to achieve both correctness and efficiency.

## Results

- **Part 1**: 4,781,377,701
- **Part 2**: 1,470,616,992

The Part 2 answer corresponds to a rectangle from `(5254, 66490)` to `(94821, 50072)` with dimensions 89,568 × 16,419.
