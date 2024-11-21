# Advent of Code 2023 - Day 15: Lens Library

## Overview
This project implements a hash algorithm and lens organization system. The main functionalities include calculating hash values for strings, processing initialization sequences, and managing a system of boxes containing lenses with specific focal lengths.

## How It Works
1. **Input Reading**: The input is read from a text file named `input.txt`, containing a comma-separated sequence of initialization steps.

2. **HASH Algorithm**:
   The HASH algorithm processes strings into numbers (0-255) through these steps:
   - Start with a current value of 0
   - For each character:
     1. Add its ASCII code to the current value
     2. Multiply the current value by 17
     3. Set the current value to remainder when divided by 256

3. **Lens Management System**:
   - **Parsing**: Each step in the sequence is parsed into:
     - Label (string)
     - Operation (= or -)
     - Focal Length (number, only for = operations)
   
   - **Box Operations**:
     - 256 boxes (numbered 0-255)
     - Box number determined by HASH of lens label
     - Two types of operations:
       - Remove (-): Remove lens with matching label
       - Add/Replace (=): Add new lens or replace existing one

4. **Focusing Power Calculation**:
   Total focusing power is sum of individual lens powers:
   - Box number + 1
   - Slot number (1-based)
   - Focal length
   These three values are multiplied together for each lens.

## Algorithm
The solution uses several key components:
- **String Processing**: Efficient parsing of comma-separated input
- **Hash Calculation**: Implementation of the HASH algorithm
- **Box Management**: Array-based storage of lenses with O(n) operations
- **Power Calculation**: Linear processing of final box states

## Usage
To run the solver:
1. Ensure input.txt is present in the correct directory
2. Run the script to get solutions for both parts
3. Part 1 gives sum of HASH values
4. Part 2 gives total focusing power

## Testing
The project includes comprehensive pytest-based tests covering:
- HASH algorithm functionality
- Step parsing
- Box operations
- Focusing power calculations
- End-to-end solution verification

Run tests with:
```bash
pytest -v -s 2023/15/test.py
``` 