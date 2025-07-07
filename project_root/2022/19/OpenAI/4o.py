from collections import deque
from math import prod
import sys

def part1(data):
    blueprints = parse_data(data)
    r = run_blueprints(blueprints, 24)
    return sum((i + 1) * v for i, v in enumerate(r))

def part2(data):
    blueprints = parse_data(data)[:3]
    r = run_blueprints(blueprints, 32)
    return prod(r)

def parse_data(data):
    return [[(int(line.split()[i]), 0, 0, 0) for i in (6, 12, 18, 27)] for line in data]

def run_blueprints(blueprints, time):
    r = []
    for bp in blueprints:
        max_reserves = [max(i) * 1.6 for i in zip(*bp)]
        max_reserves[3] = 99999

        state = ((1, 0, 0, 0), (0, 0, 0, 0))
        queue = deque([state])
        seen = set()
        remaining_time = time

        _max = 0
        while remaining_time > 0:
            for _ in range(len(queue)):
                s = queue.popleft()
                if s in seen:
                    continue

                seen.add(s)
                s1, s2 = s

                if all(a >= b for a, b in zip(s2, bp[3])):
                    s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, bp[3], s1, max_reserves))
                    s1n = tuple(a + b for a, b in zip(s1, (0, 0, 0, 1)))
                    if remaining_time == 1:
                        _max = max(_max, s2n[3])
                    else:
                        queue.append((s1n, s2n))
                else:
                    for robot, cost in enumerate(bp):
                        if s1[robot] < max_reserves[robot] and all(a >= b for a, b in zip(s2, cost)):
                            s2n = tuple(min(a - b + c, d) for a, b, c, d in zip(s2, cost, s1, max_reserves))
                            s1n = tuple(a + (1 if i == robot else 0) for i, a in enumerate(s1))
                            if remaining_time == 1:
                                _max = max(_max, s2n[3])
                            else:
                                queue.append((s1n, s2n))

                    s2n = tuple(min(a + c, d) for a, c, d in zip(s2, s1, max_reserves))
                    queue.append((s1, s2n))

            remaining_time -= 1
        r.append(_max)
    return r

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")