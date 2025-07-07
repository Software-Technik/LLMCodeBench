import sys
def main():
    s = open(sys.argv[1]).readline().strip()
    d = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    x = y = 0
    loc = {(0, 0)}
    for c in s:
        dx, dy = d[c]
        x += dx; y += dy
        loc.add((x, y))
    p1 = len(loc)
    loc = {(0, 0)}
    x0 = y0 = x1 = y1 = 0
    for i, c in enumerate(s):
        dx, dy = d[c]
        if i & 1:
            x1 += dx; y1 += dy
            loc.add((x1, y1))
        else:
            x0 += dx; y0 += dy
            loc.add((x0, y0))
    p2 = len(loc)
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()