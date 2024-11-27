import puzzle
import pytest
import heapq

TEST_INPUT = """"""


def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 668 == answer    

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    answer = 788 

def test_least_heat_loss_case_1():
    grid = [
           [2, 3, 4, 3],
           [3, 2, 5, 5],
           [3, 2, 5, 4],
           [3, 4, 4, 5]
       ]
    assert puzzle.calculate_least_heat_loss(grid) == 20  # Corrected expected heat loss

def test_least_heat_loss_case_2():
    grid = [
           [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
       ]
    assert puzzle.calculate_least_heat_loss(grid) == 20  # Expected heat loss remains the same

def test_least_heat_loss_case_3():
    grid = [
           [1, 1, 1, 1],
           [1, 9, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]
       ]
    assert puzzle.calculate_least_heat_loss(grid) == 6  # Corrected expected heat loss

def test_least_heat_loss_case_4():
    grid = [
           [9, 9, 9],
           [9, 1, 9],
           [9, 9, 9]
       ]
    assert puzzle.calculate_least_heat_loss(grid) == 28  # Corrected expected heat loss

def test_least_heat_loss_case_5():
    grid = [
           [0, 1, 2],
           [1, 0, 1],
           [2, 1, 0]
       ]
    assert puzzle.calculate_least_heat_loss(grid) == 2  # Corrected expected heat loss

def test_parse():
    input_data = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
    expected_output = [
        [2,4,1,3,4,3,2,3,1,1,3,2,3],
        [3,2,1,5,4,5,3,5,3,5,6,2,3],
        [3,2,5,5,2,4,5,6,5,4,2,5,4],
        [3,4,4,6,5,8,5,8,4,5,4,5,2],
        [4,5,4,6,6,5,7,8,6,7,5,3,6],
        [1,4,3,8,5,9,8,7,9,8,4,5,4],
        [4,4,5,7,8,7,6,9,8,7,7,6,6],
        [3,6,3,7,8,7,7,9,7,9,6,5,3],
        [4,6,5,4,9,6,7,9,8,6,8,8,7],
        [4,5,6,4,6,7,9,9,8,6,4,5,3],
        [1,2,2,4,6,8,6,8,6,5,5,6,3],
        [2,5,4,6,5,4,8,8,8,7,7,3,5],
        [4,3,2,2,6,7,4,6,5,5,5,3,3]
    ]
    
    # Call the parse function
    output = puzzle.parse(input_data)
    
    # Assert that the output matches the expected output
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

def test_only_forward_left_right_movements():
    # Define a simple grid
    grid = [
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ]
    
    # Attempt to calculate least heat loss
    result = puzzle.calculate_least_heat_loss(grid)
    
    # Since the function does not return a path, we will check the result
    # The expected result should be the least heat loss from (0,0) to (2,2)
    expected_result = 2  # The path would be (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2)
    
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_movement_constraint():
    # Create a grid where the optimal path requires turning after three blocks
    grid = [
        [0, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1]
    ]
    
    # The optimal path would be:
    # Start at (0,0) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (2,3) -> (3,4) -> (4,4)
    # Heat loss: 0 + 1 + 1 + 1 + 9 + 1 + 1 + 1 = 16
    expected_heat_loss = 16
    
    # Calculate the least heat loss using the calculate_least_heat_loss function
    answer = puzzle.calculate_least_heat_loss(grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'

def test_least_heat_loss_sample_input():
    input_data = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
    expected_heat_loss = 102  # Expected result based on the provided input
    
    # Parse the input data into a matrix
    input_grid = puzzle.parse(input_data)
    
    # Calculate the least heat loss using the calculate_least_heat_loss function
    answer = puzzle.calculate_least_heat_loss(input_grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'

def test_no_backward_movement():
    grid = [
        [0, 1, 2],
        [1, 9, 1],
        [2, 1, 0]
    ]
    
    # The optimal path should be:
    # Start at (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2)
    expected_path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    expected_heat_loss = 4  # The path would be (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2)
    
    # Calculate the least heat loss using the calculate_least_heat_loss function
    answer = puzzle.calculate_least_heat_loss(grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'

def test_movement_constraint_with_turns():
    grid = [
        [0, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1]
    ]
    
    # The optimal path should be:
    # Start at (0,0) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (2,3) -> (3,4) -> (4,4)
    # Heat loss: 0 + 1 + 1 + 1 + 9 + 1 + 1 + 1 = 16
    expected_heat_loss = 16
    
    # Calculate the least heat loss using the calculate_least_heat_loss function
    answer = puzzle.calculate_least_heat_loss(grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'


def test_ultra_crucible_case_1():
    grid = [
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [9,9,9,9,9,9,9,9,9,9,9,1],
        [9,9,9,9,9,9,9,9,9,9,9,1],
        [9,9,9,9,9,9,9,9,9,9,9,1],
        [9,9,9,9,9,9,9,9,9,9,9,1]
    ]
    
    expected_heat_loss = 71  # Expected result based on the provided input
    
    # Calculate the least heat loss using the calculate_least_heat_loss_ultra function
    answer = puzzle.calculate_least_heat_loss_ultra(grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'    

def test_ultra_crucible_sample_input():
    input_data = """\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
    expected_heat_loss = 94  # Expected result based on the provided input
    
    # Parse the input data into a matrix
    grid = puzzle.parse(input_data)
    
    # Calculate the least heat loss using the calculate_least_heat_loss_ultra function
    answer =puzzle.calculate_least_heat_loss_ultra(grid)
    
    # Assert that the calculated answer matches the expected heat loss
    assert answer == expected_heat_loss, f'Expected {expected_heat_loss}, but got {answer}'     