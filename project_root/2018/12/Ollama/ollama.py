from functools import reduce
from collections import defaultdict
import sys

def calc_score(state, low_pot, high_pot):
    return sum(pot for pot in range(low_pot, high_pot + 1) if state[pot])

def parse_input(file_path):
    with open(file_path, 'r') as file:
        init_state = file.readline().strip()
        file.readline()
        rules = [0] * 32
        while line := file.readline().strip():
            if line[-1] == '#':
                idx = int(line[:5].replace('.', '0').replace('#', '1'), 2)
                rules[idx] = 1
    return init_state, rules

def part1(file_path):
    init_state, rules = parse_input(file_path)
    state = defaultdict(int, {i: (c == '#') for i, c in enumerate(init_state[15:])})
    low_pot, high_pot = 0, len(init_state) - 1

    for _ in range(20):
        new_state = defaultdict(int)
        for pot in range(low_pot - 2, high_pot + 3):
            n = reduce(lambda acc, b: (acc << 1) | b, [state[idx] for idx in range(pot - 2, pot + 3)], 0)
            new_state[pot] = rules[n]
            if rules[n]:
                low_pot = min(low_pot, pot)
                high_pot = max(high_pot, pot)
        state = new_state

    return calc_score(state, low_pot, high_pot)

def part2(file_path):
    init_state, rules = parse_input(file_path)

    state = defaultdict(int, {i: (c == '#') for i, c in enumerate(init_state[15:])})
    low_pot, high_pot = 0, len(init_state) - 1

    score = calc_score(state, low_pot, high_pot)
    last_diff = None
    diffs = []

    target_cycles = 50000000000

    for cycle in range(1, target_cycles + 1):
        new_state = defaultdict(int)
        for pot in range(low_pot - 2, high_pot + 3):
            n = reduce(lambda acc, b: (acc << 1) | b, [state[idx] for idx in range(pot - 2, pot + 3)], 0)
            new_state[pot] = rules[n]
            if rules[n]:
                low_pot = min(low_pot, pot)
                high_pot = max(high_pot, pot)

        state = new_state
        new_score = calc_score(state, low_pot, high_pot)
        diff = new_score - score

        if last_diff and diff == last_diff:
            a = (diff * cycle) // (cycle - len(diffs))
            return score + ((target_cycles - cycle) // cycle) * a
        elif len(diffs) > 0 and diff != last_diff:
            diffs.clear()

        score, last_diff = new_score, diff

    return part1(file_path)

sys.stdout.write(f"{part1(sys.argv[1])} {part2(sys.argv[1])}")