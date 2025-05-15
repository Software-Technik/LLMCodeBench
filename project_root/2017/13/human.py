import sys
from collections import defaultdict
from math import lcm
from itertools import count

def make_firewall(lines):
    firewall = defaultdict(set)
    for line in lines:
        if not line.strip():
            continue
        depth, height = map(int, line.split(": "))
        firewall[height].add(depth)
    return dict(firewall)

def is_caught(depth, height, delay=0):
    return (depth + delay) % (2 * (height - 1)) == 0

def calculate_severity(firewall):
    total = 0
    for height in firewall:
        for depth in firewall[height]:
            if is_caught(depth, height):
                total += depth * height
    return total

def one_remains(height, depths):
    return len(depths) == height - 2

def pymod(a, b):
    m = (-a) % b
    return 0 if m == 0 else m + b

def find_allowed_delay(height, depths):
    period = 2 * (height - 1)
    potential = set(range(0, period, 2))
    forbidden = {pymod(depth, period) for depth in depths}
    allowed = potential - forbidden
    delay = next(iter(allowed))
    return delay, period

def find_delay_params(walls):
    delays = []
    periods = []
    for height, depths in walls:
        d, p = find_allowed_delay(height, depths)
        delays.append(d)
        periods.append(p)

    common_multi = lcm(*periods)
    allowed = set(range(common_multi))
    for d, p in zip(delays, periods):
        valid = {d + i for i in range(0, common_multi, p)}
        allowed &= valid

    delay = next(iter(allowed))
    return delay, common_multi

def is_group_caught(group, delay):
    height, depths = group
    return any(is_caught(depth, height, delay) for depth in depths)

def part1(data):
    firewall = make_firewall(data)
    return calculate_severity(firewall)

def part2(data):
    firewall = make_firewall(data)
    calc_group = []
    control_group = []
    for height in firewall:
        if one_remains(height, firewall[height]):
            calc_group.append((height, firewall[height]))
        else:
            control_group.append((height, firewall[height]))

    delay, step = find_delay_params(calc_group)
    while any(is_group_caught(group, delay) for group in control_group):
        delay += step
    return delay

# Entrée depuis la ligne de commande
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

# Affiche les résultats des deux parties
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")