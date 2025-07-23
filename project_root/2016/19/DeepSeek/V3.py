import numpy as np
import sys


def part1(elves):
    n = len(elves)
    if n == 1:
        return elves[0] + 1
    if n % 2:
        return part1(np.roll(elves[::2], -1))
    return part1(elves[::2])


def part2(elves):
    n = len(elves)
    if n == 1:
        return elves[0] + 1
    
    across = n // 2
    if n % 2:
        new = np.roll(elves, -across)[1::3]
    else:
        new = np.roll(elves, -across)[::3]
    
    return part2(new)


with open(sys.argv[1], 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(np.arange(data))} {part2(np.arange(data))}")