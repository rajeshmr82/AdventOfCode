import puzzle

TEST_INPUT = """"""

def test_parse():
    assert [] == None

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.readInput()
    answer = puzzle.solvePartOne(input)
    print(f'Part One : {answer}')
    # assert 0 == answer

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.readInput()
    answer = puzzle.solvePartTwo(input)
    print(f'Part Two : {answer}')
    # assert 0 == answer