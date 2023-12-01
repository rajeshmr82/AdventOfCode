import re

def readInput():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read().split()

def parse(lines):
    return lines.splitlines()

def convert_text_to_number(text):
    words_to_numbers = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    return words_to_numbers.get(text,0)

def solvePartA(data):
    total = 0
    
    for text in data:
        
        digits = re.findall(r'\d', text)
        if(digits):
            num = 10* int(digits[0])+ int(digits[-1])
            total = total + num
    return total

def solvePartB(data):
    total = 0

    
    for text in data:        
        matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', text)
        digits = [match.group(1) for match in matches]

        first_number = 0
        last_number = 0
        if(digits):
            first_number = int(digits[0]) if digits[0].isdigit() else convert_text_to_number(digits[0])
            last_number = int(digits[-1]) if digits[-1].isdigit() else convert_text_to_number(digits[-1])
                
            num = 10* first_number+ last_number

            total = total + num
    return total