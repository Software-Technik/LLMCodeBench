import sys
from array import array

def main():
    with open(sys.argv[1]) as f:
        data = [l.strip() for l in f if l.strip()]
    n = len(data)
    coords = [0] * (n * 4)
    m = 0
    j = 0
    for line in data:
        a, b = line.split(' -> ')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))
        coords[j] = x1; coords[j+1] = y1; coords[j+2] = x2; coords[j+3] = y2
        j += 4
        if x1 > m: m = x1
        if x2 > m: m = x2
        if y1 > m: m = y1
        if y2 > m: m = y2
    size = m + 1
    tot = size * size
    g1 = array('I', [0]) * tot
    g2 = array('I', [0]) * tot
    idx = 0
    for _ in range(n):
        x1, y1, x2, y2 = coords[idx], coords[idx+1], coords[idx+2], coords[idx+3]
        idx += 4
        dx = 1 if x2 > x1 else -1 if x2 < x1 else 0
        dy = 1 if y2 > y1 else -1 if y2 < y1 else 0
        steps = abs(x2 - x1) if dx else abs(y2 - y1)
        if dx == 0 or dy == 0:
            for i in range(steps + 1):
                p = (y1 + dy * i) * size + (x1 + dx * i)
                g1[p] += 1; g2[p] += 1
        else:
            for i in range(steps + 1):
                p = (y1 + dy * i) * size + (x1 + dx * i)
                g2[p] += 1
    c1 = c2 = 0
    for v1, v2 in zip(g1, g2):
        if v1 > 1: c1 += 1
        if v2 > 1: c2 += 1
    sys.stdout.write(f"{c1} {c2}")

if __name__ == '__main__':
    main()