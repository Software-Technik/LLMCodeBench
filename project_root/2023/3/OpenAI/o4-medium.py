import sys
table = open(sys.argv[1]).read().splitlines()
nrows = len(table)
segments = []
num_id = []
for i, row in enumerate(table):
    ids = [-1] * len(row)
    j = 0
    while j < len(row):
        if row[j].isdigit():
            start = j
            while j < len(row) and row[j].isdigit():
                j += 1
            end = j - 1
            val = int(row[start:j])
            seg_idx = len(segments)
            segments.append((i, start, end, val))
            for k in range(start, end + 1):
                ids[k] = seg_idx
        else:
            j += 1
    num_id.append(ids)
total1 = 0
for r, start, end, val in segments:
    found = False
    if end + 1 < len(table[r]) and table[r][end + 1] != '.':
        found = True
    elif start - 1 >= 0 and table[r][start - 1] != '.':
        found = True
    elif r > 0:
        for c in range(start, end + 1):
            ch = table[r - 1][c]
            if ch != '.' and not ch.isdigit():
                found = True
                break
    if not found and r + 1 < nrows:
        for c in range(start, end + 1):
            ch = table[r + 1][c]
            if ch != '.' and not ch.isdigit():
                found = True
                break
    if found:
        total1 += val
total2 = 0
for i, row in enumerate(table):
    for j, ch in enumerate(row):
        if ch == '*':
            adj = set()
            left_limit = j
            right_limit = j
            if j > 0:
                sid = num_id[i][j - 1]
                if sid >= 0 and segments[sid][2] == j - 1:
                    adj.add(sid)
                    left_limit = j - 1
            if j + 1 < len(row):
                sid = num_id[i][j + 1]
                if sid >= 0 and segments[sid][1] == j + 1:
                    adj.add(sid)
                    right_limit = j + 1
            if i > 0:
                for c in range(left_limit, right_limit + 1):
                    if 0 <= c < len(table[i - 1]):
                        sid = num_id[i - 1][c]
                        if sid >= 0:
                            adj.add(sid)
            if i + 1 < nrows:
                for c in range(left_limit, right_limit + 1):
                    if 0 <= c < len(table[i + 1]):
                        sid = num_id[i + 1][c]
                        if sid >= 0:
                            adj.add(sid)
            if len(adj) == 2:
                a, b = adj
                total2 += segments[a][3] * segments[b][3]
sys.stdout.write(f"{total1} {total2}")