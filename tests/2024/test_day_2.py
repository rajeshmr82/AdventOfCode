import pytest
import sys
sys.path.append('2024/day_02')
import puzzle


@pytest.fixture
def sample_input_string():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def test_part_one_for_sample(sample_input_string):  
    assert puzzle.count_safe_reports(sample_input_string) == 2    

def test_solve_part_one():
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 598 == answer    

def test_part_two_for_sample(sample_input_string):  
    assert puzzle.count_safe_reports_with_dampner(sample_input_string) == 4      

def test_solve_part_two():
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert 634 == answer    