import puzzle


def test_parse_single_hailstone():
    data = "19, 13, 30 @ -2,  1, -2"
    hailstones = puzzle.parse_hailstones(data)
    
    assert len(hailstones) == 1
    hailstone = hailstones[0]
    
    assert hailstone.position == puzzle.Point3D(19, 13, 30)
    assert hailstone.velocity == puzzle.Point3D(-2, 1, -2)

def test_parse_multiple_hailstones():
    data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2"""
    
    hailstones = puzzle.parse_hailstones(data)
    
    assert len(hailstones) == 2
    assert hailstones[0].position == puzzle.Point3D(19, 13, 30)
    assert hailstones[0].velocity == puzzle.Point3D(-2, 1, -2)
    assert hailstones[1].position == puzzle.Point3D(18, 19, 22)
    assert hailstones[1].velocity == puzzle.Point3D(-1, -1, -2)

def test_position_at_time():
    hailstone = puzzle.Hailstone(
        position=puzzle.Point3D(20, 19, 15),
        velocity=puzzle.Point3D(1, -5, -3)
    )
    
    pos_at_1ns = hailstone.position_at(1)
    assert pos_at_1ns == puzzle.Point3D(21, 14, 12)
    
    pos_at_2ns = hailstone.position_at(2)
    assert pos_at_2ns == puzzle.Point3D(22, 9, 9)

def test_empty_input():
    assert puzzle.parse_hailstones("") == []

def test_collision_detection():
    test_data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

    hailstones = puzzle.parse_hailstones(test_data)
    collisions = puzzle.count_collisions(hailstones, 7, 27, 7, 27)
    assert collisions == 2, f"Expected 2 collisions, got {collisions}"
    
    # Test parallel paths
    h1 = puzzle.Hailstone(puzzle.Point3D(0, 0, 0), puzzle.Point3D(1, 1, 0))
    h2 = puzzle.Hailstone(puzzle.Point3D(1, 1, 0), puzzle.Point3D(1, 1, 0))
    assert puzzle.find_intersection_2d(h1, h2) is None
    
    # Test past collision
    h1 = puzzle.Hailstone(puzzle.Point3D(0, 0, 0), puzzle.Point3D(1, 1, 0))
    h2 = puzzle.Hailstone(puzzle.Point3D(2, 2, 0), puzzle.Point3D(-1, -1, 0))
    assert puzzle.find_intersection_2d(h1, h2) is None


def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 15558 == answer

def test_rock_trajectory():
    test_data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

    hailstones = puzzle.parse_hailstones(test_data)
    position, velocity = puzzle.find_rock_trajectory(hailstones)
    
    assert position == puzzle.Point3D(24, 13, 10), f"Expected position (24, 13, 10), got {position}"
    assert velocity == puzzle.Point3D(-3, 1, 2), f"Expected velocity (-3, 1, 2), got {velocity}"
    
    # Verify each collision
    expected_collisions = [
        (5, puzzle.Point3D(9, 18, 20)),
        (3, puzzle.Point3D(15, 16, 16)),
        (4, puzzle.Point3D(12, 17, 18)),
        (6, puzzle.Point3D(6, 19, 22)),
        (1, puzzle.Point3D(21, 14, 12))
    ]
    
    for h, (exp_time, exp_pos) in zip(hailstones, expected_collisions):
        # Verify that rock and hailstone intersect at the expected time
        rock_pos = puzzle.Point3D(
            position.x + velocity.x * exp_time,
            position.y + velocity.y * exp_time,
            position.z + velocity.z * exp_time
        )
        hail_pos = puzzle.Point3D(
            h.position.x + h.velocity.x * exp_time,
            h.position.y + h.velocity.y * exp_time,
            h.position.z + h.velocity.z * exp_time
        )
        assert rock_pos == hail_pos == exp_pos
        assert 47 == position.x + position.y + position.z

def test_solve_part_two_from_example():
    test_data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
    position_sum = puzzle.solve_part_two(test_data)
    
    assert 47 == position_sum, f"Expected 47, but got {position_sum}"

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert 765636044333842 == answer