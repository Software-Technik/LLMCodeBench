import sys


def count_safes(row, total_lines):
    safe = 0
    for i in range(total_lines):
        if i == 40:
            first_solution = safe
        safe += row.count('.')
        old = '.' + row + '.'
        row = ''
        for left, right in zip(old, old[2:]):
            row += '^' if left != right else '.'
    return first_solution, safe

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    data = infile.read()

first, second = count_safes(data, 400000)

sys.stdout.write(f"{first} {second}")  