import sys

DISK_1 = 272
DISK_2 = 35651584

def fill_disk(data, disk_size):
    while len(data) < disk_size:
        data = data + [0] + [1 - i for i in reversed(data)]
    return data[:disk_size]

def create_checksum(data):
    while len(data) % 2 == 0:
        data = [data[i] == data[i+1] for i in range(0, len(data), 2)]
    return ''.join(map(str, map(int, data)))

def solve(data, size):
    d = fill_disk(list(map(int, data)), size)
    return create_checksum(d)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{solve(data, DISK_1)} {solve(data, DISK_2)}")