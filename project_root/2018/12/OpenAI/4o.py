from collections import defaultdict
import sys

def calc_score(state, low_pot, high_pot):
    return sum(pot for pot in range(low_pot, high_pot + 1) if state[pot])

def part1(file_path):
    rules = [0] * 32
    with open(file_path, 'r') as file:
        init_state = file.readline().strip("\n")
        file.readline()
        for line in file:
            line = line.strip("\n")
            if line[-1] == '#':
                idx = int(line[:5].replace('#', '1').replace('.', '0'), 2)
                rules[idx] = 1

    low_pot = 0
    high_pot = len(init_state) - 1
    state = defaultdict(int)
    for idx, c in enumerate(init_state):
        state[idx] = 1 if c == '#' else 0

    for _ in range(20):
        new_state = defaultdict(int)
        new_low_pot = new_high_pot = None
        for pot in range(low_pot - 2, high_pot + 3):
            n = sum(state[idx] << (4 - (idx - pot + 2)) for idx in range(pot - 2, pot + 3))
            if rules[n]:
                new_state[pot] = 1
                new_low_pot = pot if new_low_pot is None else min(new_low_pot, pot)
                new_high_pot = pot if new_high_pot is None else max(new_high_pot, pot)

        state = new_state
        low_pot = new_low_pot
        high_pot = new_high_pot

    return calc_score(state, low_pot, high_pot)

def part2(file_path):
    rules = [0] * 32
    with open(file_path, 'r') as file:
        init_state = file.readline().strip("\n")
        file.readline()
        for line in file:
            line = line.strip("\n")
            if line[-1] == '#':
                idx = int(line[:5].replace('#', '1').replace('.', '0'), 2)
                rules[idx] = 1

    low_pot = 0
    high_pot = len(init_state) - 1
    state = defaultdict(int)
    for idx, c in enumerate(init_state):
        state[idx] = 1 if c == '#' else 0

    last_score = 0
    last_diff = 0
    diffs = []
    for cycle in range(1, 500):
        new_state = defaultdict(int)
        new_low_pot = new_high_pot = None
        for pot in range(low_pot - 2, high_pot + 3):
            n = sum(state[idx] << (4 - (idx - pot + 2)) for idx in range(pot - 2, pot + 3))
            if rules[n]:
                new_state[pot] = 1
                new_low_pot = pot if new_low_pot is None else min(new_low_pot, pot)
                new_high_pot = pot if new_high_pot is None else max(new_high_pot, pot)

        state = new_state
        low_pot = new_low_pot
        high_pot = new_high_pot

        score = calc_score(state, low_pot, high_pot)
        diff = score - last_score
        last_score = score

        if diff == last_diff or diffs:
            diffs.append((diff, score, cycle))
        last_diff = diff

    for chk in range(1, 10):
        if diffs[-chk][0] != diffs[-chk - 1][0]:
            raise Exception(f"BAD, {diffs[-chk]} / {diffs[-chk - 1]}")

    a = diffs[-1][0]
    b = diffs[-1][1] - diffs[-1][2] * a

    target = 50000000000
    return a * target + b

inout_strings = sys.argv[1]
sys.stdout.write(f"{part1(inout_strings)} {part2(inout_strings)}")