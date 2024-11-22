import pytest
import puzzle

TEST_INPUT = """.....
.S-7.
.|.|.
.L-J.
....."""

TEST_INPUT2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

TEST_INPUT3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

TEST_INPUT4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

def test_parse():
    map = puzzle.parse(TEST_INPUT)
    expected = {
        (0, 0): ".", (1, 0): ".", (2, 0): ".", (3, 0): ".", (4, 0): ".",
        (0, 1): ".", (1, 1): "S", (2, 1): "-", (3, 1): "7", (4, 1): ".",
        (0, 2): ".", (1, 2): "|", (2, 2): ".", (3, 2): "|", (4, 2): ".",
        (0, 3): ".", (1, 3): "L", (2, 3): "-", (3, 3): "J", (4, 3): ".",
        (0, 4): ".", (1, 4): ".", (2, 4): ".", (3, 4): ".", (4, 4): ".",
    }
    assert map == expected

def test_trace_map():
    map = puzzle.parse(TEST_INPUT)
    steps, step_count = puzzle.trace_path(map)
    expected = {
        (1, 1): 0, (1, 2): 1, (1, 3): 2, (2, 3): 3,
        (3, 3): 4, (3, 2): 5, (3, 1): 6, (2, 1): 7,
    }
    assert steps == expected

def test_compute_distance_simple():
    map = puzzle.parse(TEST_INPUT)
    steps, step_count = puzzle.trace_path(map)
    assert 4 == step_count / 2

def test_compute_distance_complex():
    map = puzzle.parse(TEST_INPUT2)
    steps, step_count = puzzle.trace_path(map)
    assert 8 == step_count / 2

def test_pass_solveOne(capsys):
    print("Solving Part One:")
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f"Part One : {answer}")
    assert 7097 == answer

def test_tiles_enclosed_simple():
    map = puzzle.parse(TEST_INPUT3)
    result = puzzle.scan_path(map)
    assert {(2, 6), (3, 6), (7, 6), (8, 6)} == result

def test_tiles_enclosed_complex():
    map = puzzle.parse(TEST_INPUT4)
    result = puzzle.scan_path(map)
    expected = {(7, 4), (8, 4), (14, 6), (14, 3), (6, 6), (7, 5), (8, 5), (9, 4)}
    assert expected == result

def test_pass_solveTwo(capsys):
    print("Solving Part Two:")
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f"Part Two : {answer}")
    # Original commented assertion left as-is
    # assert 0 == answer
