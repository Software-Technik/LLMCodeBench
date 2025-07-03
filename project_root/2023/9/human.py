import sys

def get_pascal_triangle_row(row):
    current_row = [1]
    for i in range(1, row + 1):
        new_row = [1]
        for j in range(i - 1):
            a = current_row[j]
            b = current_row[j + 1]
            new_row.append(a + b)
        new_row.append(1)
        current_row = new_row
    return current_row


def part1(text: str) -> int:
    """
    The solutions follow a pattern found in the Pascal triangle,
    with each number alternating between adding and subtracting.
    This solves the problem in linear time.
    """
    lines = text.splitlines()
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

def part2(text: str) -> int:
    """Same as 09.py, but with the values reversed :shrug:"""
    lines = text.splitlines()
    lines = [list(map(int, line.split()[::-1])) for line in lines]

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




inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")