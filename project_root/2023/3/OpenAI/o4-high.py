import sys
with open(sys.argv[1]) as f: rows = f.read().splitlines()
H = len(rows)
prefix = [None] * H
for i, row in enumerate(rows):
    M = len(row)
    P = [0] * (M + 1)
    for j, ch in enumerate(row):
        P[j+1] = P[j] + (ch!='.' and not('0'<=ch<='9'))
    prefix[i] = P
part1 = 0
numbers_idx_map = [None] * H
numbers_values = [None] * H
for i, row in enumerate(rows):
    M = len(row)
    idx_map = [-1] * M
    values = []
    j = 0
    while j < M:
        ch = row[j]
        if '0'<=ch<='9':
            start = j
            j += 1
            while j < M and '0'<=row[j]<='9':
                j += 1
            end = j - 1
            v = int(row[start:j])
            k = len(values)
            values.append(v)
            for x in range(start, end+1):
                idx_map[x] = k
            hor = False
            if end+1 < M and row[end+1] != '.':
                hor = True
            elif start > 0 and row[start-1] != '.':
                hor = True
            if not hor:
                if i > 0 and prefix[i-1][end+1] - prefix[i-1][start] > 0:
                    hor = True
                elif i+1 < H and prefix[i+1][end+1] - prefix[i+1][start] > 0:
                    hor = True
            if hor:
                part1 += v
        else:
            j += 1
    numbers_idx_map[i] = idx_map
    numbers_values[i] = values
del prefix
part2 = 0
for i, row in enumerate(rows):
    M = len(row)
    idx_map = numbers_idx_map[i]
    for j, ch in enumerate(row):
        if ch == '*':
            found = set()
            left = j
            right = j
            if j+1 < M:
                k = idx_map[j+1]
                if k >= 0:
                    found.add((i, k))
                    right = j+1
            if j > 0:
                k = idx_map[j-1]
                if k >= 0:
                    found.add((i, k))
                    left = j-1
            if i > 0:
                idx_up = numbers_idx_map[i-1]
                for x in range(left, right+1):
                    k = idx_up[x]
                    if k >= 0:
                        found.add((i-1, k))
            if i+1 < H:
                idx_dn = numbers_idx_map[i+1]
                for x in range(left, right+1):
                    k = idx_dn[x]
                    if k >= 0:
                        found.add((i+1, k))
            if len(found) == 2:
                it = iter(found)
                i1, k1 = next(it)
                i2, k2 = next(it)
                part2 += numbers_values[i1][k1] * numbers_values[i2][k2]
sys.stdout.write(f"{part1} {part2}")