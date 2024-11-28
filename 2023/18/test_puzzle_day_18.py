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
        ('R', 6),
        ('D', 5),
        ('L', 2),
        ('D', 2),
        ('R', 2)
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
    assert 59574883048274 == answer

def test_calculate_lagoon_capacity():
    directions = puzzle.parse(TEST_INPUT)
    capacity = puzzle.calculate_lagoon_capacity(directions)
    assert capacity == 62  # Expected capacity of the lagoon

def test_convert_hex_to_instructions():
    hex_codes = [
        "#70c710",  # R 461937
        "#0dc571",  # D 56407
        "#5713f0",  # R 356671
        "#d2c081",  # D 863240
        "#59c680",  # R 367720
        "#411b91",  # D 266681
        "#8ceee2",  # L 577262
        "#caa173",  # U 829975
        "#1b58a2",  # L 112010
        "#caa171",  # D 829975
        "#7807d2",  # L 491645
        "#a77fa3",  # U 686074
        "#015232",  # L 5411
        "#7a21e3"   # U 500254
    ]
    
    expected_instructions = [
        ('R', 461937),
        ('D', 56407),
        ('R', 356671),
        ('D', 863240),
        ('R', 367720),
        ('D', 266681),
        ('L', 577262),
        ('U', 829975),
        ('L', 112010),
        ('D', 829975),
        ('L', 491645),
        ('U', 686074),
        ('L', 5411),
        ('U', 500254)
    ]
    
    # Call the conversion function
    instructions = puzzle.convert_hex_to_instructions(hex_codes)
    
    # Assert that the output matches the expected instructions
    assert instructions == expected_instructions, f"Expected {expected_instructions}, but got {instructions}"

def test_parse_hex_instructions():
    test_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)"""
    
    expected_output = [
        ('R', 461937),
        ('D', 56407),
        ('R', 356671),
        ('D', 863240),
        ('R', 367720)
    ]
    
    # Call the conversion function
    instructions = puzzle.parse_hex_instructions(test_input)
    
    # Assert that the output matches the expected instructions
    assert instructions == expected_output, f"Expected {expected_output}, but got {instructions}"

def test_calculate_area_from_hex():
    test_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
#411b91 (#266681)
#8ceee2 (#577262)
#caa173 (#829975)
#1b58a2 (#112010)
#caa171 (#829975)
#7807d2 (#491645)
#a77fa3 (#686074)
#015232 (#5411)
#7a21e3 (#500254)"""
    
    expected_area = 952408144115
    directions = puzzle.parse_hex_instructions(TEST_INPUT)
    # Call the area calculation function
    area = puzzle.calculate_lagoon_capacity(directions)
    
    # Assert that the output matches the expected area
    assert area == expected_area, f"Expected {expected_area}, but got {area}"
