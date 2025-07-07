import sys
from collections import Counter

def part1(data):
    fish = [int(x) for x in data.split(",")]
    for _ in range(80):
        new_fish = fish.count(0)
        fish = [6 if f == 0 else f - 1 for f in fish] + [8] * new_fish
    return len(fish)

def part2(data):
    fish = Counter(int(x) for x in data.split(","))
    for _ in range(256):
        new_fish = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[6] += new_fish
        fish[8] = new_fish
    return sum(fish.values())

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = next(f).strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")