import sys

def get_pascal_triangle_row(row):
    current_row = [1]
    for i in range(1, row + 1):
        new_row = [1]
        prev_val = current_row[0]
        for j in range(1, i):
            current_val = current_row[j]
            new_row.append(prev_val + current_val)
            prev_val = current_val
        new_row.append(1)
        current_row = new_row
    return current_row

def part1(text: str) -> int:
    lines = [list(map(int, line.split())) for line in text.splitlines()]
    n = len(lines[0]) if lines else 0
    values = get_pascal_triangle_row(n)
    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        line_total = 0
        for a, b in zip(line, values):
            line_total += a * b if add else -a * b
            add = not add
        total += line_total
    return total

def part2(text: str) -> int:
    lines = [list(map(int, line.split()[::-1])) for line in text.splitlines()]
    n = len(lines[0]) if lines else 0
    values = get_pascal_triangle_row(n)
    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        line_total = 0
        for a, b in zip(line, values):
            line_total += a * b if add else -a * b
            add = not add
        total += line_total
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")