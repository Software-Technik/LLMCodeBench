import sys

def parse_table(text):
    table = text.splitlines()
    numbers = [[] for _ in table]
    for r, row in enumerate(table):
        c = 0
        while c < len(row):
            if row[c].isdigit():
                start = c
                v = 0
                while c < len(row) and row[c].isdigit():
                    v = v * 10 + ord(row[c]) - 48
                    c += 1
                end = c - 1
                numbers[r].append((start, end, v))
            else:
                c += 1
    return table, numbers

def part1(table, numbers):
    total = 0
    H = len(table)
    W = len(table[0]) if H else 0
    for r, row_nums in enumerate(numbers):
        for start, end, v in row_nums:
            ok = False
            # left
            if start > 0 and table[r][start-1] != '.':
                ok = True
            # right
            if not ok and end+1 < W and table[r][end+1] != '.':
                ok = True
            # up
            if not ok and r > 0:
                for c in range(start, end+1):
                    ch = table[r-1][c]
                    if ch != '.' and not ch.isdigit():
                        ok = True
                        break
            # down
            if not ok and r+1 < H:
                for c in range(start, end+1):
                    ch = table[r+1][c]
                    if ch != '.' and not ch.isdigit():
                        ok = True
                        break
            if ok:
                total += v
    return total

def part2(table, numbers):
    total = 0
    H = len(table)
    W = len(table[0]) if H else 0
    for r, row in enumerate(table):
        for c, ch in enumerate(row):
            if ch == '*':
                s = set()
                # left
                if c>0:
                    for a,b,v in numbers[r]:
                        if a <= c-1 <= b:
                            s.add(v); break
                # right
                if c+1<W:
                    for a,b,v in numbers[r]:
                        if a <= c+1 <= b:
                            s.add(v); break
                # up
                if r>0:
                    for a,b,v in numbers[r-1]:
                        if a <= c <= b:
                            s.add(v); break
                # down
                if r+1<H:
                    for a,b,v in numbers[r+1]:
                        if a <= c <= b:
                            s.add(v); break
                if len(s)==2:
                    it = iter(s)
                    total += next(it)*next(it)
    return total

text = open(sys.argv[1]).read()
table, numbers = parse_table(text)
sys.stdout.write(f"{part1(table,numbers)} {part2(table,numbers)}")