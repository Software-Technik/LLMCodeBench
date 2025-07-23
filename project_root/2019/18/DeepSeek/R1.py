To solve this problem, we need to find the shortest path to collect all keys in a maze while navigating through doors that require corresponding keys to open. The maze is represented as a grid where walls are marked by `#`, open passages by `.`, keys by lowercase letters, doors by uppercase letters, and the starting position by `@`. 

### Approach
1. **Problem Analysis**:
   - **Part 1**: The robot starts at `@` and must collect all keys. Each door (uppercase letter) requires the corresponding key (lowercase letter) to pass through. The goal is to find the minimal number of steps to collect all keys.
   - **Part 2**: The maze is divided into four quadrants, each with its own robot. The robots must collectively collect all keys, with each robot confined to its quadrant.

2. **Key Insights**:
   - **Graph Representation**: Convert the maze into a graph where nodes are important positions (start, keys, doors) and edges represent traversable paths with weights indicating the number of steps.
   - **State Representation**: Use a state tuple `(mask, current)` where `mask` is a bitmask representing collected keys and `current` is the current position (or positions for Part 2). This helps in efficiently tracking progress and minimizing redundant calculations.
   - **Precomputation**: Precompute distances and required doors between all pairs of important nodes to avoid repeated Dijkstra calls during state exploration.
   - **Priority Queue (Dijkstra)**: Explore states in order of increasing cost to ensure the first time all keys are collected is with the minimal cost.

3. **Optimization**:
   - **Graph Condensation**: Simplify the graph by removing dead ends and condensing linear paths to reduce the number of nodes.
   - **State Space Pruning**: Use a priority queue to explore states with minimal cost first, ensuring optimal paths are found early.
   - **Bitmask for Keys**: Represent collected keys as a bitmask to efficiently check door requirements and update state.

### Solution Code

import sys
import networkx as nx
from collections import defaultdict
import heapq

def createLevelFrom(data):
    x, y = 0, 0
    level = dict()
    for line in data:
        for c in line:
            if c == "@": position = (x,y)
            level[(x,y)] = '.' if c == "@" else c
            x += 1
        x = 0
        y += 1
    return level, position

def createLevelFrom2(data):
    x, y = 0, 0
    level = dict()
    for line in data:
        for c in line:
            if c == "@": position = (x,y)
            level[(x,y)] = '.' if c == "@" else c
            x += 1
        x = 0
        y += 1

    level[position] = "#"
    level[(position[0] - 1, position[1] + 0)] = "#"
    level[(position[0] + 1, position[1] + 0)] = "#"
    level[(position[0] + 0, position[1] + 1)] = "#"
    level[(position[0] + 0, position[1] - 1)] = "#"

    positions = (
        (position[0] - 1, position[1] - 1),
        (position[0] - 1, position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 1, position[1] + 1),
    )
    return level, positions

def neighbors(level, p):
    return [x for x in [
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1]),
        (p[0], p[1] + 1),
        (p[0], p[1] - 1),
    ] if x in level and level[x] != "#"]

def createGameFrom(level, position):
    spaces = set()
    keys = dict()
    doors = dict()
    curgraph = nx.Graph()

    for p in level:
        if level[p] == "#": continue
        if level[p] == ".": spaces.add(p)
        if level[p].isupper(): doors[level[p].lower()] = p
        if level[p].islower(): keys[level[p]] = p
        curgraph.add_node(p)
    
    for p in level:
        for n in neighbors(level, p):
            if n in curgraph.nodes() and p in curgraph.nodes():
                curgraph.add_edge(p, n, weight=1)

    keepgoing = True
    while keepgoing:
        keepgoing = False
        leaves = [
            x for x in curgraph.nodes()
            if x != position and len(list(curgraph.neighbors(x))) == 1
        ]
        for leaf in leaves:
            if level[leaf] == "." or level[leaf].isupper():
                keepgoing = True
                curgraph.remove_node(leaf)
                if level[leaf] == ".": 
                    spaces.remove(leaf) 
                else: 
                    del doors[level[leaf].lower()]

    keepgoing = True
    while keepgoing:
        keepgoing = False
        potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
        for pot in potentials:
            others = list(curgraph.neighbors(pot))
            if pot in spaces and len(others) == 2 and pot != position:
                weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
                curgraph.remove_node(pot)
                spaces.remove(pot)
                curgraph.add_edge(others[0], others[1], weight=weight)

    return curgraph, spaces, doors, keys

