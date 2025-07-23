import sys

priority_map = {}
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for idx, char in enumerate(letters, 1):
    priority_map[char] = idx

def part1(data):
    priorities = 0
    for line in data:
        half = len(line) // 2
        seen = set(line[:half])
        for c in line[half:]:
            if c in seen:
                priorities += priority_map[c]
                break
    return priorities

def part2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        set1 = set(data[i])
        set2 = set(data[i+1])
        common12 = set1 & set2
        for c in data[i+2]:
            if c in common12:
                priorities += priority_map[c]
                break
    return priorities

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")