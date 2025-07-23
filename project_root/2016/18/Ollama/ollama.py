import sys

def count_safes(row, total_lines):
    safe, first_solution = row.count('.'), 0
    for _ in range(1, total_lines):
        next_row = '..'
        idx, end = 2, len(row) - 1
        while idx <= end:
            center = '.' if row[idx - 1] == row[idx + 1] else '^'
            next_row += center + '.'
            safe += (center == '.')
            idx += 2
        next_row += '..'
        first_solution, row = (safe if _ == 40 else first_solution), next_row[1:-1]
    return first_solution, safe

with open(sys.argv[1], 'r') as infile:
    data = infile.read()

first, second = count_safes(data, 400000)

sys.stdout.write(f"{first} {second}")