def createGameFrom2(level, positions):
    spaces = set()
    keys = dict()
    doors = dict()
    curgraph = nx.Graph()

    for p in level:
        if level[p] == "#": continue
        if level[p] == ".": spaces.add(p)
        if level[p].isupper(): doors[level[p].lower()] = p
        if level[p].islower(): keys[level[p]] = p
        curgraph.add_node(p)
    
    for p in level:
        for n in neighbors(level, p):
            if n in curgraph.nodes() and p in curgraph.nodes():
                curgraph.add_edge(p, n, weight=1)

    keepgoing = True
    while keepgoing:
        keepgoing = False
        leaves = [
            x for x in curgraph.nodes()
            if x not in positions and len(list(curgraph.neighbors(x))) == 1
        ]
        for leaf in leaves:
            if level[leaf] == "." or level[leaf].isupper():
                keepgoing = True
                curgraph.remove_node(leaf)
                if level[leaf] == ".": 
                    spaces.remove(leaf) 
                else: 
                    del doors[level[leaf].lower()]

    keepgoing = True
    while keepgoing:
        keepgoing = False
        potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
        for pot in potentials:
            others = list(curgraph.neighbors(pot))
            if pot in spaces and len(others) == 2 and pot not in positions:
                weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
                curgraph.remove_node(pot)
                spaces.remove(pot)
                curgraph.add_edge(others[0], others[1], weight=weight)

    return curgraph, spaces, doors, keys

def part1(data):
    level, position = createLevelFrom(data)
    curgraph, spaces, doors, keys = createGameFrom(level, position)
    
    important_nodes = {'@': position}
    for k, pos in keys.items():
        important_nodes[k] = pos
        
    dist = {}
    door_sets = {}
    for n1 in important_nodes:
        for n2 in important_nodes:
            if n1 == n2:
                continue
            if (n1, n2) in dist:
                continue
            try:
                path = nx.shortest_path(curgraph, source=important_nodes[n1], target=important_nodes[n2], weight='weight')
            except:
                continue
            total_weight = 0
            for i in range(len(path)-1):
                total_weight += curgraph.edges[path[i], path[i+1]]['weight']
            dist[(n1, n2)] = total_weight
            dist[(n2, n1)] = total_weight
            doors_on_path = set()
            for p in path[1:-1]:
                c = level[p]
                if c.isupper():
                    doors_on_path.add(c.lower())
            door_sets[(n1, n2)] = doors_on_path
            door_sets[(n2, n1)] = doors_on_path

    all_keys = set(keys.keys())
    n_keys = len(all_keys)
    key_to_index = {k: i for i, k in enumerate(sorted(all_keys))}
    full_mask = (1 << n_keys) - 1

    best = defaultdict(lambda: float('inf'))
    heap = []
    start_state = ('@', 0)
    best[start_state] = 0
    heapq.heappush(heap, (0, start_state))

    while heap:
        cost, state = heapq.heappop(heap)
        current, mask = state
        if mask == full_mask:
            return cost
        if cost > best[state]:
            continue
        for next_key in all_keys:
            if mask & (1 << key_to_index[next_key]):
                continue
            if next_key == current:
                continue
            if (current, next_key) in door_sets:
                if door_sets[(current, next_key)].issubset(set( k for k in all_keys if mask & (1 << key_to_index[k]) )):
                    new_cost = cost + dist[(current, next_key)]
                    new_mask = mask | (1 << key_to_index[next_key])
                    new_state = (next_key, new_mask)
                    if new_cost < best[new_state]:
                        best[new_state] = new_cost
                        heapq.heappush(heap, (new_cost, new_state))
    return None

