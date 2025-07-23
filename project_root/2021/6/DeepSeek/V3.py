import sys
from collections import defaultdict

def part1(data):
    fish = list(map(int, data.split(',')))
    for _ in range(80):
        new_fish = []
        spawn = 0
        for f in fish:
            if f == 0:
                spawn += 1
                new_fish.append(6)
            else:
                new_fish.append(f - 1)
        fish = new_fish + [8] * spawn
    return len(fish)

def part2(data):
    counts = defaultdict(int)
    for num in map(int, data.split(',')):
        counts[num] += 1
    for day in range(256):
        new_counts = defaultdict(int)
        for timer, count in counts.items():
            if timer == 0:
                new_counts[6] += count
                new_counts[8] += count
            else:
                new_counts[timer - 1] += count
        counts = new_counts
    return sum(counts.values())

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")