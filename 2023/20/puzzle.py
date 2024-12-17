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
    flops = set()  # Use a set for faster lookups
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
                flops.add(node)  # Store flip-flop in a set
            elif module_type == '&':
                conjs[node] = {}
            
            graph[node] = (module_type, destinations)
    
    return graph, flops  # Return both the graph and the set of flip-flops

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
    graph, flops = parse_input(input_data)

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

def get_binary_string_for_connected_node(graph, connected, flip_flops):
    binary_string = ''
    while True:
        module_type, destinations = graph.get(connected, (None, []))
        
        # Early exit if there are no destinations
        if not destinations:
            break
        
        # Construct the binary string based on the conditions
        binary_string = ('1' if len(destinations) == 2 or destinations[0] not in flip_flops else '0') + binary_string
        
        # Find all flip-flops in the destinations using the precomputed set
        flip_flops_in_destinations = [dest for dest in destinations if dest in flip_flops]
        if not flip_flops_in_destinations:
            break
        
        connected = next((dest for dest in flip_flops_in_destinations), None)  # Get the first flip-flop or None
    
    return int(binary_string, 2)  # Convert binary string to integer

def solve_part_two(input_data):
    graph,flip_flops = parse_input(input_data)
    results = []
    _, broadcaster_destinations = graph.get('broadcaster', (None, []))
    
    for connected in broadcaster_destinations:
        binary_value = get_binary_string_for_connected_node(graph, connected, flip_flops)
        results.append(binary_value)
    
    presses_needed = math.lcm(*results) if results else None

    return presses_needed 

def process_flip_flops(graph, flip_flops):
    results = []
    
    for flip_flop in flip_flops:
        state = 0  # Initialize an integer to represent the state
        connected = flip_flop
        
        while True:
            module_type, destinations = graph.get(connected, (None, []))
            
            # Early exit if there are no destinations
            if not destinations:
                break
            
            # Update the state based on the conditions
            if len(destinations) == 2 or destinations[0] not in flip_flops:
                state |= 1
            else:
                state &= ~1
            
            # Find all flip-flops in the destinations
            flip_flops_in_destinations = [dest for dest in destinations if dest in flip_flops]
            
            # get the next flip-flop or None
            connected = next((dest for dest in flip_flops_in_destinations), None)
            if connected is None:
                break  # Exit the loop if there are no flip-flops
        
        results.append(state)  # Append the final state as an integer
    
    return results 