import sys

DISK_1 = 272
DISK_2 = 35651584

def fill_disk(data, disk_size):
    data = list(map(int, data))
    while len(data) < disk_size:
        data += [0] + [1 - b for b in reversed(data)]
    return data[:disk_size]

def compute_checksum(data):
    while len(data) % 2 == 0:
        data = [a == b for a, b in zip(data[::2], data[1::2])]
    return ''.join(map(str, map(int, data)))

def part1(data):
    d = fill_disk(data, DISK_1)
    return compute_checksum(d)

def part2(data):
    d = fill_disk(data, DISK_2)
    return compute_checksum(d)

with open(sys.argv[1], 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")