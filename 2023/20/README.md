# Advent of Code 2023 - Day 20: Graph Traversal and Flip-Flop Counting

## Overview
This project calculates the total number of button presses required based on a series of flip-flops and their connections in a graph structure. The main functionalities include parsing graph data, processing connections, and counting the necessary button presses based on specific conditions.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing definitions of flip-flops and their connections.

2. **Graph Definitions**:
   - Each flip-flop is represented as a node in a graph, with connections to other flip-flops or conjunctions.
   - The graph structure allows for efficient traversal and condition checking.

3. **Button Press Counting**:
   - The total number of button presses is calculated based on the conditions defined in the graph.
   - The algorithm tracks the state of each flip-flop and applies conditions recursively to determine the required button presses.

## Logic Explanation
The logic for counting button presses involves the following key steps:

### Part 1: Basic Flip-Flop Counting
1. **Graph Initialization**: The algorithm starts by parsing the input to create a graph representation of the flip-flops and their connections.

2. **Traversal and Counting**: The main function processes each flip-flop:
   - It traverses the graph to find connected flip-flops.
   - For each flip-flop, it checks the conditions to determine if it contributes to the button press count.

3. **Condition Evaluation**: The algorithm evaluates conditions based on the connections:
   - If a flip-flop connects to a conjunction, it is counted as a button press.
   - The algorithm continues traversing until no further connections are found.

### Part 2: Advanced Flip-Flop Counting with Binary Representation
1. **Binary String Construction**: In this part, the algorithm constructs a binary string representation of the flip-flop states:
   - Each flip-flop's state is represented as a bit in the binary string.
   - The algorithm evaluates conditions to determine whether to append '1' or '0' to the binary string.

2. **Iterative Processing**: The algorithm iteratively processes each flip-flop:
   - It checks the number of connections and updates the binary string based on the conditions.
   - The traversal continues until all reachable flip-flops are processed.

3. **Final Count Calculation**: Once the binary string is constructed, it is converted to an integer to represent the total button presses required.

## Usage
To run the solver:
1. Ensure `input.txt` is present in the correct directory.
2. Run the script to get the total number of button presses required for both parts of the solution.
3. The program processes the graph and outputs the results.

## Testing
The project includes comprehensive pytest-based tests covering:
- Input parsing and handling.
- Graph traversal and condition processing logic.
- Button press counting for both parts of the solution.
- End-to-end solution verification.

Run tests with:
```
pytest
``` 