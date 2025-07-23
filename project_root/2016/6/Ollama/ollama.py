import sys
from collections import Counter

def part1_2(data):
    columns = (''.join(column) for column in zip(*data))
    first_solution, second_solution = '', ''

    for column in columns:
        (most, _), *_, (least, _) = Counter(column).most_common()
        first_solution += most
        second_solution += least

    return first_solution, second_solution

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read().splitlines()

first, second = part1_2(data)
sys.stdout.write(f"{first} {second}")