import sys
from collections import Counter


def part1(data):
    columns = zip(*data)
    first_solution = []
    for column in columns:
        counter = Counter(column)
        most_common = counter.most_common(1)[0][0]
        first_solution.append(most_common)
    return ''.join(first_solution)

def part2(data):
    columns = zip(*data)
    second_solution = []
    for column in columns:
        counter = Counter(column)
        least_common = counter.most_common()[-1][0]
        second_solution.append(least_common)
    return ''.join(second_solution)


inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = [line.strip() for line in infile]

sys.stdout.write(f"{part1(data)} {part2(data)}")