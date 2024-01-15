from collections import defaultdict
import sys
import re
from functools import reduce
import numpy as np
import pandas as pd
from collections import deque
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


def readInput():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse(input):
    return {
        (x, y): c
        for y, r in enumerate(input.strip().split("\n"))
        for x, c in enumerate(r)
    }


def trace_path(map):
    start_x, start_y = next((x, y) for (x, y), value in map.items() if value == "S")

    x, y = start_x, start_y
    direction = (
        "N"
        if map.get((x, y - 1), "X") in "|7F"
        else "E"
        if map.get((x - 1, y), "X") in "-J7"
        else "S"
        if map.get((x, y + 1), "X") in "|LJ"
        else "W"
        if map.get((x - 1, y), "X") in "-LF"
        else "?"
    )

    steps = {}
    step_count = 0
    direction_deltas = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    direction_changes = {
        (dir1, map_char): dir2
        for (dir1, map_char), dir2 in {
            ("N", "|"): "N",
            ("N", "F"): "E",
            ("N", "7"): "W",
            ("E", "-"): "E",
            ("E", "J"): "N",
            ("E", "7"): "S",
            ("S", "|"): "S",
            ("S", "J"): "W",
            ("S", "L"): "E",
            ("W", "-"): "W",
            ("W", "L"): "N",
            ("W", "F"): "S",
        }.items()
    }

    while True:
        steps[(x, y)] = step_count

        dx, dy = direction_deltas[direction]
        x += dx
        y += dy
        step_count += 1
        if (x, y) == (start_x, start_y):
            break

        direction = direction_changes[(direction, map[(x, y)])]

    return steps, step_count


def solvePartOne(input):
    map = parse(input)
    steps, step_count = trace_path(map)
    return step_count / 2


def scan_path(map):
    steps, step_count = trace_path(map)
    x_values, y_values = zip(*map.keys())
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    inside_cells = set()

    for y in range(min_y, max_y):
        winding = 0

        for x in range(min_x, max_x):
            if (x, y) in steps and (x, y + 1) in steps:
                if steps[(x, y + 1)] == (steps[(x, y)] + 1) % step_count:
                    winding += 1
                elif steps[(x, y)] == (steps[(x, y + 1)] + 1) % step_count:
                    winding -= 1

            if (x, y) not in steps and winding != 0:
                inside_cells.add((x, y))

    return inside_cells


def solvePartTwo(input):
    map = parse(input)
    result = scan_path(map)
    return len(result)
