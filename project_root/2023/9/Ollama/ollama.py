import sys

def get_pascal_triangle_row(row):
    current_row = [1] * (row + 1)
    for i in range(1, row):
        new_row = [current_row[j - 1] + current_row[j] for j in range(1, len(current_row))]
        current_row = [1] + new_row + [1]
    return current_row

def process_lines(lines, reversed=False):
    if reversed:
        lines = [[int(x) for x in line.split()[::-1]] for line in lines]
    else:
        lines = [list(map(int, line.split())) for line in lines]

    n = len(lines[0])
    values = get_pascal_triangle_row(n)

    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        for a, b in zip(line, values):
            r = a * b
            if add:
                total += r
            else:
                total -= r
            add = not add
    return total

def part1(text: str) -> int:
    lines = text.splitlines()
    return process_lines(lines)

def part2(text: str) -> int:
    lines = text.splitlines()
    return process_lines(lines, reversed=True)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()

sys.stdout.write(f"{part1(text)} {part2(text)}")