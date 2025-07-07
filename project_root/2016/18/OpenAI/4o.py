import sys

def count_safes(row, total_lines):
    safe = row.count('.')
    first_solution = 0
    for i in range(1, total_lines):
        if i == 40:
            first_solution = safe
        old = '.' + row + '.'
        row = ''.join('^' if left != right else '.' for left, right in zip(old, old[2:]))
        safe += row.count('.')
    return first_solution, safe

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    data = infile.read().strip()

first, second = count_safes(data, 400000)

sys.stdout.write(f"{first} {second}")