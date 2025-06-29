import numpy as np
import sys

INPUT = 3018458

inout_strings = sys.argv[1]
with open(inout_strings, 'r')  as file:
    INPUT = int(file.read().strip())

def find_elf(elves):
    if len(elves) <= 2:
        return elves[0] + 1

    if len(elves) % 2:
        return find_elf(np.roll(elves[::2], 1))
    else:
        return find_elf(elves[::2])


def new_rules(elves):
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

    return new_rules(np.roll(new, across-removed))


elf_circle = np.arange(INPUT)

print(find_elf(elf_circle), new_rules(elf_circle))