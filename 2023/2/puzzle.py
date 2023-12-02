import re
from functools import reduce

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(lines):
    return lines.splitlines()


def solvePartA(data):
    total = 0
    availability = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

    for game in data:
        pattern = r'Game (\d+): ((?:[^;]+)(?:;[^;]+)*)'
        matches = re.match(pattern, game)
        game_possible = True
        if matches:
            game_id = matches.group(1)
            sets = matches.group(2).split(';')

            for s in sets:
                color_quantity = re.findall(r'(\d+) (\w+)', s)
                for quantity, color in color_quantity:
                    if color in availability and int(quantity) > availability[color]:
                        game_possible = False
                        break
  
        if(game_possible):
            total += int(game_id)

    return total

def solvePartB(data):
    total = 0
    pattern = r'Game (\d+): ((?:[^;]+)(?:;[^;]+)*)'
    for game in data:        
        matches = re.match(pattern, game)
        color_counts = {}
        if matches:
            sets = matches.group(2).split(';')
            for s in sets:
                color_quantity = re.findall(r'(\d+) (\w+)', s)
                for quantity, color in color_quantity:
                    if color in color_counts:
                        color_counts[color] = max(color_counts[color],int(quantity))
                    else:
                        color_counts[color] = int(quantity)            

        total += reduce(lambda x, y: x * y, color_counts.values(), 1)
    return total