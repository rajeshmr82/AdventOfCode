"""
Tests for Advent of Code 2025 - Day 5
Author: Rajesh M R
"""

import pytest
from puzzle import (
    Range,
    read_input,
    parse,
    solve_part_one,
    solve_part_two,
)


# Sample input from problem description (paste the example here)
SAMPLE_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


class TestRange:
    """Tests for the Range class."""

    def test_range_contains_with_in_operator(self):
        """Test that Range supports 'in' operator (Pythonic)."""
        r = Range(5, 10)

        assert 5 in r
        assert 7 in r
        assert 10 in r
        assert 4 not in r
        assert 11 not in r

    def test_range_with_negative_numbers(self):
        """Test Range with negative numbers."""
        r = Range(-5, 5)

        assert -5 in r
        assert 0 in r
        assert 5 in r
        assert -6 not in r
        assert 6 not in r


class TestRangeMerging:
    """Tests for range merging optimization."""

    def test_merge_overlapping_ranges(self):
        """Test that overlapping ranges are merged."""
        text = """1-5
3-7

10"""

        db = parse(text)

        # Ranges 1-5 and 3-7 overlap, should merge to 1-7
        assert len(db.fresh_ranges) == 1
        assert db.fresh_ranges[0].start == 1
        assert db.fresh_ranges[0].end == 7

    def test_merge_adjacent_ranges(self):
        """Test that adjacent ranges are merged."""
        text = """1-5
6-10

1"""

        db = parse(text)

        # Ranges 1-5 and 6-10 are adjacent, should merge to 1-10
        assert len(db.fresh_ranges) == 1
        assert db.fresh_ranges[0].start == 1
        assert db.fresh_ranges[0].end == 10

    def test_no_merge_for_separate_ranges(self):
        """Test that non-overlapping ranges stay separate."""
        text = """1-5
10-15

1"""

        db = parse(text)

        # Ranges 1-5 and 10-15 don't overlap, should stay separate
        assert len(db.fresh_ranges) == 2

    def test_merge_multiple_overlapping_ranges(self):
        """Test merging multiple overlapping ranges."""
        text = """3-5
10-14
16-20
12-18

1"""

        db = parse(text)

        # 10-14 and 12-18 overlap -> merge to 10-18
        # 10-18 and 16-20 overlap -> merge to 10-20
        # Result: 3-5 and 10-20
        assert len(db.fresh_ranges) == 2

        # Check the merged ranges
        ranges = sorted([(r.start, r.end) for r in db.fresh_ranges])
        assert ranges == [(3, 5), (10, 20)]


class TestOptimizedParsing:
    """Tests for the optimized parser."""

    def test_basic_parsing(self):
        """Test basic parsing with the example from the problem."""
        text = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

        db = parse(text)

        # Check that ranges are stored (not expanded)
        assert len(db.fresh_ranges) <= 4  # Could be merged

        # Check freshness using range checking
        assert db.is_fresh(3) is True
        assert db.is_fresh(4) is True
        assert db.is_fresh(5) is True
        assert db.is_fresh(11) is True
        assert db.is_fresh(17) is True

        assert db.is_fresh(1) is False
        assert db.is_fresh(6) is False
        assert db.is_fresh(32) is False

        # Check available ingredient IDs
        assert db.available_ids == [1, 5, 8, 11, 17, 32]

    def test_large_range_efficiency(self):
        """Test that large ranges don't cause memory issues."""
        text = """1-1000000000
2000000000-3000000000

500000000
2500000000
5000000000"""

        db = parse(text)

        # Should only store 2 ranges, not billions of IDs
        assert len(db.fresh_ranges) == 2

        # Check freshness
        assert db.is_fresh(1) is True
        assert db.is_fresh(500000000) is True
        assert db.is_fresh(1000000000) is True
        assert db.is_fresh(2500000000) is True
        assert db.is_fresh(1500000000) is False

    def test_many_ranges(self):
        """Test efficiency with many ranges (175+)."""
        # Create 200 non-overlapping ranges
        ranges = [f"{i * 1000}-{i * 1000 + 100}" for i in range(200)]
        text = "\n".join(ranges) + "\n\n" + "5050\n15050\n25050"

        db = parse(text)

        # Should store 200 ranges
        assert len(db.fresh_ranges) == 200

        # Check specific IDs
        assert db.is_fresh(5050) is True
        assert db.is_fresh(15050) is True
        assert db.is_fresh(5500) is False  # Between ranges 5000-5100 and 6000-6100


class TestPythonicAPI:
    """Tests for Pythonic API improvements."""

    def test_fresh_available_property(self):
        """Test the fresh_available property (Pythonic)."""
        text = """3-5
10-14

1
5
8
11
17"""

        db = parse(text)

        # Use property instead of method
        fresh_and_available = db.fresh_available
        assert fresh_and_available == [5, 11]

    def test_len_method(self):
        """Test the __len__ method (Pythonic)."""
        text = """1-3

5
10
15"""

        db = parse(text)

        assert len(db) == 3

    def test_repr_method(self):
        """Test the __repr__ method (Pythonic)."""
        text = """1-3

5
10"""

        db = parse(text)

        repr_str = repr(db)
        assert "IngredientDatabase" in repr_str
        assert "ranges=" in repr_str
        assert "available=" in repr_str


