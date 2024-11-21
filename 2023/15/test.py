import puzzle

TEST_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert answer == 505427

def test_hash_empty_string():
    assert puzzle.hash("") == 0

def test_hash_single_char():
    assert puzzle.hash("H") == 200  # 72 * 17 % 256

def test_hash_example():
    assert puzzle.hash("HASH") == 52

def test_hash_initialization_steps():
    test_cases = {
        "rn=1": 30,
        "cm-": 253,
        "qp=3": 97,
        "cm=2": 47,
        "qp-": 14,
        "pc=4": 180,
        "ot=9": 9,
        "ab=5": 197,
        "pc-": 48,
        "pc=6": 214,
        "ot=7": 231
    }
    
    for input_str, expected in test_cases.items():
        assert puzzle.hash(input_str) == expected, f"Failed for {input_str}"

def test_hash_full_sequence():
    sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    steps = sequence.split(',')
    total = sum(puzzle.hash(step) for step in steps)
    assert total == 1320

def test_hash_algorithm_steps():
    """Test each step of the HASH algorithm for 'HASH'"""
    # This test helps verify the intermediate values
    values = puzzle.hash_with_steps("HASH")
    expected = [
        72,    # After 'H': ASCII 72
        200,   # After 'H': (72 * 17) % 256
        265,   # After 'A': 200 + 65
        153,   # After 'A': (265 * 17) % 256
        236,   # After 'S': 153 + 83
        172,   # After 'S': (236 * 17) % 256
        244,   # After 'H': 172 + 72
        52     # Final: (244 * 17) % 256
    ]
    assert values == expected

def test_parse_step():
    test_cases = [
        ("rn=1", ("rn", "=", 1)),
        ("cm-", ("cm", "-", None)),
        ("qp=3", ("qp", "=", 3)),
    ]
    for input_str, expected in test_cases:
        assert puzzle.parse_step(input_str) == expected

def test_process_sequence():
    sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    boxes = puzzle.process_sequence(sequence)
    
    # Test final state of boxes
    expected_box_0 = [("rn", 1), ("cm", 2)]
    expected_box_3 = [("ot", 7), ("ab", 5), ("pc", 6)]
    
    assert boxes[0] == expected_box_0
    assert boxes[3] == expected_box_3
    # All other boxes should be empty
    assert boxes[1] == []
    assert boxes[2] == []

def test_calculate_focusing_power():
    # Create a test state of boxes
    boxes = [[] for _ in range(256)]
    boxes[0] = [("rn", 1), ("cm", 2)]
    boxes[3] = [("ot", 7), ("ab", 5), ("pc", 6)]
    
    expected_powers = {
        ("rn", 1, 0): 1,  # 1 * 1 * 1
        ("cm", 2, 0): 4,  # 1 * 2 * 2
        ("ot", 7, 3): 28, # 4 * 1 * 7
        ("ab", 5, 3): 40, # 4 * 2 * 5
        ("pc", 6, 3): 72, # 4 * 3 * 6
    }
    
    total_power = puzzle.calculate_focusing_power(boxes)
    assert total_power == 145

def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert answer == 243747

def test_solve_part_two_with_file(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert answer == 243747

