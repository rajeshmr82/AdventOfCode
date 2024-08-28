from functools import lru_cache


def readInput():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse_rows(input_string):
    return [
        {"row": line.split()[0], "rules": line.split()[1]}
        for line in input_string.splitlines()
    ]


def count_combinations(row, rules):
    groups = tuple(map(int, rules.split(",")))
    
    @lru_cache(maxsize=None)
    def solve(row, group_index=0, current_group_count=0):
        if group_index == len(groups):
            return '#' not in row
        if not row:
            return group_index == len(groups) - 1 and current_group_count == groups[group_index]
        
        result = 0
        if row[0] in '.?':
            if current_group_count == groups[group_index]:
                result += solve(row[1:], group_index + 1, 0)
            elif current_group_count == 0:
                result += solve(row[1:], group_index, 0)
        if row[0] in '#?':
            if group_index < len(groups) and current_group_count < groups[group_index]:
                result += solve(row[1:], group_index, current_group_count + 1)
        
        return result

    return solve(row)


def solvePartOne(input):
    return sum(count_combinations(**data) for data in parse_rows(input))


def solvePartTwo(input):
    return sum(
        count_combinations('?'.join([data["row"]] * 5), ','.join([data["rules"]] * 5))
        for data in parse_rows(input)
    )
