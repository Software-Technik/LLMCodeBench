import sys
from collections import defaultdict

data = [line.strip() for line in open(sys.argv[1])]

dirs_size = defaultdict(int)
working_dir = ['']

for line in data:
    if line.startswith('$'):
        parts = line.split()
        if parts[1] == 'cd':
            if parts[2] == '/':
                working_dir = ['']
            elif parts[2] == '..':
                working_dir.pop()
            else:
                working_dir.append(parts[2])
    else:
        a, b = line.split()
        if a != 'dir':
            size = int(a)
            for i in range(1, len(working_dir) + 1):
                path = '/'.join(working_dir[:i])
                dirs_size[path] += size

sizes = dirs_size.values()
part1 = sum(v for v in sizes if v <= 100000)
total = dirs_size['']
unused = 70000000 - total
need = 30000000 - unused
part2 = min(v for v in sizes if v >= need)

sys.stdout.write(f"{part1}\n{part2}\n")