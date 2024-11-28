import puzzle

TEST_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

def test_parse():
    test_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)"""
    
    expected_output = [
        ('R', 6, '#70c710'),
        ('D', 5, '#0dc571'),
        ('L', 2, '#5713f0'),
        ('D', 2, '#d2c081'),
        ('R', 2, '#59c680')
    ]
    
    assert puzzle.parse(test_input) == expected_output

def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 46359 == answer

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    # assert 0 == answer

def test_calculate_lagoon_capacity():
    directions = puzzle.parse(TEST_INPUT)
    capacity = puzzle.calculate_lagoon_capacity(directions)
    assert capacity == 62  # Expected capacity of the lagoon