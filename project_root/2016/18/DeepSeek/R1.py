import sys

def count_safes(row, total_lines):
    safe = 0
    first_solution = None
    n = len(row)
    for i in range(total_lines):
        if i == 40:
            first_solution = safe
        safe += row.count('.')
        next_row = []
        for j in range(n):
            left = row[j-1] if j-1 >= 0 else '.'
            right = row[j+1] if j+1 < n else '.'
            next_row.append('^' if left != right else '.')
        row = ''.join(next_row)
    return first_solution, safe

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    data = infile.read().strip()

first, second = count_safes(data, 400000)

sys.stdout.write(f"{first} {second}")