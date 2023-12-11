import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
import math

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    time_values = re.findall(r'\d+', re.search(r'Time:(.*)Distance:', input, re.DOTALL).group(1))
    distance_values = re.findall(r'\d+', re.search(r'Distance:(.*)', input, re.DOTALL).group(1))

    races = []
    for i in range(len(time_values)):
        race = {
            'Time': int(time_values[i]),
            'Distance': int(distance_values[i])
        }
        races.append(race)

    return races

def parse_with_kerning(input):
    # Extract the relevant sections
    time_section = re.search(r'Time:(.*?)Distance:', input, re.DOTALL).group(1)
    distance_section = re.search(r'Distance:(.*)', input, re.DOTALL).group(1)

    # Combine individual values
    combined_time = ''.join(re.findall(r'\d+', time_section))
    combined_distance = ''.join(re.findall(r'\d+', distance_section))

    # Create a single race object
    race = {
        'Time': int(combined_time),
        'Distance': int(combined_distance)
    }
    return race


def max_distance_ways(t, race_duration, race_distance, ways):
    # Base case
    if t == 0:
        return 0, 0

    # Hold the button for one more millisecond
    max_distance_hold, ways_hold = max_distance_ways(t - 1, race_duration, race_distance, ways)
    ways += ways_hold

    # Let go of the button and start moving
    max_distance_move = t * (race_duration - t)

    # If the distance covered during acceleration plus constant speed exceeds the record distance, increment ways
    if max_distance_move > race_distance:
        ways += 1

    return max(max_distance_hold, max_distance_move), ways


def solvePartOne(input):    
    result = 1

    races = parse(input)

    # Calculate the number of ways to beat the record distance for each race
    for race in races:
        race_duration = race['Time']
        record_distance = race['Distance']
        max_dist, ways = max_distance_ways(race_duration, race_duration, record_distance, 0)
        result *= ways

    return result


def ways_to_beat_record(total_time, distance):
    discriminant = total_time * total_time - (4 * distance)

    if discriminant < 0:
        return 0
    
    sqrt_discriminant = math.sqrt(discriminant)
    max_value = (total_time + sqrt_discriminant) / 2
    min_value = (total_time - sqrt_discriminant) / 2

    if min_value.is_integer():
        min_value += 1
    else:
        min_value = math.ceil(min_value)

    if max_value.is_integer():
        max_value -= 1
    else:
        max_value = math.floor(max_value)

    return int(max_value - min_value) + 1

def solvePartTwo(input):
    race = parse_with_kerning(input)
    print(f'race: {race}')
    race_duration = race['Time']
    record_distance = race['Distance']

    ways = ways_to_beat_record(race_duration, record_distance)
    return ways