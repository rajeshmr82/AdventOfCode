import puzzle
import pytest

def test_parse_valid_hiking_trail():
    input_str = """
#.###
#...#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.start == (0, 1)
    assert trail.end == (2, 3)
    assert trail.width == 5
    assert trail.height == 3

def test_parse_hiking_trail_with_slopes():
    input_str = """
#.###
#v..#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.get_tile_type((1, 1)) == puzzle.TileType.SLOPE_DOWN

def test_is_valid_position():
    input_str = """
#.###
#...#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.is_valid_position((1, 1)) == True  # Path
    assert trail.is_valid_position((0, 0)) == False  # Forest
    assert trail.is_valid_position((-1, 0)) == False  # Out of bounds

def test_invalid_grid_dimensions():
    input_str = """
#.###
#..#
###.#
""".strip()
    with pytest.raises(ValueError):
        puzzle.parse_hiking_trail(input_str)

def test_multiple_start_positions():
    input_str = """
#..##
#...#
###.#
""".strip()
    with pytest.raises(ValueError, match="Multiple or no start positions found"):
        puzzle.parse_hiking_trail(input_str)


def test_simple_path():
    input_str = """
#.###
#...#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.find_longest_path() == 4  # Path: (0,1) -> (1,1) -> (1,2) -> (2,3)

def test_path_with_slopes():
    input_str = """
#.###
#v..#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.find_longest_path() == -1  # Only one valid path due to slope

def test_no_valid_path():
    input_str = """
#.###
#^..#
###.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.find_longest_path() == -1  # No valid path due to upward slope

def test_path_with_multiple_slopes():
    input_str = """
#.####
#v...#
#>v..#
####.#
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.find_longest_path() == 3  # Must follow slopes

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 2250 == answer

def test_example_from_problem():
    input_str = """
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
""".strip()
    trail = puzzle.parse_hiking_trail(input_str)
    assert trail.start == (0, 1)
    assert trail.end == (22, 21)
    assert trail.get_tile_type((3, 12)) == puzzle.TileType.SLOPE_RIGHT
    assert trail.get_tile_type((4, 3)) == puzzle.TileType.SLOPE_DOWN
    # The example has a path of length 94 (including end tile, excluding start tile)
    assert trail.find_longest_path() == 94

def test_example_from_problem_without_slopes():
    input_str = """
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
""".strip()
    grid = puzzle.parse_input(input_str)
    
    assert puzzle.solve(grid, ignore_slopes=True) == 154

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert 6470 == answer