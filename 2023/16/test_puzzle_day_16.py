import puzzle


TEST_INPUT = """"""


def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    # assert 0 == answer

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    # assert 0 == answer

def test_simple_beam_path():
    grid = [
        ".....",
        ".....",
        "....."
    ]
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 5

def test_mirror_reflection():
    grid = [
        "..\\.",
        "....",
        "...."
    ]
    # Beam moving right hits \ mirror, should reflect downward
    # Path: (0,0) -> (0,1) -> (0,2 with \) -> (1,2) -> (2,2)
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 5

def test_splitter_straight():
    grid = [
        "..-.",
        "....",
        "...."
    ]
    # Beam moving right hits - splitter, should pass through
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 4

def test_splitter_split():
    grid = [
        "...|.",
        "....|",
        ".....",
    ]
    # Path should be:
    # 1. (0,0)->(0,1)->(0,2)->(0,3)
    # 2. Then splits at | to (1,3) and up (which goes out of bounds)
    # 3. Down path continues to (1,3)->(1,4)
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 6

def test_example_from_problem():
    grid = [
        r".|...\....",
        r"|.-.\.....",
        r".....|-...",
        r"........|.",
        r"..........",
        r".........",
        r"..../.\\..",
        r".-.-/..|..",
        r".|....-|.",
        r"..//.|...."
    ]
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 46

def test_beam_loop():
    grid = [
        "\\.\\",
        "...",
        "\\./",
    ]
    # Start at (0,0) going right
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 8

def test_multiple_beams_same_tile():
    grid = [
        ".|.",
        "-.-",
        ".|.",
    ]
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 4

def test_out_of_bounds():
    grid = [
        "\\.",
        "..",
    ]
    # Beam should stop when it goes out of bounds
    assert puzzle.calculate_energized_tiles(grid, (0, 0, "right")) == 2

def test_parse():
    input_data = (
        ".|...\....\n"
        "|.-.\\.....\n"
        ".....|-...\n"
        "........|\n"
        "..........\n"
        ".........\\\n"
        "..../.\\..\n"
        ".-.-/..|..\n"
        ".|....-|.\\\n"
        "..//.|...."
    )
    
    expected_output = [
        ".|...\....",
        "|.-.\\.....",
        ".....|-...",
        "........|",
        "..........",
        ".........\\",
        "..../.\\..",
        ".-.-/..|..",
        ".|....-|.\\",
        "..//.|...."
    ]
    
    assert puzzle.parse(input_data) == expected_output, "Test failed: Output did not match expected result."
    print("Test passed: Output matches expected result.")

