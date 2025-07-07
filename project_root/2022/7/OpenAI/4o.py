import sys
from collections import defaultdict, deque

def part1(data):
    dirs_size = calc_dir_size(data)
    return sum(v for v in dirs_size.values() if v <= 100000)

def part2(data):
    dirs_size = calc_dir_size(data)
    unused = 70000000 - dirs_size["/"]
    require = 30000000 - unused
    return min(v for v in dirs_size.values() if v >= require)

def calc_dir_size(data):
    dirs, sub_dirs = parse_commands(data)
    dirs_size = defaultdict(int)

    for k, v in dirs.items():
        dirs_size[k] += v
        queue = deque([k])
        while queue:
            dir = queue.popleft()
            if dir in sub_dirs:
                for h in sub_dirs[dir]:
                    dirs_size[k] += dirs[h]
                    queue.append(h)
    return dirs_size

def parse_commands(data):
    idx = 0
    dirs = {"/": 0}
    sub_dirs = defaultdict(list)
    working_dir = []

    while idx < len(data):
        command = data[idx]
        if command.startswith("$ cd"):
            dir_name = command[5:]
            if dir_name == "..":
                working_dir.pop()
            else:
                working_dir.append(dir_name)
            idx += 1

        elif command.startswith("$ ls"):
            idx += 1
            while idx < len(data) and not data[idx].startswith("$"):
                type_or_size, dir_name = data[idx].split()
                curr_dir = "/".join(working_dir)
                if type_or_size == "dir":
                    path = f"{curr_dir}/{dir_name}"
                    dirs[path] = 0
                    sub_dirs[curr_dir].append(path)
                else:
                    dirs[curr_dir] += int(type_or_size)
                idx += 1

    return dirs, sub_dirs

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")