import pytest
import puzzle
import numpy as np

@pytest.fixture
def sample_input():
    return """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def test_parse():
    test_input = """O....#....
O.OO#....#
.....##..."""
    expected = np.array([
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0],
        [1, 0, 1, 1, 2, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0]
    ])
    np.testing.assert_array_equal(puzzle.parse(test_input), expected)

def test_tilt_north():
    test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

    expected_output = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""

    input_grid = puzzle.parse(test_input)
    expected_grid = puzzle.parse(expected_output)

    result = puzzle.tilt_north(input_grid)
    np.testing.assert_array_equal(result, expected_grid)

def test_tilt_north_no_change():
    input_grid = np.array([
        [1, 1, 1, 1, 0, 2, 0, 1, 1, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
        [0, 0, 2, 0, 0, 2, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    result = puzzle.tilt_north(input_grid)
    np.testing.assert_array_equal(result, input_grid)

def test_calculate_total_load():
    input_grid = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""
    
    grid = puzzle.parse(input_grid)
    total_load = puzzle.calculate_total_load(grid)
    assert total_load == 136

def test_solve_part_one():
    input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
    result = puzzle.solve_part_one(input)
    assert result == 136

def test_solve_part_one_with_input():
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    # assert answer == 0  # Uncomment and update when you know the expected answer

def test_solve_part_two():
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    # assert answer == 0  # Uncomment and update when you know the expected answer
