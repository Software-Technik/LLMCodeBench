import sys
from collections import defaultdict

def find_paths(repeat):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    found_paths = []
    stack = [(['start'], repeat)]
    
    while stack:
        current_path, can_repeat = stack.pop()
        current_node = current_path[-1]
        
        if current_node == 'end':
            found_paths.append(current_path)
            continue
        
        for neighbor in graph[current_node]:
            if neighbor.isupper():
                stack.append((current_path + [neighbor], can_repeat))
            else:
                if neighbor not in current_path:
                    stack.append((current_path + [neighbor], can_repeat))
                elif can_repeat and neighbor != 'start':
                    stack.append((current_path + [neighbor], False))
    
    return found_paths

def part1():
    return len(find_paths(False))

def part2():
    return len(find_paths(True))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]
    lst = [line.split("-") for line in data]
    edges = [[a, b] for a, b in lst if a != "end" and b != "start"]
    edges += [[b, a] for a, b in lst if a != "start" and b != "end"]

sys.stdout.write(f"{part1()} {part2()}")