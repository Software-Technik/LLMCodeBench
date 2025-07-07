import sys
from math import sqrt, ceil

def compute_i(time, distance):
    i = ceil((time - sqrt(time*time - 4*distance)) / 2)
    if i*(time - i) <= distance:
        i += 1
    return i

def part1(times, distances):
    total = 1
    for t, d in zip(times, distances):
        i = compute_i(t, d)
        mp = (t - 1)//2 + (t%2 == 0)
        if i < mp:
            total *= ((mp - i)*2 + 1 if t%2 == 0 else (mp - i + 1)*2)
    return total

def part2(time, distance):
    i = compute_i(time, distance)
    mp = (time - 1)//2 + (time%2 == 0)
    if i < mp:
        return (mp - i)*2 + 1 if time%2 == 0 else (mp - i + 1)*2
    return 0

with open(sys.argv[1]) as f:
    l1 = f.readline().split()[1:]
    l2 = f.readline().split()[1:]
    times = list(map(int, l1)); distances = list(map(int, l2))
    t0, d0 = times[0], distances[0]
print(part1(times, distances), part2(t0, d0))