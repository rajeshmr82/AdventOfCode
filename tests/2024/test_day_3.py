import pytest
import sys
sys.path.append('2024/day_03')
import puzzle


@pytest.fixture
def sample_input_string():
    return """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def test_get_pattern(sample_input_string):
    assert puzzle.get_pattern(sample_input_string) == 161

def test_solve_part_one():
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 161289189 == answer    

def test_get_all_pattern(sample_input_string):
    assert puzzle.get_all_instructions(sample_input_string) == 48

def test_solve_part_two():
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert 83595109 == answer    