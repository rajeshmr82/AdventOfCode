from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
from collections import defaultdict, deque
import random
import math

def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

@dataclass
class Edge:
    start: str
    end: str
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
    
    def __hash__(self):
        return hash((self.start, self.end))

class OptimizedKarger:
    def __init__(self, input_text: str):
        """Initialize the graph from input text."""
        self.edges = []
        self.vertices = set()
        self._parse_input(input_text)
        
        # Calculate required iterations using probability theory
        n = len(self.vertices)
        self.max_iterations = int(math.log(n) * n * n)  # This gives good probability of success

    def _parse_input(self, input_text: str) -> None:
        """Parse input text into edges and vertices."""
        edges_seen = set()  # To avoid duplicate edges
        for line in input_text.strip().split('\n'):
            source, targets = line.strip().split(': ')
            source = source.strip()
            
            for target in targets.strip().split():
                # Ensure consistent edge ordering
                if source < target:
                    edge = Edge(source, target)
                else:
                    edge = Edge(target, source)
                    
                if edge not in edges_seen:
                    self.edges.append(edge)
                    edges_seen.add(edge)
                    self.vertices.add(source)
                    self.vertices.add(target)

    def _union_find_find(self, v: str, subsets: Dict[str, Tuple[str, int]]) -> str:
        """Find with path compression."""
        if v != subsets[v][0]:
            new_parent = self._union_find_find(subsets[v][0], subsets)
            subsets[v] = (new_parent, subsets[v][1])
        return subsets[v][0]

    def _union_find_union(self, v1: str, v2: str, subsets: Dict[str, Tuple[str, int]]) -> None:
        """Union by rank."""
        root1, root2 = self._union_find_find(v1, subsets), self._union_find_find(v2, subsets)
        if root1 == root2:
            return
            
        rank1, rank2 = subsets[root1][1], subsets[root2][1]
        if rank1 > rank2:
            subsets[root2] = (root1, rank2)
        elif rank1 < rank2:
            subsets[root1] = (root2, rank1)
        else:
            subsets[root2] = (root1, rank2)
            subsets[root1] = (root1, rank1 + 1)

    def _get_component_sizes(self, edges: List[Edge]) -> Tuple[int, int]:
        """Get sizes of components after removing edges."""
        # Build adjacency list
        adj_list = defaultdict(set)
        for edge in edges:
            adj_list[edge.start].add(edge.end)
            adj_list[edge.end].add(edge.start)
        
        # Use BFS to find component size
        start_vertex = next(iter(self.vertices))
        visited = {start_vertex}
        queue = deque([start_vertex])
        
        while queue:
            vertex = queue.popleft()
            for neighbor in adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        comp1_size = len(visited)
        comp2_size = len(self.vertices) - comp1_size
        return comp1_size, comp2_size

    def _try_cut(self, edges: List[Edge], excluded_edges: Set[Edge]) -> bool:
        """Try a specific cut and check if it creates exactly 2 components."""
        remaining_edges = [e for e in edges if e not in excluded_edges]
        comp1, comp2 = self._get_component_sizes(remaining_edges)
        return comp1 > 0 and comp2 > 0

    def _karger_iteration(self, edges: List[Edge], n_vertices: int, seed: int) -> Tuple[bool, List[Edge]]:
        """Perform one iteration of Karger's algorithm with a specific seed."""
        rng = random.Random(seed)
        edges = edges.copy()
        subsets = {v: (v, 0) for v in self.vertices}
        
        # Shuffle edges deterministically
        rng.shuffle(edges)
        edge_index = len(edges) - 1
        vertices_remaining = n_vertices
        
        while vertices_remaining > 2 and edge_index >= 0:
            edge = edges[edge_index]
            p1 = self._union_find_find(edge.start, subsets)
            p2 = self._union_find_find(edge.end, subsets)
            
            if p1 != p2:
                self._union_find_union(p1, p2, subsets)
                vertices_remaining -= 1
            edge_index -= 1
        
        # Find crossing edges
        cut_edges = []
        for edge in edges[:edge_index + 1]:
            p1 = self._union_find_find(edge.start, subsets)
            p2 = self._union_find_find(edge.end, subsets)
            if p1 != p2:
                cut_edges.append(edge)
        
        return len(cut_edges) == 3, cut_edges

    def find_min_cut(self) -> Tuple[List[Edge], int]:
        """Find the minimum cut using multiple iterations."""
        n_vertices = len(self.vertices)
        
        for iteration in range(self.max_iterations):
            found, cut_edges = self._karger_iteration(self.edges, n_vertices, iteration)
            
            if found and self._try_cut(self.edges, set(cut_edges)):
                # Remove cut edges and calculate component sizes
                remaining_edges = [e for e in self.edges if e not in cut_edges]
                comp1_size, comp2_size = self._get_component_sizes(remaining_edges)
                return cut_edges, comp1_size * comp2_size
        
        raise RuntimeError(f"No 3-cut found after {self.max_iterations} iterations")



def solve_part_one(input_text):
    solver = OptimizedKarger(input_text)
    wires, product = solver.find_min_cut()
    return product


def solve_part_two(input):      
    
    result = None
    return result