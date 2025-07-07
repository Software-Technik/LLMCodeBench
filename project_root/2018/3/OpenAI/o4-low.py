import sys

def extract_claims(lines):
    claims = []
    max_x = max_y = 0
    for line in lines:
        part1, _, rest = line.partition(" @ ")
        cid = part1[1:]
        coord, _, size = rest.partition(": ")
        x, y = map(int, coord.split(","))
        w, h = map(int, size.split("x"))
        claims.append((cid, x, y, w, h))
        max_x = max(max_x, x + w)
        max_y = max(max_y, y + h)
    return claims, max_x, max_y

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    claims, max_x, max_y = extract_claims(lines)
    grid = [[0]*max_y for _ in range(max_x)]
    for _, x, y, w, h in claims:
        for i in range(x, x+w):
            row = grid[i]
            for j in range(y, y+h):
                row[j] += 1
    overlap = sum(1 for i in range(max_x) for j in range(max_y) if grid[i][j] > 1)
    intact = None
    for cid, x, y, w, h in claims:
        ok = True
        for i in range(x, x+w):
            row = grid[i]
            for j in range(y, y+h):
                if row[j] > 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            intact = cid
            break
    sys.stdout.write(f"{overlap} {intact}")

if __name__ == "__main__":
    main()