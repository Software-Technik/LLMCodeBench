import sys

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
            for i in range(length // 2):
                start = (pos + i) % 256
                end = (pos + length - 1 - i) % 256
                nums[start], nums[end] = nums[end], nums[start]
            pos = (pos + length + skip) % 256
            skip += 1

    dense = []
    for b in range(0, 256, 16):
        xor = nums[b]
        for i in range(1, 16):
            xor ^= nums[b + i]
        dense.append(xor)

    return ''.join(f"{x:08b}" if bin_out else f"{x:02x}" for x in dense)

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
        stack = [coord]
        while stack:
            x, y = stack.pop()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                neighbor = (x + dx, y + dy)
                if neighbor in maze:
                    maze.remove(neighbor)
                    stack.append(neighbor)

    regions = 0
    while maze:
        dfs(maze.pop())
        regions += 1
    return regions

# ------------------- Solutions --------------------

def part1(data):
    maze = create_maze(data[0])
    return len(maze)

def part2(data):
    maze = create_maze(data[0])
    return count_regions(maze)

# ------------------- Entrée / Sortie standard --------------------

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")