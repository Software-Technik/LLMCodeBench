import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    claims = []
    max_x = max_y = 0
    for l in lines:
        p = l.split()
        cid = p[0][1:]
        x, y = map(int, p[2][:-1].split(','))
        w, h = map(int, p[3].split('x'))
        claims.append((cid, x, y, w, h))
        if x + w > max_x: max_x = x + w
        if y + h > max_y: max_y = y + h
    W, H = max_x, max_y
    counts = [0] * (W * H)
    overlaps = 0
    for _, x, y, w, h in claims:
        for dy in range(h):
            row = (y + dy) * W
            for dx in range(w):
                idx = row + x + dx
                if counts[idx] == 1:
                    overlaps += 1
                counts[idx] += 1
    intact = None
    for cid, x, y, w, h in claims:
        ok = True
        for dy in range(h):
            row = (y + dy) * W
            for dx in range(w):
                if counts[row + x + dx] > 1:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            intact = cid
            break
    sys.stdout.write(f"{overlaps} {intact}")

if __name__ == "__main__":
    main()