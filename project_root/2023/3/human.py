import sys


def has_adjacent_symbol(table: list[str], row: int, start: int, end: int) -> bool:
    # Check right
    if end < len(table[row]) - 1:
        end += 1
        if table[row][end] != ".":
            return True

    # Check left
    if start > 0:
        start -= 1
        if table[row][start] != ".":
            return True

    # Check up
    if row > 0:
        for i in range(start, end + 1):
            char = table[row - 1][i]
            if char != "." and not char.isdigit():
                return True

    # Check down
    if row < len(table) - 1:
        for i in range(start, end + 1):
            char = table[row + 1][i]
            if char != "." and not char.isdigit():
                return True

    return False


def part1(text: str) -> int:
    table = text.splitlines()
    total = 0
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                # Collect all digits.
                number += c
                # If we're at the end of the row,
                # check if we have an adjacent symbol.
                is_end = j == len(row) - 1
                if is_end and has_adjacent_symbol(
                    table=table,
                    row=i,
                    start=j - len(number) + 1,
                    end=j,
                ):
                    total += int(number)
            # If we're at a symbol, and we have a number,
            # check if we have an adjacent symbol.
            elif number:
                if has_adjacent_symbol(
                    table=table,
                    row=i,
                    start=j - len(number),
                    end=j - 1,
                ):
                    total += int(number)
                number = ""
    return total

def get_adjacent_numbers(
    table: list[str], numbers: list[list[tuple[int, int]]], row: int, col: int
) -> tuple[int, int] | None:
    adjancent_numbers = set()
    left_limit = col
    right_limit = col

    # Check right
    if col < len(table[row]) - 1:
        for start, end in numbers[row]:
            if col + 1 == start:
                adjancent_numbers.add((row, start, end))
                break
        right_limit += 1

    # Check left
    if col > 0:
        for start, end in numbers[row]:
            if col - 1 == end:
                adjancent_numbers.add((row, start, end))
                break
        left_limit -= 1

    # Check up
    if row > 0:
        for i in range(left_limit, right_limit + 1):
            char = table[row - 1][i]
            if char.isdigit():
                for start, end in numbers[row - 1]:
                    if i >= start and i <= end:
                        adjancent_numbers.add((row - 1, start, end))
                        break

    # Check down
    if row < len(table) - 1:
        for i in range(left_limit, right_limit + 1):
            char = table[row + 1][i]
            if char.isdigit():
                for start, end in numbers[row + 1]:
                    if i >= start and i <= end:
                        adjancent_numbers.add((row + 1, start, end))
                        break

    if len(adjancent_numbers) == 2:
        result = [
            int(table[row][start : end + 1]) for row, start, end in adjancent_numbers
        ]
        return result[0], result[1]

    return None


def part2(text: str) -> int:
    table = text.splitlines()
    # Collect all numbers' positions.
    numbers = [[] for _ in range(len(table))]
    for i, row in enumerate(table):
        number = ""
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
                is_end = j == len(row) - 1
                if is_end:
                    numbers[i].append((j - len(number) + 1, j))
            elif number:
                numbers[i].append((j - len(number), j - 1))
                number = ""

    # Inspect each `*` symbol, and check if it has adjacent numbers.
    total = 0
    for i, row in enumerate(table):
        for j, c in enumerate(row):
            if c == "*":
                adjacent_numbers = get_adjacent_numbers(
                    table=table, numbers=numbers, row=i, col=j
                )
                if adjacent_numbers:
                    total += adjacent_numbers[0] * adjacent_numbers[1]

    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")