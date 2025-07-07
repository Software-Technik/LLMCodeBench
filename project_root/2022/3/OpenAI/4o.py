import sys

def part1(data):
    priorities = 0
    for line in data:
        _sep = len(line) // 2
        badge = (set(line[:_sep]) & set(line[_sep:])).pop()
        priorities += ord(badge) - (96 if badge.islower() else 38)
    return priorities

def part2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        badge = (set(data[i]) & set(data[i+1]) & set(data[i+2])).pop()
        priorities += ord(badge) - (96 if badge.islower() else 38)
    return priorities

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")