class TestOptimizedMethods:
    """Tests for optimized method implementations."""

    def test_is_fresh_method(self):
        """Test the is_fresh method with range checking."""
        text = """3-5

1"""

        db = parse(text)

        assert db.is_fresh(3) is True
        assert db.is_fresh(4) is True
        assert db.is_fresh(5) is True
        assert db.is_fresh(1) is False
        assert db.is_fresh(6) is False

    def test_is_available_method(self):
        """Test the is_available method."""
        text = """1-3

5
10
15"""

        db = parse(text)

        assert db.is_available(5) is True
        assert db.is_available(10) is True
        assert db.is_available(15) is True
        assert db.is_available(1) is False
        assert db.is_available(20) is False


class TestEdgeCases:
    """Tests for edge cases with optimized parser."""

    def test_empty_string(self):
        """Test parsing an empty string."""
        text = ""

        db = parse(text)
        assert len(db.fresh_ranges) == 0
        assert db.available_ids == []

    def test_negative_ranges(self):
        """Test that negative ranges work correctly."""
        text = """-5--1
1-3

-3
0
2"""

        db = parse(text)

        assert db.is_fresh(-5) is True
        assert db.is_fresh(-3) is True
        assert db.is_fresh(-1) is True
        assert db.is_fresh(0) is False
        assert db.is_fresh(1) is True
        assert db.is_fresh(2) is True

    def test_single_element_range(self):
        """Test ranges with a single element."""
        text = """5-5
10-10

5"""

        db = parse(text)

        assert db.is_fresh(5) is True
        assert db.is_fresh(10) is True
        assert db.is_fresh(4) is False
        assert db.is_fresh(6) is False


class TestPerformanceComparison:
    """Tests demonstrating performance benefits."""

    def test_memory_efficiency_large_ranges(self):
        """Demonstrate memory efficiency with huge ranges."""
        # This would use ~8GB if we stored all IDs in a set
        # With ranges, it uses just a few bytes
        text = """0-1000000000

500000000"""

        db = parse(text)

        # Only stores 1 range object
        assert len(db.fresh_ranges) == 1

        # But can still check any ID instantly
        assert db.is_fresh(0) is True
        assert db.is_fresh(500000000) is True
        assert db.is_fresh(1000000000) is True
        assert db.is_fresh(1000000001) is False

    def test_query_performance_many_checks(self):
        """Test performance with many lookups."""
        # Create database with many ranges
        ranges = [f"{i * 100}-{i * 100 + 50}" for i in range(100)]
        text = "\n".join(ranges) + "\n\n"

        # Add 1000 available IDs
        available = [str(i) for i in range(0, 10000, 10)]
        text += "\n".join(available)

        db = parse(text)

        # Get all fresh available ingredients
        fresh_available = db.fresh_available

        # Should find those that fall in the ranges
        assert len(fresh_available) > 0

        # Verify they're all actually fresh
        for id in fresh_available:
            assert db.is_fresh(id) is True


class TestErrorHandling:
    """Tests for error handling."""

    def test_missing_blank_line(self):
        """Test that missing blank line raises an error."""
        text = """1-5
10"""

        with pytest.raises(ValueError, match="missing blank line separator"):
            parse(text)

    def test_invalid_range_format(self):
        """Test that invalid ranges raise errors."""
        text = """1-5
abc-def

10"""

        with pytest.raises(ValueError, match="Invalid range format"):
            parse(text)

    def test_invalid_range_order(self):
        """Test that start > end raises an error."""
        text = """10-5

1"""

        with pytest.raises(ValueError, match="Invalid range.*start must be <= end"):
            parse(text)


class TestDay05:
    """Test cases for Day 5 solutions."""

    def test_part_one_sample(self):
        """Test part one with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_one(data)
            print(f"Part One (sample): {result}")
            assert result == 3

    def test_part_one_solution(self):
        """Test part one with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_one(data)
        print(f"\n{'=' * 50}")
        print(f"🎄 Part One Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 505

    def test_part_two_sample(self):
        """Test part two with sample input."""
        if SAMPLE_INPUT:
            data = parse(SAMPLE_INPUT)
            result = solve_part_two(data)
            print(f"Part Two (sample): {result}")
            assert result == 14

    def test_part_two_solution(self):
        """Test part two with actual input."""
        raw = read_input()
        data = parse(raw)
        result = solve_part_two(data)
        print(f"\n{'=' * 50}")
        print(f"⭐ Part Two Solution: {result}")
        print(f"{'=' * 50}")
        assert result == 344423158480189


if __name__ == "__main__":
    # Run with: python test_puzzle_day_5.py
    # Or: pytest test_puzzle_day_5.py -v -s
    pytest.main([__file__, "-v", "-s"])
