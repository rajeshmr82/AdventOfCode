# Advent of Code 2023 - Day 16: Energized Tiles

## Overview
This project implements a simulation of a beam traversing a grid of tiles, where each tile can reflect or split the beam. The main functionalities include calculating the number of energized tiles based on the beam's path and finding the optimal configuration to maximize the energized tiles.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing a grid representation of tiles.

2. **Tile Types**:
   - **Reflectors**: Tiles that change the direction of the beam:
     - `\`: Reflects the beam based on its current direction.
     - `/`: Reflects the beam based on its current direction.
   - **Splitters**: Tiles that allow the beam to split into multiple paths:
     - `|`: Splits the beam into upward and downward paths.
   - **Empty Tiles**: Tiles that do not affect the beam's path.

3. **Beam Simulation**:
   - The beam can start from any edge tile, heading away from that edge.
   - The simulation tracks the path of the beam as it interacts with the tiles, counting the number of energized tiles.

4. **Energized Tile Calculation**:
   The total number of energized tiles is calculated based on the beam's path through the grid.

## Algorithm
The solution uses several key components:
- **Grid Parsing**: Efficient parsing of the input grid to identify tile types.
- **Beam Traversal**: Implementation of the beam's movement logic based on tile interactions.
- **Path Tracking**: Keeping track of visited tiles to count energized tiles accurately.
- **Optimal Configuration Search**: Finding the best starting position and direction to maximize energized tiles.

## Usage
To run the solver:
1. Ensure `input.txt` is present in the correct directory.
2. Run the script to get solutions for both parts.
3. Part 1 calculates the number of energized tiles for a single configuration.
4. Part 2 finds the optimal configuration to maximize the number of energized tiles.

## Testing
The project includes comprehensive pytest-based tests covering:
- Tile parsing and handling.
- Beam simulation and path tracking.
- Energized tile calculations.
- End-to-end solution verification.

Run tests with:
```bash
pytest -v -s 2023/16/test.py
``` 