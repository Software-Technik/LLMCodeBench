import sys
from collections import Counter


def part1(data):
    columns = (''.join(column) for column in zip(*data))

    first_solution = ''
    second_solution = ''

    for column in columns:
        (most, _), *others, (least, _) = Counter(column).most_common()
        first_solution += most
        second_solution += least

    return first_solution

def part2(data):
    columns = (''.join(column) for column in zip(*data))

    first_solution = ''
    second_solution = ''

    for column in columns:
        (most, _), *others, (least, _) = Counter(column).most_common()
        first_solution += most
        second_solution += least

    return second_solution


inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readlines()

sys.stdout.write(f"{part1(data)} {part2(data)}") 