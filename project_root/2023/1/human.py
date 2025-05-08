import sys
from functools import reduce
from operator import mul



def part1(data):
    total = 0
    for line in data.splitlines():
        number = ""
        for c in line:
            if c.isdigit():
                number += c
                break

        for c in reversed(line):
            if c.isdigit():
                number += c
                break

        total += int(number)
    return total

def part2(data):
    total = 0
    for line in data.splitlines():
        _, game_data = line.split(":", maxsplit=1)
        power = get_power(game_data.strip())
        total += power
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(str([part1(data), part2(data)]))

