import sys
with open(sys.argv[1]) as f:
    s = f.readline().strip()
x = y = x0 = y0 = x1 = y1 = turn = 0
v1 = {(0, 0)}
v2 = {(0, 0)}
for c in s:
    if c == '^':
        y += 1
        if turn == 0:
            y0 += 1; v2.add((x0, y0))
        else:
            y1 += 1; v2.add((x1, y1))
    elif c == 'v':
        y -= 1
        if turn == 0:
            y0 -= 1; v2.add((x0, y0))
        else:
            y1 -= 1; v2.add((x1, y1))
    elif c == '>':
        x += 1
        if turn == 0:
            x0 += 1; v2.add((x0, y0))
        else:
            x1 += 1; v2.add((x1, y1))
    else:
        x -= 1
        if turn == 0:
            x0 -= 1; v2.add((x0, y0))
        else:
            x1 -= 1; v2.add((x1, y1))
    v1.add((x, y))
    turn ^= 1
sys.stdout.write(f"{len(v1)}\n{len(v2)}\n")