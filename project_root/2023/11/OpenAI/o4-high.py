import sys

def compute(positions, offset_rows, offset_cols, E):
    N = len(positions)
    new_y = [y + E * offset_rows[y] for y, x in positions]
    new_x = [x + E * offset_cols[x] for y, x in positions]
    new_y.sort()
    new_x.sort()
    total = 0
    for i, v in enumerate(new_y):
        total += v * (2 * i - N + 1)
    for i, v in enumerate(new_x):
        total += v * (2 * i - N + 1)
    return total

def main():
    text = open(sys.argv[1]).read()
    lines = text.strip().splitlines()
    H = len(lines)
    W = len(lines[0]) if H else 0
    positions = []
    row_count = [0] * H
    col_count = [0] * W
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "#":
                positions.append((y, x))
                row_count[y] += 1
                col_count[x] += 1
    offset_rows = [0] * H
    c = 0
    for i in range(H):
        offset_rows[i] = c
        if row_count[i] == 0:
            c += 1
    offset_cols = [0] * W
    c = 0
    for i in range(W):
        offset_cols[i] = c
        if col_count[i] == 0:
            c += 1
    p1 = compute(positions, offset_rows, offset_cols, 1)
    p2 = compute(positions, offset_rows, offset_cols, 999999)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()