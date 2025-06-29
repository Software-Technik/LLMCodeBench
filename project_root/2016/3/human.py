import sys
from itertools import chain

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    puzzle = infile.readlines()

horizontal = [[int(value) for value in row.split()] for row in puzzle]
vertical = list(chain.from_iterable(zip(*horizontal)))


def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c


def find_triangles(candidates, second_part=False):
    if not second_part:
        return sum(is_triangle(row) for row in candidates)
    else:
        return sum(is_triangle(candidates[i:i+3])
                   for i in range(0, len(candidates)-2, 3))


print(find_triangles(horizontal), find_triangles(vertical, True))