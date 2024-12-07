from collections import deque
import ast

def read_input():
    try:
        with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
            return input_file.read()
    except FileNotFoundError:
        print("Input file not found.")
        return ""

class Pipeline:
    def __init__(self):
        self.workflows = {}

    def register_workflow(self, name, rules):
        self.workflows[name] = rules

    def evaluate_part(self, part):
        queue = deque(['in'])  # Start from the 'in' workflow

        while queue:
            current_workflow = queue.popleft()  # Get the next workflow to evaluate
            rules = self.workflows.get(current_workflow, [])

            for rule in rules:
                # Parse the rule
                if ':' in rule:
                    condition, destination = rule.split(':', 1)
                else:
                    condition = None
                    destination = rule

                # Evaluate the condition if it exists
                if condition:
                    if evaluate_condition(condition, part):  # Use the custom evaluation function
                        # If the destination is a workflow, enqueue that workflow
                        if destination.strip() in self.workflows:
                            queue.append(destination.strip())
                            break  # Break to continue with the next workflow
                        else:
                            # If it's not a workflow, handle acceptance or rejection
                            if destination.strip() == 'R':
                                return False  # Part is rejected
                            elif destination.strip() == 'A':
                                return True  # Part is accepted
                else:
                    # If no condition exists, check for acceptance or rejection directly
                    if destination.strip() == 'R':
                        return False  # Part is rejected
                    elif destination.strip() == 'A':
                        return True  # Part is accepted
                    elif destination.strip() in self.workflows:
                        # If the destination is a workflow, enqueue that workflow
                        queue.append(destination.strip())

        return False  # If we exhaust the queue without accepting, the part is rejected

def parse(input_string):
    # Split the input into workflows and parts
    sections = input_string.strip().split("\n\n")
    workflows_section = sections[0].strip().splitlines()
    parts_section = sections[1].strip().splitlines()

    pipeline = Pipeline()
    for line in workflows_section:
        name, rules = line.split("{")
        name = name.strip()
        rules = rules.rstrip("}").strip().split(",")
        pipeline.register_workflow(name, [rule.strip() for rule in rules])

    parts = []
    for line in parts_section:
        # Replace '=' with ':' to convert to valid dictionary format
        line = line.strip().replace('=', ':')
        # Manually parse the string to create a dictionary
        part_dict = {}
        for item in line.strip('{}').split(','):
            key, value = item.split(':')
            part_dict[key.strip()] = int(value.strip())  # Convert value to int
        parts.append(part_dict)

    return pipeline, parts

def calculate_sum(pipeline, parts):
    total_sum = 0

    for part in parts:
        if pipeline.evaluate_part(part):
            total_sum += sum(part.values())  # Add the ratings to the total sum

    return total_sum

def solve_part_one(input):
    pipeline, parts = parse(input)
    return calculate_sum(pipeline, parts)

def solve_part_two(input):      
    pipeline, parts = parse(input)
    workflows = pipeline.workflows
    translated_workflows = translate_workflows(workflows)
    return count_accepted_combinations(translated_workflows)

def count_accepted_combinations(workflows):
    # Initialize splits for each variable
    splits = {
        'x': {'low': 1, 'high': 4000},
        'm': {'low': 1, 'high': 4000},
        'a': {'low': 1, 'high': 4000},
        's': {'low': 1, 'high': 4000}
    }
    total = 0

    def process_workflow(wf_name, current_ranges):
        nonlocal total
        conditions = workflows[wf_name]

        for condition in conditions:
            # Process the condition
            varname = condition['varname']
            operator = condition['operator']
            operand = condition['operand']
            destiny = condition['destiny']

            # Clone the current ranges for modification
            new_ranges = clone_ranges(current_ranges)

            print(f"wf_name: {wf_name} - new_ranges :{new_ranges}")

            # Update the ranges based on the condition
            if varname == 'x':
                update_ranges(operator, operand, current_ranges['x'], new_ranges['x'])
            elif varname == 'm':
                update_ranges(operator, operand, current_ranges['m'], new_ranges['m'])
            elif varname == 'a':
                update_ranges(operator, operand, current_ranges['a'], new_ranges['a'])
            elif varname == 's':
                update_ranges(operator, operand, current_ranges['s'], new_ranges['s'])

            # Check the destiny
            if destiny == 'R':
                continue  # Reject this path
            elif destiny == 'A':
                total += calc_arrangements(new_ranges)
            else:
                # Recur into the next workflow
                process_workflow(destiny, new_ranges)

    # Start processing from the 'in' workflow
    process_workflow('in', splits)

    return total

def clone_ranges(source):
    return {key: {'low': value['low'], 'high': value['high']} for key, value in source.items()}

def update_ranges(operator, operand, current_range, new_range):
    if operator == "<":
        new_range['high'] = operand - 1  # Set the new high value to one less than the operand
        current_range['low'] = operand  # Set the current low value to the operand
    elif operator == ">":
        new_range['low'] = operand + 1  # Set the new low value to one more than the operand
        current_range['high'] = operand  # Set the current high value to the operand

def calc_arrangements(ranges):
    result = 1
    result *= ranges['x']['high'] - ranges['x']['low'] + 1
    result *= ranges['m']['high'] - ranges['m']['low'] + 1
    result *= ranges['a']['high'] - ranges['a']['low'] + 1
    result *= ranges['s']['high'] - ranges['s']['low'] + 1
    return result

def parse_condition(condition_str):
    if ':' not in condition_str:
        return create_condition("", "", 0, condition_str)

    condition_part, destiny = condition_str.split(':', 1)
    varname = condition_part[0]
    operator = condition_part[1] if len(condition_part) > 1 else ""
    operand = int(condition_part[2:]) if operator in ("<", ">") and len(condition_part) > 2 else 0

    return create_condition(varname, operator, operand, destiny)

def create_condition(varname, operator, operand, destiny):
    return {
        "varname": varname,
        "operator": operator,
        "operand": operand,
        "destiny": destiny
    }

def translate_workflows(original_workflows):
    translated_workflows = {}

    for wf_name, conditions in original_workflows.items():
        translated_conditions = []
        for raw_condition in conditions:
            translated_conditions.append(parse_condition(raw_condition))
        translated_workflows[wf_name] = translated_conditions

    return translated_workflows

def evaluate_condition(condition, part):
    # Replace variable names with their values
    for var in ['x', 'm', 'a', 's']:
        condition = condition.replace(var, str(part[var]))

    # Evaluate the condition safely
    return eval(condition)  # Use eval here since we control the input format


