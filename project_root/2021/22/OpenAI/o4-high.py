import sys

def intersect(a, b):
    x1 = max(a[0], b[0]); x2 = min(a[1], b[1])
    if x1 > x2: return None
    y1 = max(a[2], b[2]); y2 = min(a[3], b[3])
    if y1 > y2: return None
    z1 = max(a[4], b[4]); z2 = min(a[5], b[5])
    if z1 > z2: return None
    return (x1, x2, y1, y2, z1, z2)

def compute(steps, limit):
    cubes = []
    for on, cube in steps:
        if limit:
            c = intersect(cube, limit)
            if not c: continue
        else:
            c = cube
        new = []
        for x1, x2, y1, y2, z1, z2, sign in cubes:
            inter = intersect((x1, x2, y1, y2, z1, z2), c)
            if inter:
                new.append((*inter, -sign))
        if on:
            new.append((*c, 1))
        cubes += new
    ans = 0
    for x1, x2, y1, y2, z1, z2, sign in cubes:
        ans += sign * (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return ans

def main():
    data = open(sys.argv[1]).read().splitlines()
    steps = []
    for line in data:
        op, rest = line.split(' ')
        on = op == 'on'
        xs, ys, zs = rest.split(',')
        x1, x2 = map(int, xs[2:].split('..'))
        y1, y2 = map(int, ys[2:].split('..'))
        z1, z2 = map(int, zs[2:].split('..'))
        steps.append((on, (x1, x2, y1, y2, z1, z2)))
    limit = (-50, 50, -50, 50, -50, 50)
    p1 = compute(steps, limit)
    p2 = compute(steps, None)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()