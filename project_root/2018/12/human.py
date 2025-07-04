
from functools import reduce
from collections import defaultdict
import sys


def calc_score_1(state, low_pot, high_pot):
    score = 0
    for pot in range(low_pot, high_pot+1):
        if state[pot]:
            score += pot
    return score

def part1(file_path):
    # Read the rules, convert '.' = 0 and '#' = 1 and storing as binary
    # There are 32 combinations
    rules = [ 0 for i in range(32) ]
    with open(file_path, 'r') as file:
        init_state = file.readline().rstrip("\n")
        file.readline()
        while line := file.readline().rstrip("\n"):
            if line[-1] == '#':
                idx = int(line[0:5].replace('#', '1').replace('.', '0'), 2)
                rules[idx] = 1

    low_pot = 0
    high_pot = len(init_state)-1
    state = defaultdict(int)
    for idx, c in enumerate(init_state[15:]):
        state[idx] = 1 if c == '#' else 0

    for cycle in range(20):
        new_state = defaultdict(int)
        for pot in range(low_pot-2, high_pot+3):
            # Create integer from slice of five pots
            s = [ state[idx] for idx in range(pot-2, pot+3)  ]
            n = reduce(lambda acc, b: (acc << 1) | b, s, 0)
            new_state[pot] = rules[n]
            if rules[n]:                # If new plant, possibly adjust low/high
                low_pot = min(low_pot, pot)
                high_pot = max(high_pot, pot)

        state = new_state

    return calc_score_1(state, low_pot, high_pot)


def calc_score_2(state, low_pot, high_pot):
    score = 0
    for pot in range(low_pot, high_pot+1):
        if state[pot]:
            score += pot
    return score

def part2(file_path):
    # Read the rules, convert '.' = 0 and '#' = 1 and storing as binary
    # There are 32 combinations
    rules = [ 0 for i in range(32) ]
    with open(file_path, 'r') as file:
        init_state = file.readline().rstrip("\n")
        file.readline()
        while line := file.readline().rstrip("\n"):
            if line[-1] == '#':
                idx = int(line[0:5].replace('#', '1').replace('.', '0'), 2)
                rules[idx] = 1

    low_pot = 0
    high_pot = len(init_state)-1
    state = defaultdict(int)
    for idx, c in enumerate(init_state[15:]):
        state[idx] = 1 if c == '#' else 0

    last_score = 0
    last_diff = 0
    diffs = []
    for cycle in range(1, 500):
        new_state = defaultdict(int)
        for pot in range(low_pot-2, high_pot+3):
            # Create integer from slice of five pots
            s = [ state[idx] for idx in range(pot-2, pot+3)  ]
            n = reduce(lambda acc, b: (acc << 1) | b, s, 0)
            new_state[pot] = rules[n]
            if rules[n]:                # If new plant, possibly adjust low/high
                low_pot = min(low_pot, pot)
                high_pot = max(high_pot, pot)

        state = new_state

        score = calc_score_2(state, low_pot, high_pot)
        diff = score - last_score
        last_score = score

        # Wait for the difference to start repeating, then store away
        if diff == last_diff or len(diffs):
            diffs.append((diff, score, cycle))
        last_diff = diff

    # Make sure the recent differences are the same
    for chk in range(1, 10):
        if diffs[-chk][0] != diffs[-chk-1][0]:
            raise Exception(f"BAD, {diffs[-chk]} / {diffs[-chk-1]}")

    # Just a linear equation, score = a * cycle + b
    a = diffs[-1][0]                        # Diff amt is factor
    b = diffs[-1][1] - diffs[-1][2] * a     # b = score - cycle * diff

    target = 50000000000
    return a * target + b


inout_strings = sys.argv[1]
sys.stdout.write(f"{part1(inout_strings)} {part2(inout_strings)}") 