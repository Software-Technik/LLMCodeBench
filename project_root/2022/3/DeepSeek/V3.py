import sys

def part1(data):
    priorities = 0
    for line in data:
        half = len(line) // 2
        common = set(line[:half]).intersection(line[half:]).pop()
        priorities += ord(common) - (96 if common.islower() else 38)
    return priorities

def part2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        common = set(data[i]).intersection(data[i+1], data[i+2]).pop()
        priorities += ord(common) - (96 if common.islower() else 38)
    return priorities

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")