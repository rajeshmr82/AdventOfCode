import pytest
import puzzle

TEST_INPUT = """"""


def test_parse_valid_input():
    input_str = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3"""

    bricks = puzzle.parse_bricks(input_str)
    assert len(bricks) == 3
    assert bricks[0].start == (1, 0, 1)
    assert bricks[0].end == (1, 2, 1)


def test_parse_with_ids():
    input_str = "1,0,1~1,2,1\n0,0,2~2,0,2"
    bricks = puzzle.parse_bricks(input_str)
    assert bricks[0].id == "A"
    assert bricks[1].id == "B"


def test_get_all_positions():
    brick = puzzle.Brick((1, 0, 1), (1, 2, 1))
    positions = brick.get_positions()
    assert len(positions) == 3
    assert (1, 0, 1) in positions
    assert (1, 1, 1) in positions
    assert (1, 2, 1) in positions


def test_invalid_coordinate_format():
    with pytest.raises(ValueError):
        puzzle.parse_bricks("1,0~1,2,1")


def test_invalid_extension():
    with pytest.raises(ValueError):
        puzzle.parse_bricks("0,0,1~1,1,2")  # Extends in multiple dimensions


def test_normalize_coordinates():
    brick = puzzle.Brick((2, 2, 2), (0, 0, 0))
    assert brick.start == (0, 0, 0)
    assert brick.end == (2, 2, 2)


def test_vertical_brick():
    brick = puzzle.Brick((0, 0, 1), (0, 0, 10))
    positions = brick.get_positions()
    assert len(positions) == 10
    assert all(pos[0] == 0 and pos[1] == 0 for pos in positions)
    assert all(1 <= pos[2] <= 10 for pos in positions)


def test_find_removable_bricks():
    input_str = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

    bricks = puzzle.parse_bricks(input_str)
    stack = puzzle.BrickStack(bricks)
    removable = stack.find_removable_bricks()

    # Assert the expected removable bricks
    expected_removable = {"G", "B", "C", "D", "E"}
    assert set(removable) == expected_removable


def test_solve_part_one(capsys):
    print("Solving Part One:")
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f"Part One : {answer}")
    assert 492 == answer


def test_chain_reactions():
    input_str = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
    bricks = puzzle.parse_bricks(input_str)
    stack = puzzle.BrickStack(bricks)
    chain_reactions = stack.calculate_chain_reactions()

    # Sum all chain reactions
    total_falls = sum(chain_reactions.values())

    # Print detailed results
    print("\nChain reaction results:")
    for brick_id, fall_count in sorted(chain_reactions.items()):
        print(
            f"Removing brick {brick_id} would cause {fall_count} other bricks to fall"
        )
    print(f"\nTotal sum of falling bricks: {total_falls}")

    assert 7 == total_falls


def test_solve_part_two(capsys):
    print("Solving Part Two:")
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f"Part Two : {answer}")
    assert 86556 == answer
