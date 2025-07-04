import sys

def find_path_r(current_path, found_paths, repeat):
    current_node = current_path[-1]
    if current_node == "end":
        found_paths.append(current_path)
        return
    for edge in edges:
        if edge[0] == current_node:
            if edge[1].isupper() or edge[1] not in current_path:
                find_path_r(current_path + [edge[1]], found_paths, repeat)
            elif edge[1].islower() and edge[1] in current_path and repeat:
                find_path_r(current_path + [edge[1]], found_paths, False)


def find_paths(repeat):
    """Find the all the paths from start to the end node"""
    found_paths = []
    find_path_r(["start"], found_paths, repeat)
    return found_paths

def part1():
    return len(find_paths(False))  # Part 1

def part2():
    return len(find_paths(True))  # Part 2

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

    lst = [line.split("-") for line in data]
    edges = [[a, b] for a, b in lst if a != "end" and b != "start"]
    edges += [[b, a] for a, b in lst if a != "start" and b != "end"]


sys.stdout.write(f"{part1()} {part2()}")