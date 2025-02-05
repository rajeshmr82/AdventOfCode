def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    return [list(map(int, line.split())) for line in input.strip().splitlines()]

def count_safe_reports(input):
    reports = parse(input)
    result = 0
    for report in reports:
        result += all(abs(i - j) <= 3 for i, j in zip(report, report[1:])) and (all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:])))
    return result

def solve_part_one(input):
    return count_safe_reports(input)

def is_safe_report(report):
    return all(abs(i - j) <= 3 for i, j in zip(report, report[1:])) and (all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:])))

def count_safe_reports_with_dampner(input):
    reports = parse(input)
    return sum([any([is_safe_report(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports])

def solve_part_two(input):      
    return count_safe_reports_with_dampner(input)