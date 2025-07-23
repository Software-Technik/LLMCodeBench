import sys

def count_safes(row, total_lines):
    safe = 0
    first_solution = 0
    for i in range(total_lines):
        safe += row.count('.')
        if i == 39:
            first_solution = safe
        new_row = []
        extended_row = '.' + row + '.'
        for left, right in zip(extended_row, extended_row[2:]):
            new_row.append('^' if left != right else '.')
        row = ''.join(new_row)
    return first_solution, safe

with open(sys.argv[1], 'r') as infile:
    data = infile.read().strip()

first, second = count_safes(data, 400000)

sys.stdout.write(f"{first} {second}")