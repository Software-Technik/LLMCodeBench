import sys
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    init_state = lines[0][15:]
    rules = [0] * 32
    for line in lines[2:]:
        if line.endswith('#'):
            s = line[:5].replace('.', '0').replace('#', '1')
            idx = int(s, 2)
            rules[idx] = 1
    return init_state, rules

def step(state, low, high, rules):
    new_state = defaultdict(int)
    new_low = None
    new_high = None
    for pot in range(low - 2, high + 3):
        n = 0
        for i in range(pot - 2, pot + 3):
            n = (n << 1) | state[i]
        if rules[n]:
            new_state[pot] = 1
            if new_low is None:
                new_low = pot
                new_high = pot
            else:
                new_low = min(new_low, pot)
                new_high = max(new_high, pot)
    if new_low is None:
        new_low = low
        new_high = high
    return new_state, new_low, new_high

def calc_score(state, low, high):
    total = 0
    for pot in range(low, high + 1):
        if state[pot]:
            total += pot
    return total

def part1(file_path):
    init_state, rules = read_input(file_path)
    state = defaultdict(int)
    for i, c in enumerate(init_state):
        state[i] = 1 if c == '#' else 0
    low = 0
    high = len(init_state) - 1
    for _ in range(20):
        state, low, high = step(state, low, high, rules)
    return calc_score(state, low, high)

def part2(file_path):
    init_state, rules = read_input(file_path)
    state = defaultdict(int)
    for i, c in enumerate(init_state):
        state[i] = 1 if c == '#' else 0
    low = 0
    high = len(init_state) - 1
    last_score = 0
    last_diff = 0
    diffs = []
    for cycle in range(1, 500):
        state, low, high = step(state, low, high, rules)
        current_score = calc_score(state, low, high)
        diff = current_score - last_score
        if diffs or diff == last_diff:
            diffs.append((diff, current_score, cycle))
        last_diff = diff
        last_score = current_score
    for i in range(1, 10):
        if diffs[-i][0] != diffs[-i-1][0]:
            raise Exception(f"Unstable pattern: {diffs[-i]} vs {diffs[-i-1]}")
    a = diffs[-1][0]
    b = diffs[-1][1] - a * diffs[-1][2]
    target = 50000000000
    return a * target + b

if __name__ == '__main__':
    file_path = sys.argv[1]
    part1_ans = part1(file_path)
    part2_ans = part2(file_path)
    sys.stdout.write(f"{part1_ans} {part2_ans}")