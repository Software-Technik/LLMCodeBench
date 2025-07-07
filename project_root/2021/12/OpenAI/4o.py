import sys

def find_path_r(current_path, found_paths, repeat):
    current_node = current_path[-1]
    if current_node == "end":
        found_paths.append(1)
        return
    for edge in adjacency_list[current_node]:
        if edge.isupper() or edge not in current_path:
            find_path_r(current_path + [edge], found_paths, repeat)
        elif edge.islower() and repeat:
            find_path_r(current_path + [edge], found_paths, False)

def find_paths(repeat):
    found_paths = []
    find_path_r(["start"], found_paths, repeat)
    return found_paths

def part1():
    return len(find_paths(False))

def part2():
    return len(find_paths(True))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

    adjacency_list = {}
    for a, b in [line.split("-") for line in data]:
        if a != "end" and b != "start":
            adjacency_list.setdefault(a, []).append(b)
        if b != "end" and a != "start":
            adjacency_list.setdefault(b, []).append(a)

sys.stdout.write(f"{part1()} {part2()}")