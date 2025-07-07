import sys

def main():
    import sys
    grid = open(sys.argv[1]).read().splitlines()
    n = len(grid)
    locs = {}
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != '.':
                locs.setdefault(c, []).append((i, j))
    ant1 = set()
    ant2 = set()
    for lst in locs.values():
        L = len(lst)
        for i in range(L):
            ax, ay = lst[i]
            for j in range(i+1, L):
                bx, by = lst[j]
                dx = bx - ax; dy = by - ay
                cx, cy = ax - dx, ay - dy
                if 0 <= cx < n and 0 <= cy < n:
                    ant1.add((cx, cy))
                dx2, dy2 = bx + dx, by + dy
                if 0 <= dx2 < n and 0 <= dy2 < n:
                    ant1.add((dx2, dy2))
                k = 0
                while True:
                    x = ax - dx*k; y = ay - dy*k
                    if 0 <= x < n and 0 <= y < n:
                        ant2.add((x, y))
                        k += 1
                    else:
                        break
                k = 0
                while True:
                    x = bx + dx*k; y = by + dy*k
                    if 0 <= x < n and 0 <= y < n:
                        ant2.add((x, y))
                        k += 1
                    else:
                        break
    print(len(ant1), len(ant2))

if __name__ == "__main__":
    main()