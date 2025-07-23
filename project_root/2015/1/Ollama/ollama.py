import sys

def part1(data):
    count = 0
    for char in data[0]:
        if char == "(": count += 1
        else: count -= 1
    return count

def part2(data):
    insts = [1 if i == "(" else -1 for i in data[0]]
    count = 0
    for i, change in enumerate(insts):
        count += change
        if count < 0:
            return i + 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")