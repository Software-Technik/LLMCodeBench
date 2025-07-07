from itertools import permutations
import sys

def part1(data):
        guest = parse_guest(data)
        return calc_max_happiness(guest)

def part2(data):
    guest = parse_guest(data)

    me = {i: 0 for i in guest}
    for i in guest:
        guest[i]["me"] = 0
    guest["me"] = me

    return calc_max_happiness(guest)

def parse_guest(data):
    guest = {}
    for line in data:
        parts = line.split()
        happy = 1 if parts[2] == "gain" else -1
        happy *= int(parts[3])
        if parts[0] not in guest:
            guest[parts[0]] = {}
        guest[parts[0]][parts[10][:-1]] = happy
    return guest

def calc_max_happiness(guest):
    guest_len = len(guest)
    max_happiness = float('-inf')
    for arrangement in permutations(guest.keys()):
        changed = sum(guest[v][arrangement[(i + 1) % guest_len]] + guest[v][arrangement[i - 1]] for i, v in enumerate(arrangement))
        if changed > max_happiness:
            max_happiness = changed
    return max_happiness

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")