def part2(data):
    level, positions = createLevelFrom2(data)
    curgraph, spaces, doors, keys = createGameFrom2(level, positions)
    
    minx = min(x for x, y in positions)
    miny = min(y for x, y in positions)
    maxx = max(x for x, y in positions)
    maxy = max(y for x, y in positions)
    midx = minx + 1
    midy = miny + 1

    important_nodes_by_area = [dict() for _ in range(4)]
    for i, pos in enumerate(positions):
        start_label = f"@{i}"
        important_nodes_by_area[i][start_label] = pos

    for k, pos in keys.items():
        x, y = pos
        if x < midx and y < midy:
            area = 0
        elif x < midx and y > midy:
            area = 1
        elif x > midx and y < midy:
            area = 2
        elif x > midx and y > midy:
            area = 3
        else:
            continue
        important_nodes_by_area[area][k] = pos

    dist_by_area = [dict() for _ in range(4)]
    door_sets_by_area = [dict() for _ in range(4)]
    
    for area in range(4):
        nodes = important_nodes_by_area[area]
        for n1 in nodes:
            for n2 in nodes:
                if n1 == n2:
                    continue
                if (n1, n2) in dist_by_area[area]:
                    continue
                try:
                    path = nx.shortest_path(curgraph, source=nodes[n1], target=nodes[n2], weight='weight')
                except:
                    continue
                total_weight = 0
                for i in range(len(path)-1):
                    total_weight += curgraph.edges[path[i], path[i+1]]['weight']
                dist_by_area[area][(n1, n2)] = total_weight
                dist_by_area[area][(n2, n1)] = total_weight
                doors_on_path = set()
                for p in path[1:-1]:
                    c = level[p]
                    if c.isupper():
                        doors_on_path.add(c.lower())
                door_sets_by_area[area][(n1, n2)] = doors_on_path
                door_sets_by_area[area][(n2, n1)] = doors_on_path

    all_keys = set(keys.keys())
    n_keys = len(all_keys)
    key_to_index = {k: i for i, k in enumerate(sorted(all_keys))}
    full_mask = (1 << n_keys) - 1

    best = defaultdict(lambda: float('inf'))
    heap = []
    start_positions = (f"@{0}", f"@{1}", f"@{2}", f"@{3}")
    start_state = (0, start_positions)
    best[start_state] = 0
    heapq.heappush(heap, (0, start_state))

    while heap:
        cost, state = heapq.heappop(heap)
        mask, positions = state
        if mask == full_mask:
            return cost
        if cost > best[state]:
            continue
        for robot in range(4):
            current = positions[robot]
            area_nodes = important_nodes_by_area[robot]
            for next_key in area_nodes:
                if next_key.startswith('@'):
                    continue
                if mask & (1 << key_to_index[next_key]):
                    continue
                if (current, next_key) not in dist_by_area[robot]:
                    continue
                door_set = door_sets_by_area[robot].get((current, next_key), set())
                has_doors = True
                for d in door_set:
                    if not (mask & (1 << key_to_index[d])):
                        has_doors = False
                        break
                if not has_doors:
                    continue
                new_cost = cost + dist_by_area[robot][(current, next_key)]
                new_mask = mask | (1 << key_to_index[next_key])
                new_positions = list(positions)
                new_positions[robot] = next_key
                new_positions = tuple(new_positions)
                new_state = (new_mask, new_positions)
                if new_cost < best[new_state]:
                    best[new_state] = new_cost
                    heapq.heappush(heap, (new_cost, new_state))
    return None

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

result1 = part1(data.copy())
result2 = part2(data)
print(f"{result1} {result2}")


### Explanation
1. **Graph Construction**:
   - The maze is converted into a graph where nodes represent positions (start, keys, doors) and edges represent traversable paths. Dead ends and linear paths are condensed to simplify the graph.

2. **Precomputation**:
   - For each important node (start and keys), distances and required doors between every pair are precomputed. This avoids repeated Dijkstra calls during state exploration.

3. **State Exploration**:
   - **Part 1**: Uses a priority queue to explore states `(current_position, collected_keys_mask)`. The minimal cost to collect all keys is found by moving to reachable keys (doors satisfied by collected keys).
   - **Part 2**: Extends the state to `(collected_keys_mask, (robot1_position, robot2_position, robot3_position, robot4_position))`. Each robot moves within its quadrant to collect keys, updating the state similarly.

4. **Efficiency**:
   - Precomputation reduces the overhead of pathfinding during state exploration.
   - Bitmask representation of collected keys allows efficient state updates and checks.
   - Priority queue ensures minimal cost paths are explored first, leading to optimal solutions.