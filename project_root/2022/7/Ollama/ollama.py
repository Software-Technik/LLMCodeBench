import sys
from collections import defaultdict

def part1(data):
    dir_sizes, _ = compute_dir_data(data)
    return sum(v for v in dir_sizes.values() if v <= 100000)

def part2(data):
    dir_sizes, total_used = compute_dir_data(data)
    space_needed = max(30000000 - (70000000 - total_used), 0)
    return min(v for v in dir_sizes.values() if v >= space_needed)

def compute_dir_data(data):
    _, dir_sizes, current_path, stack = initialize_state()
    for line in data:
        update_state(line, dir_sizes, current_path, stack)
    total_used = sum(dir_sizes[t] for t in dir_sizes if '/' == t.rsplit('/', 1)[0])
    dir_sizes['/'] = total_used
    return dir_sizes, total_used

def initialize_state():
    dirs = {'/': defaultdict(int)}
    size_map = defaultdict(int)
    path_stack = ['']
    current_dir = '/'
    return dirs, size_map, current_dir, path_stack

def update_state(line, sizes, curr_path, stack):
    if line.startswith('$ cd'):
        _, _, name = line.split()
        if name == '..':
            stack.pop()
        else:
            stack.append(name)
        curr_path = '/'.join(stack.strip('/'))
        if curr_path not in sizes:
            sizes[curr_path] = defaultdict(int)
        return
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir'):
        _, name = line.split()
        path = f"{curr_path}/{name}"
        sizes[curr_path][name] = 0
    else:
        size, _ = line.split()
        sizes[curr_path]['.'] += int(size)

def extract_and_trim_input(input_filename):
    with open(input_filename) as f:
        return [line.strip() for line in f]

input_file = sys.argv[1]
data = extract_and_trim_input(input_file)
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")