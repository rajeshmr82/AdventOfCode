# --- Day 2: Advent of Code ---

The Advent of Code is a series of puzzles that challenge your programming skills and problem-solving abilities. In this challenge, you are tasked with analyzing reports of location IDs to determine their safety based on specific criteria.

As you dive into the reports, you discover that the Elvish Senior Historians have compiled lists of location IDs that they believe are historically significant. However, these lists are not in perfect agreement, and your job is to help reconcile them.

## Problem Overview

The goal is to determine how many reports can be considered "safe." A report is deemed safe if the absolute difference between any two consecutive location IDs is less than or equal to 3, and the IDs are either strictly increasing or strictly decreasing.

## Solution Explanation

This repository contains a solution for a problem that involves processing numerical data from a file. The solution is implemented in Python and is structured into several functions. Below is an explanation of the logic used in the solution.

### Function Breakdown

1. **`read_input()`**: 
   - This function reads the input data from a file named `input.txt` located in the same directory as the script. It returns the content of the file as a string.

   ```python
   def read_input():
       with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
           return input_file.read()
   ```

2. **`parse(input)`**: 
   - This function takes the input string, splits it into lines, and converts each line into a list of integers. It returns a list of lists, where each inner list represents a report of location IDs.

   ```python
   def parse(input):
       return [list(map(int, line.split())) for line in input.strip().splitlines()]
   ```

3. **`count_safe_reports(input)`**: 
   - This function counts the number of safe reports based on the defined criteria. It uses the `parse` function to get the reports and then checks each report to see if it meets the safety conditions.

   ```python
   def count_safe_reports(input):
       reports = parse(input)
       result = 0
       for report in reports:
           result += all(abs(i - j) <= 3 for i, j in zip(report, report[1:])) and (all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:])))
       return result
   ```

4. **`solve_part_one(input)`**: 
   - This function serves as a wrapper for `count_safe_reports`, returning the count of safe reports for Part 1 of the puzzle.

   ```python
   def solve_part_one(input):
       return count_safe_reports(input)
   ```

5. **`is_safe_report(report)`**: 
   - This helper function checks if a single report is safe by evaluating the absolute differences and the order of the IDs.

   ```python
   def is_safe_report(report):
       return all(abs(i - j) <= 3 for i, j in zip(report, report[1:])) and (all(i < j for i, j in zip(report, report[1:])) or all(i > j for i, j in zip(report, report[1:])))
   ```

6. **`count_safe_reports_with_dampner(input)`**: 
   - This function counts the number of reports that can be made safe by removing one location ID. It checks each report and uses the `is_safe_report` function to determine if the modified report is safe.

   ```python
   def count_safe_reports_with_dampner(input):
       reports = parse(input)
       return sum([any([is_safe_report(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports])
   ```

7. **`solve_part_two(input)`**: 
   - This function serves as a wrapper for `count_safe_reports_with_dampner`, returning the count of reports that can be made safe by removing one ID for Part 2 of the puzzle.

   ```python
   def solve_part_two(input):      
       return count_safe_reports_with_dampner(input)
   ```

## Conclusion

This solution effectively processes the location ID reports and determines their safety based on the specified criteria. By allowing the removal of one ID, the program enhances its ability to reconcile the lists and provide a more comprehensive analysis of the reports.
