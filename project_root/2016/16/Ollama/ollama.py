import sys

DISK_1 = 272
DISK_2 = 35651584

def fill_disk(data, disk_size):
    while len(data) < disk_size:
        new = [1 - i for i in reversed(data)]
        data.extend([0] + new)
    return data[:disk_size]

def create_checksum(data):
    while len(data) % 2 == 0:
        zipped = zip(*[iter(data)] * 2)
        data = [a == b for a, b in zipped]
    return ''.join(map(str, map(int, data)))

def part1(data):
    d = fill_disk(list(map(int, data)), DISK_1)
    while len(d) % 2 == 0:
        zipped = zip(*[iter(d)] * 2)
        d = [a == b for a, b in zipped]
    return ''.join(map(str, map(int, d)))

def part2(data):
    d = fill_disk(list(map(int, data)), DISK_2)
    while len(d) % 2 == 0:
        zipped = zip(*[iter(d)] * 2)
        d = [a == b for a, b in zipped]
    return ''.join(map(str, map(int, d)))

input_file = sys.argv[1]
with open(input_file, 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")