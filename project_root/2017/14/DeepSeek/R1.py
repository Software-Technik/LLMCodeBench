import sys

def knot_hash(lengths, bin_out=False):
    nums = list(range(256))
    pos = skip = 0
    for _ in range(64):
        for length in lengths:
            for i in range(length // 2):
                left = (pos + i) % 256
                right = (pos + length - 1 - i) % 256
                nums[left], nums[right] = nums[right], nums[left]
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

def create_maze(instructions):
    base_string = instructions + '-'
    base_lengths = [ord(c) for c in base_string]
    fixed_suffix = [17, 31, 73, 47, 23]
    maze = set()
    for row in range(128):
        row_str = str(row)
        row_lengths = [ord(c) for c in row_str]
        total_lengths = base_lengths + row_lengths + fixed_suffix
        bin_hash = knot_hash(total_lengths, bin_out=True)
        for col, bit in enumerate(bin_hash):
            if bit == '1':
                maze.add((row, col))
    return maze

def count_regions(maze):
    regions = 0
    neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
    while maze:
        coord = next(iter(maze))
        stack = [coord]
        maze.remove(coord)
        while stack:
            x, y = stack.pop()
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                if neighbor in maze:
                    maze.remove(neighbor)
                    stack.append(neighbor)
        regions += 1
    return regions

def part1(maze_set):
    return len(maze_set)

def part2(maze_set):
    return count_regions(maze_set.copy())

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

instructions = data[0]
maze_set = create_maze(instructions)
sys.stdout.write(f"{part1(maze_set)}\n{part2(maze_set)}\n")