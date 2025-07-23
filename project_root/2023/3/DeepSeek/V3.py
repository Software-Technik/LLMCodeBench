import sys

def has_adjacent_symbol(table, row, start, end):
    rows = len(table)
    cols = len(table[row]) if rows > 0 else 0
    
    # Check right
    if end + 1 < cols and table[row][end + 1] != '.':
        return True
    
    # Check left
    if start - 1 >= 0 and table[row][start - 1] != '.':
        return True
    
    # Check up and down
    for r in (row - 1, row + 1):
        if 0 <= r < rows:
            for i in range(max(0, start - 1), min(cols, end + 2)):
                c = table[r][i]
                if c != '.' and not c.isdigit():
                    return True
    return False

def part1(text):
    table = text.splitlines()
    total = 0
    for i, row in enumerate(table):
        number = ''
        for j, c in enumerate(row):
            if c.isdigit():
                number += c
                if j == len(row) - 1 and number:
                    start = j - len(number) + 1
                    if has_adjacent_symbol(table, i, start, j):
                        total += int(number)
            elif number:
                start = j - len(number)
                if has_adjacent_symbol(table, i, start, j - 1):
                    total += int(number)
                number = ''
    return total

def get_adjacent_numbers(table, numbers, row, col):
    adj = set()
    rows = len(table)
    cols = len(table[row]) if rows > 0 else 0
    
    # Left
    if col > 0:
        for s, e in numbers[row]:
            if col - 1 == e:
                adj.add((row, s, e))
                break
    
    # Right
    if col + 1 < cols:
        for s, e in numbers[row]:
            if col + 1 == s:
                adj.add((row, s, e))
                break
    
    # Up and Down
    for r in (row - 1, row + 1):
        if 0 <= r < rows:
            for i in range(max(0, col - 1), min(cols, col + 2)):
                if table[r][i].isdigit():
                    for s, e in numbers[r]:
                        if s <= i <= e:
                            adj.add((r, s, e))
                            break
    
    if len(adj) == 2:
        nums = [int(table[r][s:e+1]) for r, s, e in adj]
        return nums[0], nums[1]
    return None

def part2(text):
    table = text.splitlines()
    numbers = [[] for _ in range(len(table))]
    for i, row in enumerate(table):
        num = ''
        for j, c in enumerate(row):
            if c.isdigit():
                num += c
                if j == len(row) - 1 and num:
                    numbers[i].append((j - len(num) + 1, j))
            elif num:
                numbers[i].append((j - len(num), j - 1))
                num = ''
    
    total = 0
    for i, row in enumerate(table):
        for j, c in enumerate(row):
            if c == '*':
                adj_nums = get_adjacent_numbers(table, numbers, i, j)
                if adj_nums:
                    total += adj_nums[0] * adj_nums[1]
    return total

with open(sys.argv[1]) as f:
    text = f.read()
print(f"{part1(text)} {part2(text)}")