import re
def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()


def get_pattern(input):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, input)
    return sum([int(match[0]) * int(match[1]) for match in matches])


def solve_part_one(input):
    return get_pattern(input)

def get_all_instructions(input):
    enabled = True
    result = 0

    for match in re.finditer(r'(?:mul\((\d{1,3}),(\d{1,3})\)|(?:don\'t|do|undo)\(\))', input):
        if 'mul' in match.group():
            if enabled:
                x, y = map(int, match.groups())
                result += x * y
        else:
            if 'don\'t' in match.group():
                enabled = False
            elif 'do' in match.group() or 'undo' in match.group():
                enabled = True

    return result

def solve_part_two(input):      
    return get_all_instructions(input)