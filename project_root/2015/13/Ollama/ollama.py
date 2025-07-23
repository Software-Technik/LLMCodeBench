from itertools import permutations
import sys

def part1(data):
    return calc_max_happiness(parse_guest(data))

def part2(data):
    guest = parse_guest(data)
    me = {key: 0 for key in guest}
    guest["You"] = me
    me["You"] = 0
    return calc_max_happiness(guest)

def parse_guest(data):
    guest = {}
    for line in data:
        parts = line.split()
        happy = int(parts[3]) * (1 if parts[2] == "gain" else -1)
        name, neighbor = parts[0], parts[10][:-1]
        guest.setdefault(name, {})[neighbor] = happy
    return guest

def calc_max_happiness(guest):
    guests_len = len(guest)
    max_happiness = float('-inf')
    for arrangement in permutations(guest.keys()):
        total_changed = 0
        for i, g1 in enumerate(arrangement):
            g2, g3 = arrangement[(i + 1) % guests_len], arrangement[i - 1]
            diff1, diff2 = guest[g1][g2] if g2 in guest[g1] else 0, guest[g1][g3] if g3 in guest[g1] else 0
            total_changed += (diff1 + diff2)
        max_happiness = max(max_happiness, total_changed)
    return max_happiness

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")