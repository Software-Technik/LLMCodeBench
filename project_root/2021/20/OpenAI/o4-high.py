import sys
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
def enhance(lit, algo, times, min_r, max_r, min_c, max_c):
    fill = 0
    for _ in range(times):
        min_r -= 1; max_r += 1; min_c -= 1; max_c += 1
        new_lit = set()
        contains = lit.__contains__
        for r in range(min_r, max_r+1):
            for c in range(min_c, max_c+1):
                idx = 0
                for dr, dc in dirs:
                    idx = (idx << 1) | (fill ^ contains((r+dr, c+dc)))
                if algo[idx]:
                    new_lit.add((r, c))
        fill = algo[0] if fill == 0 else algo[511]
        lit = new_lit
    return len(lit)

def main():
    path = sys.argv[1]
    with open(path) as f:
        data = f.read().splitlines()
    algo = [1 if ch == '#' else 0 for ch in data[0]]
    lit0 = set()
    for r, line in enumerate(data[2:]):
        for c, ch in enumerate(line):
            if ch == '#':
                lit0.add((r, c))
    min_r = min(r for r, _ in lit0)
    max_r = max(r for r, _ in lit0)
    min_c = min(c for _, c in lit0)
    max_c = max(c for _, c in lit0)
    p1 = enhance(lit0.copy(), algo, 2, min_r, max_r, min_c, max_c)
    p2 = enhance(lit0.copy(), algo, 50, min_r, max_r, min_c, max_c)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()