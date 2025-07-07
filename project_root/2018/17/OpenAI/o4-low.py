import sys

def parse_input(fn):
    x_min = y_min = float('inf')
    x_max = y_max = -float('inf')
    segments = []
    with open(fn) as f:
        for line in f:
            parts = line.strip().split(', ')
            d1, d2 = parts
            axis1, v1 = d1.split('=')
            axis2, v2 = d2.split('=')
            if '..' in v1:
                a, b = map(int, v1.split('..'))
                rng1 = (a, b)
            else:
                a = int(v1)
                rng1 = (a, a)
            a, b = map(int, v2.split('..'))
            rng2 = (a, b)
            if axis1 == 'x':
                x0, x1 = rng1; y0, y1 = rng2
            else:
                y0, y1 = rng1; x0, x1 = rng2
            x_min = min(x_min, x0)
            x_max = max(x_max, x1)
            y_min = min(y_min, y0)
            y_max = max(y_max, y1)
            segments.append((x0, x1, y0, y1))
    return segments, x_min, x_max, y_min, y_max

def build_ground(segments, x_min, x_max, y_max):
    width = x_max - x_min + 3
    height = y_max + 2
    g = [['.' for _ in range(width)] for _ in range(height)]
    for x0, x1, y0, y1 in segments:
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                g[y][x - x_min + 1] = '#'
    src = (0, 500 - x_min + 1)
    g[0][src[1]] = '+'
    return g, src

def waterfall(r, c, g):
    h = len(g)
    while r+1 < h and g[r+1][c] in '.':
        r += 1; g[r][c] = '|'
    if r+1 >= h or g[r+1][c] == '|':
        return None
    return (r, c)

def spread(r, c, g):
    out = []
    stack = [(r,c)]
    while stack:
        r, c = stack.pop()
        left = c
        while g[r][left-1] != '#' and g[r+1][left] in ('#','~'):
            left -= 1; g[r][left] = '|'
        right = c
        while g[r][right+1] != '#' and g[r+1][right] in ('#','~'):
            right += 1; g[r][right] = '|'
        if g[r][left-1] == '#' and g[r][right+1] == '#':
            for x in range(left, right+1):
                g[r][x] = '~'
            stack.append((r-1, c))
        else:
            if g[r][left-1] != '#':
                stack.append(fall(r, left-1, g))
            if g[r][right+1] != '#':
                stack.append(fall(r, right+1, g))
    return out

def fall(r, c, g):
    h = len(g)
    while r+1 < h and g[r+1][c] in ('.','|'):
        r += 1; g[r][c] = '|'
    if r+1 >= h or g[r+1][c] == '|':
        return None
    return (r, c)

if __name__ == "__main__":
    fn = sys.argv[1]
    seg, x0, x1, y0, y1 = parse_input(fn)
    ground, src = build_ground(seg, x0, x1, y1)
    cursors = [src]
    while cursors:
        cur = cursors.pop()
        nw = waterfall(*cur, ground)
        if not nw: continue
        spread_res = spread(*nw, ground)
        if spread_res:
            cursors.extend(spread_res)
    total = sum(ch in ('|','~') for row in ground[y0:] for ch in row)
    rested = sum(ch == '~' for row in ground[y0:] for ch in row)
    print(total, rested)