def has_adjacent_symbol(table, row, start, end):
    if end < len(table[row]) - 1 and table[row][end + 1] != '.':
        return True
    if start > 0 and table[row][start - 1] != '.':
        return True
    if row > 0:
        line = table[row - 1]
        for i in range(max(start - 1, 0), min(end + 2, len(line))):
            if line[i] != '.' and not line[i].isdigit():
                return True
    if row < len(table) - 1:
        line = table[row + 1]
        for i in range(max(start - 1, 0), min(end + 2, len(line))):
            if line[i] != '.' and not line[i].isdigit():
                return True
    return False

def part1(text):
    total = 0
    table = text.splitlines()
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
                if (j == len(row) - 1 or not row[j + 1].isdigit()) and has_adjacent_symbol(table, i, j - len(number) + 1, j):
                    total += int(number)
                    number = ""
    return total

def get_adjacent_numbers(table, numbers, row, col):
    adjacent_numbers = set()
    for r in range(max(0, row - 1), min(row + 2, len(table))):
        if r == row:
            start, end = col - 1, col + 1
        else:
            start, end = max(col - 1, 0), min(len(table[r]) - 1, col) + 1

        for s, e in numbers[r]:
            if start <= e or end >= s:
                adjacent_numbers.add(int(table[r][s:e+1]))

        if len(adjacent_numbers) == 2:
            return list(adjacent_numbers)
    return None

def part2(text):
    table = text.splitlines()
    numbers = [[] for _ in range(len(table))]
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
            elif number:
                numbers[i].append([j - len(number), j - 1])
                number = ""

    total = 0
    for i, row in enumerate(table):
        for j, c in enumerate(row):
            if c == '*' and (adjacent_numbers := get_adjacent_numbers(table, numbers, i, j)):
                total += adjacent_numbers[0] * adjacent_numbers[1]

    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")