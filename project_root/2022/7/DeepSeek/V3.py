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
    dirs, sub_dirs = parse_commands(data)
    dirs_size = defaultdict(int)
    visited = set()

    for k in sorted(dirs.keys(), key=lambda x: -len(x.split('/'))):
        dirs_size[k] = dirs[k]
        if k in sub_dirs:
            for sub in sub_dirs[k]:
                dirs_size[k] += dirs_size[sub]
    return dirs_size

def parse_commands(data):
    dirs = defaultdict(int)
    sub_dirs = defaultdict(list)
    working_dir = []

    idx = 0
    while idx < len(data):
        line = data[idx]
        if line.startswith("$ cd"):
            dir_name = line[5:]
            if dir_name == "..":
                working_dir.pop()
            else:
                working_dir.append(dir_name)
            idx += 1
        elif line.startswith("$ ls"):
            idx += 1
            while idx < len(data) and data[idx][0] != "$":
                type_or_size, name = data[idx].split()
                curr_dir = "/".join(working_dir)
                if type_or_size == "dir":
                    path = f"{curr_dir}/{name}" if curr_dir != "/" else f"/{name}"
                    sub_dirs[curr_dir].append(path)
                else:
                    dirs[curr_dir] += int(type_or_size)
                idx += 1
    return dirs, sub_dirs

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")