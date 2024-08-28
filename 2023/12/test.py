import pytest
import puzzle

TEST_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def test_parse():
    expected_output = [
        {"row": "???.###", "rules": "1,1,3"},
        {"row": ".??..??...?##.", "rules": "1,1,3"},
        {"row": "?#?#?#?#?#?#?#?", "rules": "1,3,1,6"},
        {"row": "????.#...#...", "rules": "4,1,1"},
        {"row": "????.######..#####.", "rules": "1,6,5"},
        {"row": "?###????????", "rules": "3,2,1"},
    ]
    assert puzzle.parse_rows(TEST_INPUT) == expected_output

@pytest.mark.parametrize(
    "row, rules, expected",
    [
        ("???.###", "1,1,3", 1),
        (".??..??...?##.", "1,1,3", 4),
        ("?#?#?#?#?#?#?#?", "1,3,1,6", 1),
        ("????.#...#...", "4,1,1", 1),
        ("????.######..#####.", "1,6,5", 4),
        ("?###????????", "3,2,1", 10),
    ],
)
def test_count_combinations(row, rules, expected):
    assert puzzle.count_combinations(row, rules) == expected

def test_solvePartOne():
    assert puzzle.solvePartOne(TEST_INPUT) == 21

def test_solvePartTwo():
    assert puzzle.solvePartTwo(TEST_INPUT) == 525152

def test_pass_solveOne():
    assert puzzle.solvePartOne(puzzle.readInput()) == 7204

def test_pass_solveTwo():
    assert puzzle.solvePartTwo(puzzle.readInput()) == 1672318386674
