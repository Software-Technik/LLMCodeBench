To solve this problem, we need to build the strongest possible bridge of components by connecting components with matching port numbers. The strength of the bridge is the sum of the port numbers of all components used. The solution involves exploring all possible bridges starting from port 0 using a depth-first search (DFS) approach to maximize the strength and length of the bridge.

### Approach
1. **Input Parsing**: The input file is parsed to extract the components. Each component is split into two port numbers. Non-double components (where the two ports are different) are stored in a list of connections, while double components (where both ports are the same) are stored separately.
2. **Graph Construction**: A graph is constructed where each node represents a port, and edges represent the components. Each edge is annotated with its index for tracking visited edges during DFS.
3. **DFS with State Tracking**: The DFS starts at port 0. For each node, it explores all unvisited edges connected to that node. The state during DFS includes:
   - **Current Node**: The current port being extended.
   - **Depth**: The number of components used so far.
   - **Base Score**: The sum of the port numbers of all components used.
   - **Doubles Seen**: A set of double port numbers encountered in the path.
4. **Score Calculation**: At each state, the total score is computed by adding the base score and a bonus (twice the value of each distinct double port encountered). The total length is the depth plus the number of distinct doubles seen.
5. **Global Best Tracking**: During DFS, the maximum score and the strongest bridge of the longest length are tracked and updated whenever a better solution is found.

### Solution Code

import sys

def parse_input(filepath):
    with open(filepath) as f:
        lines = [line.strip() for line in f if line.strip()]
    connections = []
    doubles = []
    for line in lines:
        a, b = map(int, line.split("/"))
        if a != b:
            connections.append((a, b))
        else:
            doubles.append(a)
    return connections, doubles

def solve(connections, doubles):
    max_score = 0
    longest_strongest = (0, 0)
    
    graph = {}
    for i, (a, b) in enumerate(connections):
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, i))
        graph[b].append((a, i))
    
    doubles_set = set(doubles)
    visited_edges = set()

    def dfs(current, depth, base, doubles_seen):
        nonlocal max_score, longest_strongest
        
        bonus = 0
        for n in doubles_seen:
            bonus += 2 * n
        total_score = base + bonus
        total_length = depth + len(doubles_seen)
        
        if total_score > max_score:
            max_score = total_score
        if (total_length, total_score) > longest_strongest:
            longest_strongest = (total_length, total_score)
        
        if current in graph:
            for neighbor, edge_index in graph[current]:
                if edge_index in visited_edges:
                    continue
                visited_edges.add(edge_index)
                new_base = base + current + neighbor
                if neighbor in doubles_set and neighbor not in doubles_seen:
                    new_doubles_seen = doubles_seen | {neighbor}
                else:
                    new_doubles_seen = doubles_seen
                dfs(neighbor, depth + 1, new_base, new_doubles_seen)
                visited_edges.remove(edge_index)
    
    dfs(0, 0, 0, set())
    return max_score, longest_strongest[1]

if __name__ == "__main__":
    input_file = sys.argv[1]
    connections, doubles = parse_input(input_file)
    part1, part2 = solve(connections, doubles)
    print(part1)
    print(part2)


### Explanation
1. **Input Parsing**: The input file is read and parsed into connections (non-double components) and doubles (components with identical ports).
2. **Graph Construction**: The graph is built using adjacency lists where each node (port) points to its connected neighbors along with the component index.
3. **DFS Initialization**: The DFS starts at port 0 with initial state (depth 0, base score 0, and an empty set of doubles seen).
4. **State Exploration**: For each node, the algorithm explores all unvisited edges. For each edge, it updates the base score (sum of current and neighbor ports) and checks if the neighbor port is a double not yet seen.
5. **Score and Length Calculation**: At each state, the total score is computed by adding the base score and the bonus (twice each distinct double port encountered). The total length is the sum of the depth and the count of distinct doubles seen.
6. **Global Updates**: The maximum score and the strongest longest bridge are updated whenever a better solution is found during the DFS traversal.
7. **Output**: After DFS completes, the maximum score (part1) and the strongest longest bridge score (part2) are printed.

This approach efficiently explores all possible bridges using DFS with state tracking, optimizing both runtime and memory usage by leveraging adjacency lists and careful state management.