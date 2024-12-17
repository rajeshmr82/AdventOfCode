import puzzle
from memory import Memory
import pytest

def test_parse_input():
    config = r"""
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
    modules = puzzle.parse_input(config)

    # Check that the modules are parsed correctly
    assert 'broadcaster' in modules
    assert modules['broadcaster'] == ('', ['a', 'b', 'c'])
    assert 'a' in modules
    assert modules['a'] == ('%', ['b'])
    assert 'b' in modules
    assert modules['b'] == ('%', ['c'])
    assert 'c' in modules
    assert modules['c'] == ('%', ['inv'])
    assert 'inv' in modules
    assert modules['inv'] == ('&', ['a'])

def test_conjunction_input_memory_setup():
    graph = {
        'broadcaster': ('', ['input1', 'input2']),  # Broadcaster sends to input1 and input2
        'input1': ('%', ['conjunction']),  # input1 sends to conjunction
        'input2': ('%', ['conjunction']),  # input2 sends to conjunction
        'conjunction': ('&', ['output']),  # Conjunction receives inputs from input1 and input2
        'output': ('%', [])  # Output does not have any destinations for this test
    }

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Check that the memory for each input of the conjunction is set to False
    assert memory.get('conjunction_input1') is False, "Memory for conjunction_input1 should be initialized to False"
    assert memory.get('conjunction_input2') is False, "Memory for conjunction_input2 should be initialized to False"

    # Additionally, check the initial state of the inputs
    assert memory.get('input1') is False  # Input1 should remember low pulse
    assert memory.get('input2') is False  # Input2 should remember low pulse

def test_flip_flop_behavior():
    graph = {
        'broadcaster': ('', ['flip_flop']),
        'flip_flop': ('%', [])
    }

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Check initial state before any pulses
    assert memory.get('flip_flop') is False  # State should be off

    # Test with initial low pulse
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=False)
    assert num_low == 2 
    assert num_high == 0
    assert state['flip_flop'] is True 

    # Send a low pulse to flip the state
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=False)
    assert num_low == 2 
    assert num_high == 0  
    assert state['flip_flop'] is False

    # Send a low pulse to flip the state
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=True)
    assert num_low == 0 
    assert num_high == 2  
    assert state['flip_flop'] is False    

def test_initialize_conjunction_states():
    graph = {
        'broadcaster': ('%', ['input1', 'input2']),
        'input1': ('%', ['conjunction']),
        'input2': ('%', ['conjunction']),
        'conjunction': ('&', ['output']),
        'output': ('%', [])
    }

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Initialize conjunction states
    conjs = memory.initialize_conjunction_states(graph)

    # Check that the conjunction states are set up correctly
    assert 'conjunction' in conjs  # Ensure the conjunction is in the mapping
    assert 'input1' in conjs['conjunction']  # input1 should be mapped to conjunction
    assert 'input2' in conjs['conjunction']  # input2 should be mapped to conjunction
    assert conjs['conjunction']['input1'] is False  # Initial state should be False
    assert conjs['conjunction']['input2'] is False  # Initial state should be False

def test_conjunction_module():
    graph = {
        'broadcaster': ('', ['input1', 'input2']),  # Broadcaster sends to input1 and input2
        'input1': ('%', ['conjunction']),  # input1 sends to conjunction
        'input2': ('%', ['conjunction']),  # input2 sends to conjunction
        'conjunction': ('&', ['output']),  # Conjunction receives inputs from input1 and input2 and sends to output
        'output': ('%', [])  # Output does not have any destinations for this test
    }

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph
    
    # Initial state should remember low pulses for both inputs
    assert memory.get('input1') is False  # Input1 should remember low pulse
    assert memory.get('input2') is False  # Input2 should remember low pulse

    # Simulate sending a low pulse to input1 via the broadcaster
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=False)
    assert num_low == 5  
    assert num_high == 2  
    assert memory.get('conjunction_input1') is True  # Input1 memory should be high
    assert memory.get('conjunction_input2') is True  # Input2 memory should be high 
    assert state['output'] is False  # Output should reflect the conjunction's state

    # Simulate sending a high pulse to input1 via the broadcaster
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=True)
    assert num_low == 0
    assert num_high == 3
    assert memory.get('conjunction_input1') is True  # Input1 memory should be high
    assert memory.get('conjunction_input2') is True  # Input2 memory should also be high
    assert state['output'] is False  # Output should reflect the conjunction's state

    # Simulate sending a low pulse to input2 via the broadcaster
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=False)
    assert num_low == 5
    assert num_high == 2
    assert memory.get('conjunction_input1') is False  # Input1 memory should be low
    assert memory.get('conjunction_input2') is False  # Input2 memory should be low
    assert state['output'] is False  # Output should reflect the conjunction's state

def test_broadcaster_flip_flop_inverter_sequence():
    # Define the graph structure as a text representation
    config = r"""
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """

    # Use the parse_input function to convert the text into a graph structure
    graph = puzzle.parse_input(config)

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Simulate the first button press (initial pulse is low)
    num_low, num_high, state = puzzle.push_button(graph, memory, initial_pulse=False)

    # Assert the expected counts of low and high pulses
    assert num_low == 8
    assert num_high == 4

    # Assert the final states of the flip-flop modules
    assert memory.get('a') is False  # a should be off
    assert memory.get('b') is False  # b should be off
    assert memory.get('c') is False  # c should be off
    assert memory.get('inv') is True  # inv should be on (since it inverts the last low from c)

def test_broadcaster_flip_flop_simple_conjunction():
    # Define the graph structure as a text representation
    config = r"""
    broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output
    """

    # Use the parse_input function to convert the text into a graph structure
    graph = puzzle.parse_input(config)

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Push the button the first time (initial pulse is low)
    puzzle.push_button(graph, memory, initial_pulse=False)

    # Assert the final states of the modules after the first press
    assert memory.get('a') is True  # a should be on
    assert memory.get('b') is True  # b should be on
    assert memory.get('inv') is False  # inv should be off
    assert memory.get('con') is False  # con should be off

    # Push the button the second time
    puzzle.push_button(graph, memory, initial_pulse=False)

    # Assert the final states of the modules after the second press
    assert memory.get('a') is False  # a should be off
    assert memory.get('b') is True  # b should be on
    assert memory.get('inv') is True  # inv should be on
    assert memory.get('con') is True  # con should be on

    # Push the button the third time
    puzzle.push_button(graph, memory, initial_pulse=False)

    # Assert the final states of the modules after the third press
    assert memory.get('a') is True  # a should be on
    assert memory.get('b') is False  # b should be off
    assert memory.get('inv') is False  # inv should be off
    assert memory.get('con') is True  # con should be on

    # Push the button the fourth time
    puzzle.push_button(graph, memory, initial_pulse=False)

    # Assert the final states of the modules after the fourth press
    assert memory.get('a') is False  # a should be off
    assert memory.get('b') is False  # b should be off
    assert memory.get('inv') is True  # inv should be on
    assert memory.get('con') is True  # con should be on

@pytest.mark.parametrize("config, expected_low, expected_high", [
     (
         r"""
            broadcaster -> a
            %a -> inv, con
            &inv -> b
            %b -> con
            &con -> output
         """,
         4250,  # Expected low pulses
         2750   # Expected high pulses
     ),
    (
        r"""
        broadcaster -> a, b, c
        %a -> b
        %b -> c
        %c -> inv
        &inv -> a
        """,
        8000,  # Expected low pulses
        4000   # Expected high pulses
    )
])
def test_broadcaster_flip_flop_inverter_large_sequence(config, expected_low, expected_high):
    # Define the graph structure as a text representation
    # config = r"""
    # broadcaster -> a, b, c
    # %a -> b
    # %b -> c
    # %c -> inv
    # &inv -> a
    # """

    # Use the parse_input function to convert the text into a graph structure
    graph = puzzle.parse_input(config)

    memory = Memory()
    memory.initialize(graph)  # Initialize memory based on the graph

    # Push the button 1000 times
    total_low, total_high, state = puzzle.push_button_n_times(graph, memory, 1000, initial_pulse=False)

    # Assert the expected counts of low and high pulses
    assert total_low == expected_low  # Total low pulses should be 8000
    assert total_high == expected_high  # Total high pulses should be 4000



def test_solve_part_one(capsys):
    print('Solving Part One:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_one(input)
    print(f'Part One : {answer}')
    assert 821985143 == answer

# @pytest.mark.skip(reason="Not implemented")
def test_solve_part_two(capsys):
    print('Solving Part Two:')
    input = puzzle.read_input()
    answer = puzzle.solve_part_two(input)
    print(f'Part Two : {answer}')
    assert 240853834793347 == answer

