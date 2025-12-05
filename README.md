# Advent of Code Setup

Automated setup script for Advent of Code that creates directory structure, downloads inputs, and generates test files.

## Features

- ✅ Creates organized directory structure (`2025/day_01/`, etc.)
- ✅ Automatically downloads puzzle inputs from adventofcode.com
- ✅ Generates solution templates with your name
- ✅ Creates pytest test files with sample and solution tests
- ✅ Creates URL shortcuts to puzzle pages
- ✅ Handles errors gracefully (retries, timeouts, etc.)

## Setup

### 1. Install dependencies

```bash
pip install requests pytest
```

### 2. Configure your session ID

Edit `new_day.py` and set your Advent of Code session ID:

```python
USER_SESSION_ID = "your_session_id_here"
```

**How to get your session ID:**
1. Log in to [adventofcode.com](https://adventofcode.com)
2. Open browser DevTools (F12)
3. Go to Application/Storage → Cookies
4. Find the `session` cookie and copy its value
5. Paste it into `new_day.py`

### 3. (Optional) Set your name

```python
AUTHOR = "Your Name"
```

## Usage

### Create a new day

```bash
# Create day 5 for 2025
python new_day.py 5

# Create day 10 for 2024
python new_day.py 10 2024
```

This creates:
```
2025/
  day_05/
    ├── puzzle.py              # Your solution code
    ├── test_puzzle_day_5.py   # Test file
    ├── input.txt              # Downloaded automatically!
    └── link.url               # Direct link to puzzle
```

### Run your solution

```bash
# Quick test
python 2025/day_05/puzzle.py

# Run all tests
pytest 2025/day_05/test_puzzle_day_5.py -v -s

# Run just part one
pytest 2025/day_05/test_puzzle_day_5.py::TestDay05::test_part_one_solution -v -s

# Run just part two
pytest 2025/day_05/test_puzzle_day_5.py::TestDay05::test_part_two_solution -v -s
```

## Workflow

1. **Create the day**: `python new_day.py 5`
2. **Add sample input**: Copy the example from the problem into `SAMPLE_INPUT` in the test file
3. **Implement parsing**: Edit the `parse()` function in `puzzle.py`
4. **Test parsing**: `pytest test_puzzle_day_5.py::TestDay05::test_parse_sample -v`
5. **Solve part one**: Implement `solve_part_one()`
6. **Test with sample**: `pytest test_puzzle_day_5.py::TestDay05::test_part_one_sample -v -s`
7. **Get real answer**: `pytest test_puzzle_day_5.py::TestDay05::test_part_one_solution -v -s`
8. **Submit and add assertion**: Once correct, add `assert result == YOUR_ANSWER` to lock it in
9. **Repeat for part two**

## File Structure

```
project/
├── new_day.py              # Setup script (run this!)
├── template/               # Template files
│   ├── puzzle.py
│   └── test_puzzle_day_.py
├── 2025/                   # Year directories created automatically
│   ├── day_01/
│   │   ├── puzzle.py
│   │   ├── test_puzzle_day_1.py
│   │   ├── input.txt
│   │   └── link.url
│   ├── day_02/
│   └── ...
└── 2024/                   # Previous years
    └── ...
```

## Tips

### Use sample tests effectively

```python
SAMPLE_INPUT = """1721
979
366
299
675
1456"""

def test_part_one_sample(self):
    data = parse(SAMPLE_INPUT)
    result = solve_part_one(data)
    assert result == 514579  # Expected answer from problem
```

### Add assertions once you get the right answer

```python
def test_part_one_solution(self):
    raw = read_input()
    data = parse(raw)
    result = solve_part_one(data)
    print(f"Part One: {result}")
    assert result == 1234567  # Your correct answer
```

This prevents regression if you refactor your code!

### Write unit tests for complex helpers

```python
def test_parse_line():
    from day_05.puzzle import parse_line
    assert parse_line("move 1 from 2 to 3") == (1, 2, 3)
```

### Common parsing patterns

```python
# Lines
lines = raw_input.splitlines()

# Numbers
numbers = [int(x) for x in raw_input.split()]

# Grid
grid = [list(line) for line in raw_input.splitlines()]

# Blocks (separated by blank lines)
blocks = raw_input.split('\\n\\n')

# Extract all numbers (including negative)
import re
numbers = [int(x) for x in re.findall(r'-?\\d+', raw_input)]
```

## Troubleshooting

**Input download fails?**
- Check your session ID is correct
- Make sure you're logged in to adventofcode.com
- The puzzle may not be released yet (check the date/time)

**Import errors in tests?**
- Make sure you're running pytest from the project root
- The test files add the parent directory to the path automatically

**Pytest not found?**
- Install it: `pip install pytest`

## Configuration Options

In `new_day.py`:

```python
DOWNLOAD_INPUT = True   # Set False to skip auto-download
AUTHOR = "Your Name"    # Your name in templates
USER_SESSION_ID = "..." # Your AoC session cookie
```

## Credits

Based on the original init.py by Alexe Simon, enhanced with automatic input download and pytest integration.