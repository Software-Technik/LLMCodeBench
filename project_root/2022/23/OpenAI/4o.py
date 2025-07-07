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
            if all(elves.get((pos[0] + dx, pos[1] + dy), 0) == 0 for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]):
                continue

            for d in order:
                if d == "N":
                    checks, new_pos = [(-1, -1), (-1, 0), (-1, 1)], (pos[0] - 1, pos[1])
                elif d == "S":
                    checks, new_pos = [(1, -1), (1, 0), (1, 1)], (pos[0] + 1, pos[1])
                elif d == "W":
                    checks, new_pos = [(-1, -1), (0, -1), (1, -1)], (pos[0], pos[1] - 1)
                elif d == "E":
                    checks, new_pos = [(-1, 1), (0, 1), (1, 1)], (pos[0], pos[1] + 1)

                if all(elves.get((pos[0] + dx, pos[1] + dy), 0) == 0 for dx, dy in checks):
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
    min_x, max_x, min_y, max_y = get_region_corners(p)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(p)

def part2(data):
    order = ["N", "S", "W", "E"]
    elves = parse_data(data)

    state = gen_state(elves)
    round = 1

    while True:
        locations = defaultdict(int)
        elves_new = {}
        items = [pos for pos, v in elves.items() if v == 1]
        for pos in items:
            if all(elves.get((pos[0] + dx, pos[1] + dy), 0) == 0 for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]):
                continue

            for d in order:
                if d == "N":
                    checks, new_pos = [(-1, -1), (-1, 0), (-1, 1)], (pos[0] - 1, pos[1])
                elif d == "S":
                    checks, new_pos = [(1, -1), (1, 0), (1, 1)], (pos[0] + 1, pos[1])
                elif d == "W":
                    checks, new_pos = [(-1, -1), (0, -1), (1, -1)], (pos[0], pos[1] - 1)
                elif d == "E":
                    checks, new_pos = [(-1, 1), (0, 1), (1, 1)], (pos[0], pos[1] + 1)

                if all(elves.get((pos[0] + dx, pos[1] + dy), 0) == 0 for dx, dy in checks):
                    elves_new[pos] = new_pos
                    locations[new_pos] += 1
                    break

        repeated = {p for p, c in locations.items() if c > 1}
        for pos_org, pos_new in elves_new.items():
            if pos_new not in repeated:
                elves[pos_org] = 0
                elves[pos_new] = 1

        order = order[1:] + [order[0]]

        state_new = gen_state(elves)
        if state == (state & state_new):
            return round
        state = state_new

        round += 1

def parse_data(data):
    return {(i, j): 1 for i, line in enumerate(data) for j, c in enumerate(line) if c == "#"}

def get_region_corners(elves):
    min_x, max_x, min_y, max_y = min(p[0] for p in elves), max(p[0] for p in elves), min(p[1] for p in elves), max(p[1] for p in elves)
    return min_x, max_x, min_y, max_y

def gen_state(elves):
    return {pos for pos, v in elves.items() if v == 1}

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")