import sys
def count_safes(row, total_rows):
    row = row.rstrip('\n')
    width = len(row)
    mask = 0
    for c in row:
        mask = (mask << 1) | (1 if c == '^' else 0)
    total_safe = 0
    first_sol = 0
    mask_limit = (1 << width) - 1
    for i in range(total_rows):
        traps = mask.bit_count()
        total_safe += width - traps
        if i == 39:
            first_sol = total_safe
        mask = ((mask << 1) ^ (mask >> 1)) & mask_limit
    return first_sol, total_safe

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = f.read()
    first, second = count_safes(data, 400000)
    sys.stdout.write(f"{first} {second}")