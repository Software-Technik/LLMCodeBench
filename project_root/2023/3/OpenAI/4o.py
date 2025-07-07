import sys


def has_adjacent_symbol(table, row, start, end):
    right_check = end < len(table[row]) - 1 and table[row][end + 1] != "."
    left_check = start > 0 and table[row][start - 1] != "."
    up_check = row > 0 and any(
        table[row - 1][i] != "." and not table[row - 1][i].isdigit()
        for i in range(start, end + 1)
    )
    down_check = row < len(table) - 1 and any(
        table[row + 1][i] != "." and not table[row + 1][i].isdigit()
        for i in range(start, end + 1)
    )
    return right_check or left_check or up_check or down_check


def part1(text):
    table = text.splitlines()
    total = 0
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
            if not c.isdigit() or j == len(row) - 1:
                if number and has_adjacent_symbol(table, i, j - len(number), j - 1):
                    total += int(number)
                number = ""
    return total


def get_adjacent_numbers(table, numbers, row, col):
    adjacent_numbers = set()
    for start, end in numbers[row]:
        if col + 1 == start or col - 1 == end:
            adjacent_numbers.add((row, start, end))
    for delta_row, direction in [(-1, row > 0), (1, row < len(table) - 1)]:
        if direction:
            for i in range(col - 1, col + 2):
                if i >= 0 and i < len(table[row + delta_row]) and table[row + delta_row][i].isdigit():
                    for start, end in numbers[row + delta_row]:
                        if start <= i <= end:
                            adjacent_numbers.add((row + delta_row, start, end))
                            break
    if len(adjacent_numbers) == 2:
        return [int(table[r][s:e + 1]) for r, s, e in adjacent_numbers]
    return None


def part2(text):
    table = text.splitlines()
    numbers = [[] for _ in range(len(table))]
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
            else:
                if number:
                    numbers[i].append((j - len(number), j - 1))
                    number = ""
    total = 0
    for i, row in enumerate(table):
        for j, c in enumerate(row):
            if c == "*":
                adjacent_numbers = get_adjacent_numbers(table, numbers, i, j)
                if adjacent_numbers:
                    total += adjacent_numbers[0] * adjacent_numbers[1]
    return total


inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")