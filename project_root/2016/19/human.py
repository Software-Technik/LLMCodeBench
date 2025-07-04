import numpy as np
import sys


def part1(elves):
    if len(elves) <= 2:
        return elves[0] + 1

    if len(elves) % 2:
        return part1(np.roll(elves[::2], 1))
    else:
        return part1(elves[::2])


def part2(elves):
    n = len(elves)
    if n <= 2:
        return elves[0] + 1

    across = n // 2
    if n % 2:
        removed = n - (n+1)//3
        new = np.roll(elves, -across)[1::3]
    else:
        removed = n - n//3
        new = np.roll(elves, -across)[2::3]

    return part2(np.roll(new, across-removed))

inout_strings = sys.argv[1]
with open(inout_strings, 'r')  as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(np.arange(data))} {part2(np.arange(data))}")  
