import re
from functools import reduce
import numpy as np

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(lines):
    data = lines.splitlines()
    data = [list(row) for row in data] 

    return data

def get_schematic(data):
    schematic = np.array(list(data), dtype=np.dtype(str))
    schematic = np.pad(schematic, 1, mode='constant', constant_values=['.'])
    return schematic

def get_number_positions(matrix):
    arr = np.array(matrix)

    def get_number_indices(segment):
        indices = []
        i = 0
        while i < len(segment):
            start = i
            while i < len(segment) and segment[i].isdigit():
                i += 1
            if i > start:
                indices.append((start, i - 1))
            i += 1
        return indices

    number_positions = []

    for row in range(arr.shape[0]):
        segments = get_number_indices(arr[row])

        for start, end in segments:
            length = end - start + 1
            number_positions.append([row, start, length])

    return number_positions

def has_adjacent_symbols(row, col, length, schematic):
    section = schematic[row - 1: row + 2, col - 1: col + length + 1]

    top = np.all(section[0, :] == '.')
    bottom = np.all(section[2, :] == '.')
    left = np.all(section[:, 0] == '.')
    right = np.all(section[:, -1] == '.')

    return not all([top, bottom, left, right])
    

def extract_numbers(matrix, adjacent_numbers):
    numbers = []
    for row, col, length in adjacent_numbers:
        number_str = ''.join(matrix[row][col:col+length])
        numbers.append(int(number_str))
    return numbers

def solvePartOne(schematic):
    total = 0
    
    number_positions =  get_number_positions(schematic)

    adjacent_numbers = [
            [row, col, length] for row, col, length in number_positions
            if has_adjacent_symbols(row, col, length, schematic)
        ]
    result_numbers = extract_numbers(schematic, adjacent_numbers)
    total = sum(result_numbers)
    return total

def find_star_positions(matrix):
    star_positions = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '*':
                star_positions.append((i, j))

    return star_positions

def find_numbers_adjacent_to_star(matrix):
    adjacent_to_star = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '*':
                adjacent_cells = [
                    (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
                ]
                for x, y in adjacent_cells:
                    if 0 <= x < rows and 0 <= y < cols and matrix[x][y].isdigit():
                        adjacent_to_star.append((x, y))

    return adjacent_to_star

def solvePartTwo(schematic):
    total = 0
    number_positions = get_number_positions(schematic)
    star_positions = find_star_positions(schematic)
    
    for star_row, star_col in star_positions:
        neighbors = [
            [row, col, length] for row, col, length in number_positions 
            if row - 1 <= star_row <= row + 1 and col - 1 <= star_col <= col + length
        ]
        
        if len(neighbors) == 2:
            numbers = [
                int(''.join(schematic[row][col:col + length])) 
                for row, col, length in neighbors
            ]
            total += numbers[0] * numbers[1]

    return total