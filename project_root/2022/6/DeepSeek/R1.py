import sys

def part1(data):
    return find_marker(data, 4)

def part2(data):
    return find_marker(data, 14)

def find_marker(data, size):
    buffer = data[0]
    n = len(buffer)
    freq = {}
    distinct = 0

    for i in range(size):
        c = buffer[i]
        freq[c] = freq.get(c, 0) + 1
        if freq[c] == 1:
            distinct += 1
    if distinct == size:
        return size

    for i in range(size, n):
        c_old = buffer[i - size]
        freq[c_old] -= 1
        if freq[c_old] == 0:
            distinct -= 1
        
        c_new = buffer[i]
        freq[c_new] = freq.get(c_new, 0) + 1
        if freq[c_new] == 1:
            distinct += 1
        
        if distinct == size:
            return i + 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")