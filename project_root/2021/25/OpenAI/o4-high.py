import sys

def main():
    with open(sys.argv[1]) as f:
        lines = [line.rstrip() for line in f]
    h = len(lines)
    w = len(lines[0])
    east = {(r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == '>'}
    south = {(r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == 'v'}
    steps = 0
    while True:
        moved = False
        new_east = set()
        for r, c in east:
            nc = (c + 1) % w
            if (r, nc) not in east and (r, nc) not in south:
                new_east.add((r, nc))
                moved = True
            else:
                new_east.add((r, c))
        east = new_east
        new_south = set()
        for r, c in south:
            nr = (r + 1) % h
            if (nr, c) not in east and (nr, c) not in south:
                new_south.add((nr, c))
                moved = True
            else:
                new_south.add((r, c))
        south = new_south
        steps += 1
        if not moved:
            sys.stdout.write(str(steps))
            break

if __name__ == "__main__":
    main()