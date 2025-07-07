import sys

def count_safes(row_str, total_lines):
    w = len(row_str)
    mask = (1 << w) - 1
    row = 0
    for c in row_str:
        row = (row << 1) | (c == '^')
    safe_total = 0
    first = 0
    for i in range(total_lines):
        bits = row.bit_count()
        safe_row = w - bits
        safe_total += safe_row
        if i == 40:
            first = safe_total
        row = ((row << 1) ^ (row >> 1)) & mask
    return first, safe_total

with open(sys.argv[1], 'r') as f:
    start = f.readline().strip()
first, second = count_safes(start, 400000)
print(f"{first} {second}")