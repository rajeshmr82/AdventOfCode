from memory import Memory
from collections import deque
import collections
import math
from itertools import count

def read_input():
    try:
        with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
            return input_file.read()
    except FileNotFoundError:
        print("Input file not found.")
        return ""

def parse_input(config):
    flops = {}
    conjs = {}
    graph = {}
    lines = config.strip().splitlines()
    
    for line in lines:
        line = line.strip()
        if '->' in line:
            # Split the line into the node and its destinations
            node_part, destinations_part = line.split('->')
            node_part = node_part.strip()
            destinations = [dest.strip() for dest in destinations_part.split(',') if dest.strip()]
            
            # Determine the module type from the first character
            if node_part[0] in ['%', '&']:
                module_type = node_part[0]  # First character indicates the type
                node = node_part[1:].strip()  # The rest is the node name
            else:
                module_type = ''  # No specific type
                node = node_part.strip()  # The whole node name
            
            # Handle flip-flops and conjunctions
            if module_type == '%':
                flops[node] = False
            elif module_type == '&':
                conjs[node] = {}
            
            graph[node] = (module_type, destinations)
    
    return graph

def process_node(node,module_type, pulse, memory, graph, destinations, src, todo):  # Get the module type and destinations

    if module_type == '%':
        if pulse:
            return None  # No change for high pulse
        else:
            emit_pulse = not memory.get(node)
            memory.set(node, emit_pulse)
    elif module_type == '&':
        memory.set(f"{node}_{src}", pulse)

        emit_pulse = not all(memory.get_conjunction_memory_states(graph, node).values())
        memory.set(node, emit_pulse)
    elif node in graph:
        emit_pulse = pulse
    else:
        return None  # If the node is not in the graph, do nothing

    # Forward the new state to destinations
    if emit_pulse is not None:  
        for dest in destinations:
            todo.append((node, dest, emit_pulse))  # Forward the new state to destinations

    return emit_pulse  # Return the new pulse state to be forwarded

def push_button(graph, memory, initial_pulse=False):
    num_low = 0
    num_high = 0

    # Start processing from the broadcaster with the provided initial pulse
    todo = [(None, 'broadcaster', initial_pulse)]  # Use the initial pulse state
    while todo:
        src, node, pulse = todo.pop(0)  # Get the current task
        module_type, destinations = graph.get(node, (None, [])) # Get the module type and destinations

        if pulse:
            num_high += 1
        else:
            num_low += 1
        
        process_node(node,module_type, pulse, memory, graph, destinations, src, todo)

    return num_low, num_high, memory.state  # Return the final state of memory

def push_button_n_times(graph, memory, n, initial_pulse=False):
    total_low = 0
    total_high = 0
    state = {}

    for _ in range(n):
        num_low, num_high, state = push_button(graph, memory, initial_pulse)
        total_low += num_low
        total_high += num_high
        initial_pulse = False  # Set initial pulse to False for subsequent presses

    return total_low, total_high, state  # Return total counts and final state


def solve_part_one(input_data):

    # Use the parse_input function to convert the text into a graph structure
    graph = parse_input(input_data)

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Push the button 1000 times
    total_low, total_high, state = push_button_n_times(graph, memory, 1000, initial_pulse=False)

    # Calculate the product of low and high pulses
    product = total_low * total_high

    # Return the product (or you can print it if needed)
    return product

def decode_flip_flop_chain(graph, start_node):
    bin = ''
    m2 = start_node
    while True:
        # Get the module type and destinations for the current node
        module_type, destinations = graph.get(m2, (None, []))
        
        # Append '1' or '0' based on the conditions
        if module_type is not None:
            bin = ('1' if len(destinations) == 2 or destinations[0] not in graph else '0') + bin
        
        # Find the next connected node(s)
        next_nodes = [next_ for next_ in destinations if next_ in graph]
        if not next_nodes:
            break  # No further connections, exit the loop
        m2 = next_nodes[0]  # Continue with the first next node
    
    return int(bin, 2)  # Convert binary string to integer

def fewest_button_presses_to_rx(graph, memory):
    res = []
    _, destinations = graph.get('broadcaster', (None, [])) 
    for destination in destinations:
        # Use the new function to decode the flip-flop chain
        res.append(decode_flip_flop_chain(graph, destination))

    # Calculate and return the least common multiple of the integers
    return math.lcm(*res) if res else None  # Return None if res is empty

def get_binary_string_for_connected_node(graph, connected):
    binary_string = ''
    while True:
        module_type, destinations = graph.get(connected, (None, []))
        
        # Early exit if there are no destinations
        if not destinations:
            break
        
        # Construct the binary string based on the conditions
        binary_string = ('1' if len(destinations) == 2 or graph.get(destinations[0], (None, []))[0] != '%' else '0') + binary_string
        
        # Find all flip-flops in the destinations
        flip_flops = [dest for dest in destinations if graph.get(dest, (None, []))[0] == '%']
        if not flip_flops:
            break
        
        connected = flip_flops[0]  # Move to the first flip-flop
    
    return int(binary_string, 2)  # Convert binary string to integer

def solve_part_two(input_data):
    graph = parse_input(input_data)
    results = []
    _, broadcaster_destinations = graph.get('broadcaster', (None, []))
    
    for connected in broadcaster_destinations:
        binary_value = get_binary_string_for_connected_node(graph, connected)
        results.append(binary_value)
    
    presses_needed = math.lcm(*results) if results else None

    return presses_needed 