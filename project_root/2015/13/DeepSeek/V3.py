from itertools import permutations
import sys

def part1(data):
    guest = parse_guest(data)
    return calc_max_happiness(guest)

def part2(data):
    guest = parse_guest(data)
    me = {}
    for i in guest:
        guest[i]["me"] = 0
        me[i] = 0
    guest["me"] = me
    return calc_max_happiness(guest)

def parse_guest(data):
    guest = {}
    for line in data:
        parts = line.split()
        happy = (1 if parts[2] == "gain" else -1) * int(parts[3])
        if parts[0] not in guest:
            guest[parts[0]] = {}
        guest[parts[0]][parts[10][:-1]] = happy
    return guest

def calc_max_happiness(guest):
    names = list(guest.keys())
    n = len(names)
    max_happiness = -float('inf')
    for arrangement in permutations(names):
        happiness = 0
        for i in range(n):
            left = arrangement[i-1]
            right = arrangement[(i+1) % n]
            current = arrangement[i]
            happiness += guest[current][left] + guest[current][right]
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")