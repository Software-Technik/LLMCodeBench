import sys
from collections import defaultdict

def part1(data):
    order = ["N", "S", "W", "E"]
    elves = parse_data(data)

    for _ in range(10):
        locations = defaultdict(int)
        elves_new = {}
        items = [pos for pos, v in elves.items() if v == 1]
        for pos in items:
            checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), 
                     (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), 
                     (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            if all(elves.get(c, 0) == 0 for c in checks):
                continue

            for d in order:
                if d == "N":
                    checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)]
                    new_pos = (pos[0] - 1, pos[1])
                elif d == "S":
                    checks = [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
                    new_pos = (pos[0] + 1, pos[1])
                elif d == "W":
                    checks = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
                    new_pos = (pos[0], pos[1] - 1)
                elif d == "E":
                    checks = [(pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
                    new_pos = (pos[0], pos[1] + 1)

                if all(elves.get(c, 0) == 0 for c in checks):
                    elves_new[pos] = new_pos
                    locations[new_pos] += 1
                    break

        repeated = {p for p, c in locations.items() if c > 1}
        for pos_org, pos_new in elves_new.items():
            if pos_new not in repeated:
                elves[pos_org] = 0
                elves[pos_new] = 1

        order = order[1:] + [order[0]]

    p = [pos for pos, v in elves.items() if v == 1]
    min_x = min(x for y, x in p)
    max_x = max(x for y, x in p)
    min_y = min(y for y, x in p)
    max_y = max(y for y, x in p)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(p)

def part2(data):
    order = ["N", "S", "W", "E"]
    elves = parse_data(data)
    prev_elves = set()

    round = 1
    while True:
        locations = defaultdict(int)
        elves_new = {}
        items = [pos for pos, v in elves.items() if v == 1]
        current_elves = set(items)
        if prev_elves == current_elves:
            return round
        prev_elves = current_elves

        for pos in items:
            checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), 
                     (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), 
                     (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            if all(elves.get(c, 0) == 0 for c in checks):
                continue

            for d in order:
                if d == "N":
                    checks = [(pos[0] - 1, pos[1] - 1), (pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1)]
                    new_pos = (pos[0] - 1, pos[1])
                elif d == "S":
                    checks = [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1)]
                    new_pos = (pos[0] + 1, pos[1])
                elif d == "W":
                    checks = [(pos[0] - 1, pos[1] - 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] - 1)]
                    new_pos = (pos[0], pos[1] - 1)
                elif d == "E":
                    checks = [(pos[0] - 1, pos[1] + 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1] + 1)]
                    new_pos = (pos[0], pos[1] + 1)

                if all(elves.get(c, 0) == 0 for c in checks):
                    elves_new[pos] = new_pos
                    locations[new_pos] += 1
                    break

        repeated = {p for p, c in locations.items() if c > 1}
        for pos_org, pos_new in elves_new.items():
            if pos_new not in repeated:
                elves[pos_org] = 0
                elves[pos_new] = 1

        order = order[1:] + [order[0]]
        round += 1

def parse_data(data):
    elves = defaultdict(int)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                elves[(i, j)] = 1
    return elves

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")