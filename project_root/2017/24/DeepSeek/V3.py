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
    connections_count = len(connections)
    visited = [False] * connections_count

    def dfs(path, current_node, current_score, current_length):
        nonlocal max_score, longest_strongest
        max_score = max(max_score, current_score)
        if current_length > longest_strongest[0]:
            longest_strongest = (current_length, current_score)
        elif current_length == longest_strongest[0]:
            if current_score > longest_strongest[1]:
                longest_strongest = (current_length, current_score)
        
        for i in range(connections_count):
            if not visited[i]:
                a, b = connections[i]
                if a == current_node or b == current_node:
                    visited[i] = True
                    next_node = b if a == current_node else a
                    new_score = current_score + a + b
                    new_length = current_length + 1
                    dfs(path + [next_node], next_node, new_score, new_length)
                    visited[i] = False

    dfs([], 0, 0, 0)
    
    doubles_set = set(doubles)
    for num in doubles_set:
        count = doubles.count(num)
        for _ in range(count):
            max_score += num
            if longest_strongest[0] == 0:
                longest_strongest = (1, num)
            else:
                longest_strongest = (longest_strongest[0] + 1, longest_strongest[1] + num)
    
    return max_score, longest_strongest[1]

input_file = sys.argv[1]
connections, doubles = parse_input(input_file)
part1, part2 = solve(connections, doubles)

print(part1)
print(part2)