import pytest
import puzzle

TEST_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


@pytest.fixture
def parsed_grid():
    parsed = puzzle.parse(TEST_INPUT)
    return puzzle.expand_grid(parsed)


@pytest.fixture
def parsed_grid_without_expand():
    return puzzle.parse(TEST_INPUT)


@pytest.fixture
def object_positions(parsed_grid):
    return puzzle.find_object_positions(parsed_grid)


def test_parse(parsed_grid):
    expected_grid = [
        "....#........",
        ".........#...",
        "#............",
        ".............",
        ".............",
        "........#....",
        ".#...........",
        "............#",
        ".............",
        ".............",
        ".........#...",
        "#....#.......",
    ]
    assert parsed_grid == expected_grid, "Parsed grid does not match expected output."


def test_find_object_positions(object_positions):
    expected_positions = [
        (0, 4),
        (1, 9),
        (2, 0),
        (5, 8),
        (6, 1),
        (7, 12),
        (10, 9),
        (11, 0),
        (11, 5),
    ]
    assert (
        object_positions == expected_positions
    ), "Object positions do not match expected values."


def test_compute_all_distances(object_positions):
    expected_distances = {
        (0, 1): 6,
        (0, 2): 6,
        (0, 3): 9,
        (0, 4): 9,
        (0, 5): 15,
        (0, 6): 15,
        (0, 7): 15,
        (0, 8): 12,
        (1, 2): 10,
        (1, 3): 5,
        (1, 4): 13,
        (1, 5): 9,
        (1, 6): 9,
        (1, 7): 19,
        (1, 8): 14,
        (2, 3): 11,
        (2, 4): 5,
        (2, 5): 17,
        (2, 6): 17,
        (2, 7): 9,
        (2, 8): 14,
        (3, 4): 8,
        (3, 5): 6,
        (3, 6): 6,
        (3, 7): 14,
        (3, 8): 9,
        (4, 5): 12,
        (4, 6): 12,
        (4, 7): 6,
        (4, 8): 9,
        (5, 6): 6,
        (5, 7): 16,
        (5, 8): 11,
        (6, 7): 10,
        (6, 8): 5,
        (7, 8): 5,
    }

    computed_distances = puzzle.compute_all_distances_manhattan(object_positions)
    assert (
        computed_distances == expected_distances
    ), "Computed distances do not match expected values."


def test_sum_of_shortest_paths(object_positions):
    computed_sum = puzzle.sum_of_shortest_paths(object_positions)
    expected_sum = 374
    assert (
        computed_sum == expected_sum
    ), f"Computed sum {computed_sum} does not match the expected sum {expected_sum}."


def test_pass_solveOne():
    print("Solving Part One:")
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    expected_sum = 9543156
    assert answer == expected_sum, f"Expected {expected_sum}, but got {answer}"


def test_expand_grid_by_10(parsed_grid_without_expand):
    computed_sum = puzzle.sum_of_shortest_paths_with_factor_expansion(
        parsed_grid_without_expand, 10
    )

    expected_sum = 1030  # Expected sum when expanding by 10
    assert (
        computed_sum == expected_sum
    ), f"Expected {expected_sum}, but got {computed_sum}"


def test_expand_grid_by_100(parsed_grid_without_expand):
    computed_sum = puzzle.sum_of_shortest_paths_with_factor_expansion(
        parsed_grid_without_expand, 100
    )

    expected_sum = 8410  # Expected sum when expanding by 100
    assert (
        computed_sum == expected_sum
    ), f"Expected {expected_sum}, but got {computed_sum}"


def test_pass_solveTwo():
    print("Solving Part Two:")
    input_data = puzzle.readInput()
    answer = puzzle.solvePartTwo(input_data)
    print(f"Part Two : {answer}")
    expected_sum = 625243292686
    assert answer == expected_sum, f"Expected {expected_sum}, but got {answer}"
