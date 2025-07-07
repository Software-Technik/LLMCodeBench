import sys

def get_pascal_triangle_row(row):
    current_row = [1]
    for _ in range(row):
        current_row = [1] + [current_row[j] + current_row[j + 1] for j in range(len(current_row) - 1)] + [1]
    return current_row

def compute(lines, values):
    total = 0
    for line in lines:
        add = len(line) % 2 != 0
        for a, b in zip(line, values):
            total += a * b if add else -a * b
            add = not add
    return total

def part1(text: str) -> int:
    lines = [list(map(int, line.split())) for line in text.splitlines()]
    values = get_pascal_triangle_row(len(lines[0]))
    return compute(lines, values)

def part2(text: str) -> int:
    lines = [list(map(int, line.split()))[::-1] for line in text.splitlines()]
    values = get_pascal_triangle_row(len(lines[0]))
    return compute(lines, values)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")