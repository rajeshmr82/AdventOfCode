

def read_input():
    with open((__file__.rstrip("puzzle.py") + "input.txt"), "r") as input_file:
        return input_file.read()


def parse(input_data):
    """Parse the input string into a list of tuples (direction, distance, color)."""
    parsed_data = []
    for line in input_data.strip().split('\n'):
        # Split the line into components
        parts = line.split()
        direction = parts[0]  # The direction (e.g., 'R')
        distance = int(parts[1])  # The distance (e.g., '6')
        
        # Append the tuple to the parsed data
        parsed_data.append((direction, distance))  # Ensure color is in the format '#70c710'
    
    return parsed_data


def solve_part_one(input):
    directions = parse(input)
    return calculate_lagoon_capacity(directions)


def solve_part_two(input):
    directions = parse_hex_instructions (input)
    return calculate_lagoon_capacity(directions)


def calculate_lagoon_capacity(directions):
    """Calculate the total area of the lagoon based on dug positions."""
    # Initialize starting position
    current_row, current_col = 0, 0  # Starting position (row, col)

    # Define direction mappings
    direction_map = {
        "R": (0, 1),   # Move right (row, col)
        "D": (1, 0),   # Move down
        "L": (0, -1),  # Move left
        "U": (-1, 0),  # Move up
    }

    perimeter = 0
    area = 0

    for direction, distance in directions:
        dy, dx = direction_map[direction]  # Get the change in row and column
        # Update the current position based on the direction and distance
        for step in range(1, distance + 1):
            new_col = current_col + dx * step

            area += new_col * dy
            perimeter += 1  # Increment perimeter for each step taken

        # Update the current position after processing the entire distance
        current_row += dy * distance
        current_col += dx * distance

    total_area = area + perimeter // 2 + 1  # Adjusting for overlaps or specific area calculation logic

    return total_area

def convert_hex_to_instructions(hex_codes):
    instructions = []
    for hex_code in hex_codes:
        # Extract the distance and direction from the hex code
        distance_hex = hex_code[1:6]  # First five digits
        direction_hex = hex_code[6]    # Last digit
        
        # Convert distance from hexadecimal to decimal
        distance = int(distance_hex, 16)
        
        # Determine the direction based on the last hex digit
        direction = {
            '0': 'R',
            '1': 'D',
            '2': 'L',
            '3': 'U'
        }[direction_hex]
        
        # Append the instruction to the list
        instructions.append((direction, distance))
    
    return instructions

def parse_hex_instructions(input_data):
    """Parse the input string into a list of tuples (direction, distance) based on hexadecimal codes."""
    parsed_data = []
    
    for line in input_data.strip().split('\n'):
        # Extract the hexadecimal color code from the line
        parts = line.split()
        hex_code = parts[-1].strip('()')  # Get the last part and remove parentheses
        
        # Extract the distance and direction from the hex code
        distance_hex = hex_code[1:6]  # First five digits
        direction_hex = hex_code[6]    # Last digit
        
        # Convert distance from hexadecimal to decimal
        distance = int(distance_hex, 16)
        
        # Determine the direction based on the last hex digit
        direction = {
            '0': 'R',
            '1': 'D',
            '2': 'L',
            '3': 'U'
        }[direction_hex]
        
        # Append the instruction to the parsed data
        parsed_data.append((direction, distance))
    
    return parsed_data
