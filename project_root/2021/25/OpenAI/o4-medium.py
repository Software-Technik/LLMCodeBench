import sys

def main():
    with open(sys.argv[1]) as f:
        lines = [line.rstrip('\n') for line in f]
    H = len(lines)
    W = len(lines[0])
    right = set()
    down = set()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == '>':
                right.add((i, j))
            elif ch == 'v':
                down.add((i, j))
    steps = 0
    while True:
        moved = False
        occ = right | down
        new_right = set()
        for i, j in right:
            ni, nj = i, (j + 1) % W
            if (ni, nj) not in occ:
                new_right.add((ni, nj))
                moved = True
            else:
                new_right.add((i, j))
        right = new_right
        occ = right | down
        new_down = set()
        for i, j in down:
            ni, nj = (i + 1) % H, j
            if (ni, nj) not in occ:
                new_down.add((ni, nj))
                moved = True
            else:
                new_down.add((i, j))
        down = new_down
        steps += 1
        if not moved:
            break
    sys.stdout.write(str(steps))

if __name__ == '__main__':
    main()