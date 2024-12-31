import puzzle
import pytest
from fractions import Fraction

TEST_INPUT = """"""


def test_parse_garden_plot():
    garden_str = """
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    """
    
    expected_output = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.'],
        ['.', '#', '#', '#', '.', '#', '#', '.', '.', '#', '.'],
        ['.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', 'S', '#', '#', '#', '#', '.'],
        ['.', '#', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.'],
        ['.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.'],
        ['.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
    
    # Call the parsing function
    result = puzzle.parse(garden_str)
    
    # Assert that the result matches the expected output
    assert result == expected_output

@pytest.mark.parametrize("start_position, steps, expected_reachable_plots", [
    (
        (5, 5),  # Starting position of 'S'
        1,  # Number of steps
        1  # Expected number of reachable garden plots
    ), 
    (
        (5, 5),  # Starting position of 'S'
        2,  # Number of steps
        4  # Expected number of reachable garden plots
    ),   
    (
        (5, 5),  # Starting position of 'S'
        6,  # Number of steps
        16  # Expected number of reachable garden plots
    ),
    # Add more test cases as needed
])
def test_reachable_garden_plots(start_position, steps, expected_reachable_plots):
    garden_map = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.'],
        ['.', '#', '#', '#', '.', '#', '#', '.', '.', '#', '.'],
        ['.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.'],
        ['.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', 'S', '#', '#', '#', '#', '.'],
        ['.', '#', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.'],
        ['.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.'],
        ['.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
        
    # Call the function to calculate reachable plots
    result = puzzle.count_reachable_positions(garden_map, start_position, steps)
    
    # Assert that the result matches the expected output
    assert result == expected_reachable_plots

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 3820 == answer


# Parameterized test function
@pytest.mark.parametrize("steps, expected_reachable", [
    (6, 16),
    (10, 50),
    (50, 1594),
    (100, 6536),
    (500, 167004),
    (1000, 668697),
    (5000, 16733044),
])
def test_count_reachable_positions_infinite(steps, expected_reachable):
    # garden_map = [
    #     ".................................",
    #     ".....###.#......###.#......###.#.",
    #     ".###.##..#..###.##..#..###.##..#.",
    #     "..#.#...#....#.#...#....#.#...#..",
    #     "....#.#........#.#........#.#....",
    #     ".##...####..##...####..##...####.",
    #     ".##..#...#..##..#...#..##..#...#.",
    #     ".......##.........##.........##..",
    #     ".##.#.####..##.#.####..##.#.####.",
    #     ".##..##.##..##..##.##..##..##.##.",
    #     "................................."
    # ]

    grid = """...........
                    .....###.#.
                    .###.##..#.
                    ..#.#...#..
                    ....#.#....
                    .##..S####.
                    .##..#...#.
                    .......##..
                    .##.#.####.
                    .##..##.##.
                    ..........."""

    # start_position = (5, 5)   
    garden_map = puzzle.parse(grid)
    result = puzzle.solve_two(garden_map, steps)
    assert result == expected_reachable, f"Expected {expected_reachable} but got {result} for {steps} steps"

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert Fraction(632421652138917, 1) == answer