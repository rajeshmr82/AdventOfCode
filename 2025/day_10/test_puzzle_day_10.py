"""
Tests for Advent of Code 2025 - Day 10
Author: Rajesh M R
"""

import pytest
from puzzle import read_input, parse, solve_part_one, solve_part_two

SAMPLE_INPUT = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


class TestMachineParsing:
    """Test cases for Machine class and parsing."""

    def test_parse_single_machine_line(self):
        """Test parsing a single machine configuration line."""
        from puzzle import Machine

        line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
        machine = Machine.from_line(line)

        # Check target state: [.##.] means [False, True, True, False]
        assert machine.target == [False, True, True, False]
        assert machine.num_lights == 4

        # Check buttons: (3) (1,3) (2) (2,3) (0,2) (0,1)
        assert machine.buttons == [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]

        # Joltages can be stored but ignored
        assert machine.joltages == [3, 5, 4, 7]

    def test_parse_second_machine_line(self):
        """Test parsing second example machine."""
        from puzzle import Machine

        line = "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
        machine = Machine.from_line(line)

        # Check target state: [...#.] means [False, False, False, True, False]
        assert machine.target == [False, False, False, True, False]
        assert machine.num_lights == 5

        # Check buttons
        assert machine.buttons == [
            [0, 2, 3, 4],
            [2, 3],
            [0, 4],
            [0, 1, 2],
            [1, 2, 3, 4],
        ]

        assert machine.joltages == [7, 5, 12, 7, 2]

    def test_parse_third_machine_line(self):
        """Test parsing third example machine."""
        from puzzle import Machine

        line = "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
        machine = Machine.from_line(line)

        # Check target state: [.###.#] means [False, True, True, True, False, True]
        assert machine.target == [False, True, True, True, False, True]
        assert machine.num_lights == 6

        # Check buttons
        assert machine.buttons == [[0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]]

        assert machine.joltages == [10, 11, 11, 5, 10, 5]

    def test_parse_returns_list_of_machines(self):
        """Test that parse returns a list of Machine objects."""
        machines = parse(SAMPLE_INPUT)

        assert len(machines) == 3
        assert all(hasattr(m, "target") for m in machines)
        assert all(hasattr(m, "buttons") for m in machines)

        # Verify first machine
        assert machines[0].num_lights == 4
        assert machines[0].target == [False, True, True, False]

        # Verify second machine
        assert machines[1].num_lights == 5
        assert machines[1].target == [False, False, False, True, False]

        # Verify third machine
        assert machines[2].num_lights == 6
        assert machines[2].target == [False, True, True, True, False, True]


class TestMachineSolver:
    """Test cases for solving machines."""

    def test_fewest_buttons_machine_1(self):
        """Test minimum button presses for first machine."""
        from puzzle import Machine

        line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
        machine = Machine.from_line(line)
        result = machine.fewest_buttons()
        assert result == 2, f"Expected 2, got {result}"

    def test_fewest_buttons_machine_2(self):
        """Test minimum button presses for second machine."""
        from puzzle import Machine

        line = "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
        machine = Machine.from_line(line)
        result = machine.fewest_buttons()
        assert result == 3, f"Expected 3, got {result}"

    def test_fewest_buttons_machine_3(self):
        """Test minimum button presses for third machine."""
        from puzzle import Machine

        line = "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
        machine = Machine.from_line(line)
        result = machine.fewest_buttons()
        assert result == 2, f"Expected 2, got {result}"


class TestDay10:
    """Test cases for Day 10 solutions."""

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 7, f"Expected 7, got {result}"

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 449

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 33

    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'=' * 50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 17848


if __name__ == "__main__":
    # Run with: python test_puzzle_day_10.py
    # Or: pytest test_puzzle_day_10.py -v -s
    pytest.main([__file__, "-v", "-s"])
