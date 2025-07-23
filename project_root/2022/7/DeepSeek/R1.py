import sys
from collections import defaultdict

def part1(data):
    dirs_size = calc_dir_size(data)
    return sum(v for v in dirs_size.values() if v <= 100000)

def part2(data):
    dirs_size = calc_dir_size(data)
    unused = 70000000 - dirs_size["/"]
    require = 30000000 - unused
    return min(v for v in dirs_size.values() if v >= require)

def calc_dir_size(data):
    base_sizes, children = parse_commands(data)
    total_sizes = base_sizes.copy()
    stack = ['/']
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        if node in children:
            for child in reversed(children[node]):
                stack.append(child)
    order.reverse()
    for node in order:
        if node in children:
            for child in children[node]:
                total_sizes[node] += total_sizes[child]
    return total_sizes

def parse_commands(data):
    idx = 0
    dirs = {"/": 0}
    sub_dirs = defaultdict(list)
    working_dir = []

    while idx < len(data):
        match data[idx][:4]:
            case "$ cd":
                dir_name = data[idx][5:]
                match dir_name:
                    case "..":
                        working_dir.pop()
                    case _:
                        working_dir.append(dir_name)
                idx += 1
            case "$ ls":
                idx += 1
                while idx < len(data) and data[idx][0] != "$":
                    type_or_size, dir_name = data[idx].split()
                    curr_dir = "/".join(working_dir)
                    match type_or_size:
                        case "dir":
                            path = f"{curr_dir}/{dir_name}"
                            dirs[path] = 0
                            sub_dirs[curr_dir].append(path)
                        case _:
                            dirs[curr_dir] += int(type_or_size)
                    idx += 1
    return dirs, sub_dirs

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")