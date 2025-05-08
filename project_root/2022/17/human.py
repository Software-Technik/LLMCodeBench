import sys
from itertools import zip_longest

def part1(data):
    state = {}
    return _part1(state, data)


def _part1(state, data):
    jets = data[0]
    jet_len = len(jets)
    jet_idx = 0

    above = 3

    rocks = [
        [[0, 0, 1, 1, 1, 1, 0]],
        [[0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]],
        [[0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0]],
        [[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0]],
        [[0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0]],
    ]
    rock_idx = 0
    state["room"] = [[1, 1, 1, 1, 1, 1, 1]]

    while rock_idx < 2022:
        state["room"] += [[0] * 7 for _ in range(above)]
        state["rock"] = rocks[rock_idx % 5]
        height = len(state["room"])

        while True:
            org_rock = state["rock"]
            jet = jets[jet_idx]
            rock_push(state, jet)
            if check_overlap(state, height):
                state["rock"] = org_rock
            jet_idx = (jet_idx + 1) % jet_len

            height -= 1
            if check_overlap(state, height):
                height += 1
                rock_stop(state, height)
                rock_idx += 1
                break

    return len(state["room"]) - 1


def part2(data):
    state = {}
    return _part2(state, data)


def _part2(state, data):
    jets = data[0]
    jet_len = len(jets)
    jet_idx = 0
    above = 3

    rocks = [
        [[0, 0, 1, 1, 1, 1, 0]],
        [[0, 0, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0]],
        [[0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0]],
        [[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0]],
        [[0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0]],
    ]
    rock_idx = 0
    state["room"] = [[1, 1, 1, 1, 1, 1, 1]]
    state["check_depth"] = 10
    state["states"] = {}
    state["state_history"] = []
    state["_break"] = False

    while True:
        if state["_break"]:
            break

        org_height = len(state["room"])
        state["room"] += [[0] * 7 for _ in range(above)]
        state["rock"] = rocks[rock_idx % 5]
        height = len(state["room"])

        while True:
            org_rock = state["rock"]
            jet = jets[jet_idx]
            rock_push(state, jet)
            if check_overlap(state, height):
                state["rock"] = org_rock
            jet_idx = (jet_idx + 1) % jet_len

            height -= 1
            if check_overlap(state, height):
                height += 1
                rock_stop(state, height)
                check_state_history(state, rock_idx, jet_idx, org_height)
                rock_idx += 1
                break

    repeated = state["state_history"][-1]
    round_start = state["state_history"].index(repeated)
    round_len = len(state["state_history"]) - round_start - 1

    round_height_diff_sum = sum(state["states"][state["state_history"][i]]
                                for i in range(round_start, round_start + round_len))

    rocks = 1000000000000
    tower_height = sum(state["states"][state["state_history"][i]]
                       for i in range(min(round_start, rocks)))

    if rocks > round_start:
        after_repeat = rocks - round_start
        rounds = after_repeat // round_len
        left_rocks = after_repeat % round_len

        tower_height += round_height_diff_sum * rounds
        tower_height += sum(state["states"][state["state_history"][round_start + i]]
                            for i in range(left_rocks))

    return tower_height


def rock_push(state, push):
    rock = state["rock"]
    if push == ">":
        if sum(row[-1] for row in rock) == 0:
            rock = [[0] + row[:-1] for row in rock]
    else:
        if sum(row[0] for row in rock) == 0:
            rock = [row[1:] + [0] for row in rock]
    state["rock"] = rock


def check_overlap(state, height):
    rock = [[0] * 7 for _ in range(height)] + state["rock"]
    full_height = height + len(state["rock"])
    room = state["room"]

    if len(room) > full_height:
        room = room[:full_height]
    else:
        room += [[0] * 7 for _ in range(full_height - len(room))]

    for i in range(full_height - 1, -1, -1):
        for x, y in zip(room[i], rock[i]):
            if x + y > 1:
                return True
    return False


def rock_stop(state, height):
    room = state["room"]
    rock = [[0] * 7 for _ in range(height)] + state["rock"]

    new_room = []
    for roomline, rockline in zip_longest(room, rock, fillvalue=[0] * 7):
        new_room.append([x + y for x, y in zip(roomline, rockline)])

    while sum(new_room[-1]) == 0:
        new_room.pop()

    state["room"] = new_room


def check_state_history(state, rock_idx, jet_idx, height):
    line_num = min(len(state["room"]), state["check_depth"])
    scan = "".join(str(i) for line in state["room"][-line_num:] for i in line)
    key = (rock_idx % 5, jet_idx, scan)
    height_diff = len(state["room"]) - height

    if key in state["states"]:
        state["state_history"].append(key)
        state["_break"] = True
    else:
        state["states"][key] = height_diff
        state["state_history"].append(key)


def print_room(state):
    for r in reversed(state["room"]):
        print("".join(map(str, r)))
    print()


input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")
