import sys
import re
from functools import reduce
import numpy as np
import pandas as pd

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def extract_maps(lines):
    # Extract seeds
    seeds_line = lines[0]
    seeds = [int(seed) for seed in seeds_line.split(':')[1].strip().split()]

    # Extract maps
    maps = {}
    map_names = [
        "seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water",
        "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"
    ]
    
    line_index = 1
    for map_name in map_names:
        map_data = lines[line_index].split(':')
        if(len(map_data)<2):
            line_index +=1

        line_index += 1
        
        map_values = []
        while line_index < len(lines) and lines[line_index]:                      
            values = list(map(int, lines[line_index].split()))
            map_values.append(values)
            line_index += 1
        
        maps[map_name] = map_values
    
    return seeds, maps

def parse(input):
    maps = input.strip().split("\n\n")
    seeds = list(map(int, maps[0].split("seeds:")[1].strip().split()))
    return seeds, maps[1:]

def preprocess_maps(maps):
    categories = [
        "seeds",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    map_dict = {}
    for ind, map_str in enumerate(maps):
        lines = map_str.split("\n")[1:]
        map_values = [list(map(int, line.split())) for line in lines]
        map_dict[categories[ind]] = map_values
    return map_dict

def map_value(value, mapping):
    for dest, src, length in mapping:
        if src <= value < src + length:
            return dest + (value - src)
    return value

def solvePartOne(input):
    seeds, maps = parse(input)
    seed_mapping = generate_seed_mappping(seeds, maps)
    return seed_mapping['location'].min()

def generate_seed_mappping(seeds, maps):
    map_dict = preprocess_maps(maps)
    seed_mapping = pd.DataFrame(seeds, columns=["seeds"])
    
    for ind in range(len(map_dict) - 1):
        source = list(map_dict.keys())[ind]
        destination = list(map_dict.keys())[ind + 1]
        mapping = map_dict[source]
        seed_mapping[destination] = seed_mapping[source].apply(
            lambda x: map_value(int(x), mapping)
        )

    if 'location' not in seed_mapping:
        mapping = map_dict['humidity'] 
        seed_mapping['location'] = seed_mapping['humidity'].apply(
            lambda x: map_value(int(x), mapping)
        )        
    
    return seed_mapping

def construct_map(mappings):
    mappings_list = []
    for map_name, map_data in mappings.items():
        sub_list =[]
        for destination,source,range in map_data:
            sub_list.append([source, range, destination])
        mappings_list.append(sub_list)

    return mappings_list

def process_range_seeds(seed_values, seed_ranges, map_data):
    new_seeds, new_ranges = [], []
    seed_fragments, range_fragments = list(seed_values), list(seed_ranges)
    
    while seed_fragments:
        seed_start = seed_fragments.pop()
        segment_length = range_fragments.pop()
        seed_end = seed_start + segment_length
        original_seeds_count = len(new_seeds)
        
        for map_entry in map_data:
            map_bottom, map_range, destination = map_entry
            map_top = map_bottom + map_range
            
            if seed_start < map_bottom and seed_end > map_top:
                seed_fragments.extend((seed_start, map_top, seed_end))
                range_fragments.extend((map_bottom - seed_start, map_top - map_bottom,
                                        seed_end - map_top))
                new_seeds.append(destination)
                new_ranges.append(map_top - map_bottom)
                break
            
            if seed_start < map_bottom and seed_end > map_bottom:
                seed_fragments.append(seed_start)
                range_fragments.append(map_bottom - seed_start)
                new_seeds.append(destination)
                new_ranges.append(seed_end - map_bottom)
                break

            if seed_start < map_bottom and seed_end > map_bottom:
                seed_fragments.append(map_top)
                range_fragments.append(seed_end - map_top)
                new_seeds.extend((seed_start, destination))
                new_ranges.append((map_bottom - seed_start, seed_end - map_bottom))
                break

            if seed_start >= map_bottom and seed_end <= map_top:
                new_seeds.append(seed_start - map_bottom + destination)
                new_ranges.append(segment_length)
                break

        
        if len(new_seeds) == original_seeds_count:
            new_seeds.append(seed_start)
            new_ranges.append(segment_length)
        
    return new_seeds, new_ranges


def find_lowest_location(seeds, mappings):
    lowest = float("inf")
    for i in range(0, len(seeds), 2):
        current_seeds, ranges = [seeds[i]], [seeds[i + 1]]
        for mapping in mappings:
            current_seeds, ranges = process_range_seeds(current_seeds, ranges, mapping)
        lowest = min(lowest, min(current_seeds))
    return lowest

def solvePartTwo(input):
    lines = input.splitlines()
    seed_ranges, maps = extract_maps(lines)

    mapping_list = construct_map(maps)
    result = find_lowest_location(seed_ranges, mapping_list)
    return result