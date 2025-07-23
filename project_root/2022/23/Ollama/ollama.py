import sys
from collections import defaultdict

def part1(data):
    order = ["N", "S", "W", "E"]
    elves = parse_data(data)

    for _ in range(10):
        locations = defaultdict(int)
        elves_new = {}
        items = list(elves.items())
        for pos, v in items:
            if not v: continue

            surrounds = [(pos[0] - 1, pos[1] + j) for j in range(-1, 2)] + [(pos[0], pos[1] + j) for j in range(-1, 2)] + [(pos[0] + 1, pos[1] + j) for j in range(-1, 2)]
            if all(elves[x] == 0 for x in surrounds): continue

            for d in order:
                new_positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
                directions_checks = [[(new_positions[0][0] - 1, new_positions[0][1]) for _ in range(-1, 2)],
                                     [(new_positions[1][0] + 1, new_positions[1][1]) for _ in range(-1, 2)],
                                     [(new_positions[2][0], new_positions[2][1] - 1) for _ in range(-1, 2)],
                                     [(new_positions[3][0], new_positions[3][1] + 1) for _ in range(-1, 2)]]

                new_pos = directions_checks[order.index(d)][1]
                if all(elves[c] == 0 for c in directions_checks[order.index(d)]): continue

                elves_new[pos] = new_pos
                locations[new_pos] += 1
                break

        repeated = [p for p, c in locations.items() if c > 1]
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
    round_ = 1

    while True:
        locations = defaultdict(int)
        elves_new = {}
        items = list(elves.items())
        for pos, v in items:
            if not v: continue
            surrounds = [(pos[0] - 1, pos[1] + j) for j in range(-1, 2)] + [(pos[0], pos[1] + j) for j in range(-1, 2)] + [(pos[0] + 1, pos[1] + j) for j in range(-1, 2)]

            if all(elves[x] == 0 for x in surrounds): continue

            for d in order:
                new_positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
                directions_checks = [[(new_positions[0][0] - 1, new_positions[0][1]) for _ in range(-1, 2)],
                                     [(new_positions[1][0] + 1, new_positions[1][1]) for _ in range(-1, 2)],
                                     [(new_positions[2][0], new_positions[2][1] - 1) for _ in range(-1, 2)],
                                     [(new_positions[3][0], new_positions[3][1] + 1) for _ in range(-1, 2)]]

                new_pos = directions_checks[order.index(d)][1]
                if all(elves[c] == 0 for c in directions_checks[order.index(d)]): continue
                elves_new[pos] = new_pos
                locations[new_pos] += 1
                break

        repeated = [p for p, c in locations.items() if c > 1]
        for pos_org, pos_new in elves_new.items():
            if pos_new not in repeated:
                elves[pos_org] = 0
                elves[pos_new] = 1
        order = order[1:] + [order[0]]

        state_new = gen_state(elves)
        if state == state_new: return round_
        else: state = state_new

        round_ += 1

def parse_data(data):
    elves = defaultdict(int)
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "#":
                elves[(i, j)] = 1
    return elves

def get_region_corners(elves):
    min_x, max_x = float("inf"), -float("inf")
    min_y, max_y = float("inf"), -float("inf")

    for y, x in elves:
        if x < min_x: min_x = x
        if x > max_x: max_x = x
        if y < min_y: min_y = y
        if y > max_y: max_y = y

    return min_x, max_x, min_y, max_y

def gen_state(elves):
    return set(pos for pos, v in elves.items() if v == 1)

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")