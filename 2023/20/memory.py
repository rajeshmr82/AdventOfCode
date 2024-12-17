class Memory:
    def __init__(self):
        self.state = {}

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key, None)

    def initialize(self, graph):
        # Temporary storage for conjunction inputs
        temp_conjs = {node: [] for node in graph if graph[node][0] == '&'}  # Only include conjunctions

        # First pass to initialize flip-flops and gather inputs for conjunctions
        for node in graph:
            if graph[node][0] == '%':  # Flip-flop
                self.set(node, False)  # Initialize flip-flops to off
            elif graph[node][0] == '&':  # Conjunction
                # Gather inputs for the conjunction
                for source, dests in graph.items():  # Iterate over all nodes in the graph
                    if node in dests[1]:  # Check if the current node is a destination for any source
                        temp_conjs[node].append(source)  # Store the source node as an input

        # Second pass to set conjunction states in memory
        for node, inputs in temp_conjs.items():
            for input_node in inputs:
                self.set(f"{node}_{input_node}", False)  # Initialize inputs to off with a unique key

    def initialize_conjunction_states(self, graph):
        # Create a mapping for conjunction inputs
        conjs = {node: {} for node in graph if graph[node][0] == '&'}  # Only include conjunctions

        # Populate the conjunctions dictionary
        for source, dests in graph.items():
            for dest in dests[1]:  # Get the destinations from the graph
                if dest in conjs:
                    conjs[dest][source] = False  # Initialize input memory to False

        return conjs

    def get_conjunction_memory_states(self, graph, conjunction_node):
        # Temporary storage for inputs to the conjunction
        inputs = []

        # Gather inputs for the conjunction
        for source, dests in graph.items():
            if conjunction_node in dests[1]:  # Check if the conjunction is a destination
                inputs.append(source)  # Store the source node as an input

        # Retrieve memory states for each input
        memory_states = {input_node: self.get(input_node) for input_node in inputs}
        return memory_states

    def copy(self):
        # Return a copy of the current memory state
        new_memory = Memory()
        new_memory.state = self.state.copy()  # Create a shallow copy of the state
        return new_memory

    def set_state(self, new_state):
        # Set the memory state to a new state
        self.state = new_state.copy()  # Assuming new_state is a dictionary