import sys

def part1(data):
        return sum(1 if i == "(" else -1 for i in data[0])

def part2(data):
    insts = [1 if i == "(" else -1 for i in data[0]]
    for i in range(1, len(insts) + 1):
        if sum(insts[:i]) == -1:
            return i

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")