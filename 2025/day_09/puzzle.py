"""
Advent of Code 2025 - Day 9
Author: Rajesh M R
"""

from itertools import combinations
from pathlib import Path


def read_input(filename="input.txt"):
    """Read and return the input file contents."""
    input_path = Path(__file__).parent / filename
    return input_path.read_text().strip()


def parse(raw_input):
    """
    Parse the raw input into list of tuples.

    """
    return [tuple(map(int, line.split(","))) for line in raw_input.splitlines()]


def solve_part_one(tiles):
    """
    Solve part one of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part one
    """

    return max(
        (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
        for i, j in combinations(range(len(tiles)), 2)
    )


def is_on_boundary(point, tiles):
    """Check if point is on the polygon boundary."""
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]

        x, y = point

        # Check if point is on this edge
        if x1 == x2:  # Vertical edge
            if x == x1 and min(y1, y2) <= y <= max(y1, y2):
                return True
        else:  # Horizontal edge
            if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True

    return False


def is_point_inside_polygon(point, polygon):
    """
    Ray casting algorithm to check if point is inside polygon.

    Args:
        point: (x, y) coordinate to test
        polygon: List of polygon vertices

    Returns:
        True if point is inside polygon, False otherwise
    """
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]

        # Check if point is on horizontal edge crossing
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside

        p1x, p1y = p2x, p2y

    return inside


def build_green_tile_cache(tiles):
    """
    Build a cache for is_inside/on_boundary checks using memoization.
    This avoids recalculating the same point multiple times.
    """
    cache = {}
    red_tiles = set(tiles)

    def is_green_or_red(point):
        if point in cache:
            return cache[point]

        if point in red_tiles:
            result = True
        elif is_on_boundary(point, tiles) or is_point_inside_polygon(point, tiles):
            result = True
        else:
            result = False

        cache[point] = result
        return result

    return is_green_or_red


def does_polygon_edge_intersect_rectangle(
    rect_min_x, rect_min_y, rect_max_x, rect_max_y, tiles
):
    """
    Check if any polygon edge passes through the interior of the rectangle.
    An edge crosses if it has points STRICTLY inside the rectangle interior.
    Edges that only touch the boundary are OK.
    """
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % len(tiles)]

        # For vertical edges (x1 == x2)
        if x1 == x2:
            edge_x = x1
            edge_min_y = min(y1, y2)
            edge_max_y = max(y1, y2)

            # Edge must be strictly inside rectangle's x-range
            if rect_min_x < edge_x < rect_max_x:
                # Edge must have points strictly inside rectangle's y-range
                interior_min_y = max(edge_min_y, rect_min_y)
                interior_max_y = min(edge_max_y, rect_max_y)

                # If there are points strictly inside, reject
                if interior_min_y < interior_max_y:
                    return True

        # For horizontal edges (y1 == y2)
        else:
            edge_y = y1
            edge_min_x = min(x1, x2)
            edge_max_x = max(x1, x2)

            # Edge must be strictly inside rectangle's y-range
            if rect_min_y < edge_y < rect_max_y:
                # Edge must have points strictly inside rectangle's x-range
                interior_min_x = max(edge_min_x, rect_min_x)
                interior_max_x = min(edge_max_x, rect_max_x)

                # If there are points strictly inside, reject
                if interior_min_x < interior_max_x:
                    return True

    return False


def is_rectangle_valid(p1, p2, is_green_or_red_func, tiles):
    """
    Check if ALL tiles in rectangle are red or green.

    For rectilinear polygons, a rectangle is fully inside if:
    1. All 4 corners are inside/on the polygon
    2. No polygon edges pass through the rectangle interior

    This is sufficient - we don't need to check every point!
    """
    x1, y1 = p1
    x2, y2 = p2

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check all 4 corners are inside or on boundary
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for corner in corners:
        if not is_green_or_red_func(corner):
            return False

    if does_polygon_edge_intersect_rectangle(min_x, min_y, max_x, max_y, tiles):
        return False

    return True


def solve_part_two(tiles):
    """
    Solve part two of the puzzle.

    Args:
        data: Parsed input data

    Returns:
        The answer to part two
    """
    # Build memoized check function
    is_green_or_red_func = build_green_tile_cache(tiles)

    max_area = 0
    checked = 0
    total_pairs = len(tiles) * (len(tiles) - 1) // 2

    # Try all pairs of red tiles
    for i, j in combinations(range(len(tiles)), 2):
        p1, p2 = tiles[i], tiles[j]
        checked += 1

        if checked % 10000 == 0:
            print(
                f"Progress: {checked}/{total_pairs} pairs checked, max_area so far: {max_area}"
            )

        if is_rectangle_valid(p1, p2, is_green_or_red_func, tiles):
            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if area > max_area:
                max_area = area
                print(f"New max area found: {max_area} at ({p1}, {p2})")

    return max_area


# Helper functions (add as needed)
def helper_function(param):
    """Example helper function."""
    pass


if __name__ == "__main__":
    # Quick test run
    raw = read_input()
    data = parse(raw)

    print("=" * 50)
    print(f"Advent of Code 2025 - Day 9")
    print("=" * 50)

    answer_one = solve_part_one(data)
    print(f"Part One: {answer_one}")

    answer_two = solve_part_two(data)
    print(f"Part Two: {answer_two}")

    print("=" * 50)
