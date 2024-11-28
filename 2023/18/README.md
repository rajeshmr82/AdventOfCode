# Advent of Code 2023 - Day 18: Lagoon Capacity

## Overview
This project calculates the lagoon capacity based on movement instructions parsed from input data. The main functionalities include parsing input data, calculating the total area of the lagoon based on dug positions, and handling movement constraints.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing movement instructions in either plain text or hexadecimal format.

2. **Movement Instructions**:
   - Each instruction consists of a direction (right, down, left, up) and a distance.
   - Instructions can be provided in both standard and hexadecimal formats.

3. **Lagoon Capacity Calculation**:
   - The total area of the lagoon is calculated based on the positions dug by the movements.
   - The algorithm tracks the area and perimeter as the movements are processed.

## Algorithm
The solution employs several key components:
- **Input Parsing**: Efficient parsing of the input data to extract movement instructions.
- **Movement Logic**: Implementation of movement rules, ensuring that the constraints are respected.
- **Area Calculation**: Keeping track of the area and perimeter to accurately calculate the lagoon capacity.
- **Hexadecimal Support**: Ability to parse and convert hexadecimal instructions into standard movement instructions.

## Usage
To run the solver:
1. Ensure `input.txt` is present in the correct directory.
2. Run the script to get solutions for both parts.
3. Part 1 calculates the lagoon capacity based on standard instructions.
4. Part 2 finds the lagoon capacity based on hexadecimal instructions.

## Testing
The project includes comprehensive pytest-based tests covering:
- Input parsing and handling.
- Movement logic for the lagoon.
- Area and perimeter calculations.
- End-to-end solution verification.

Run tests with:
```
pytest