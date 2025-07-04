import sys
from hashlib import md5

# ------------------- Knot Hash --------------------

def knot_hash(input_str, bin_out=False):
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]
    nums = list(range(256))
    pos = skip = 0

    for _ in range(64):
        for length in lengths:
            if length > len(nums):
                continue
            # reverse section
            section = [nums[(pos + i) % 256] for i in range(length)]
            for i in range(length):
                nums[(pos + i) % 256] = section[-(i + 1)]
            pos = (pos + length + skip) % 256
            skip += 1

    dense = []
    for b in range(0, 256, 16):
        xor = 0
        for i in range(16):
            xor ^= nums[b + i]
        dense.append(xor)

    if bin_out:
        return ''.join(f"{x:08b}" for x in dense)
    else:
        return ''.join(f"{x:02x}" for x in dense)

# ------------------- Maze + DFS --------------------

def create_maze(instructions):
    maze = set()
    for row in range(128):
        key = f"{instructions}-{row}"
        bin_hash = knot_hash(key, bin_out=True)
        for i, bit in enumerate(bin_hash):
            if bit == '1':
                maze.add((row, i))
    return maze

def count_regions(maze):
    def dfs(coord):
        x, y = coord
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in maze:
                maze.remove(neighbor)
                dfs(neighbor)

    regions = 0
    while maze:
        coord = maze.pop()
        dfs(coord)
        regions += 1
    return regions

# ------------------- Solutions --------------------

def part1(data):
    instructions = data[0]
    maze = create_maze(instructions)
    return len(maze)

def part2(data):
    instructions = data[0]
    maze = create_maze(instructions)
    return count_regions(maze)

# ------------------- Entrée / Sortie standard --------------------

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")