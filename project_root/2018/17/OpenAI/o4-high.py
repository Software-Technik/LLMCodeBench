import sys

def main():
    clay = set()
    xmin = 10**9; xmax = -10**9; ymin = 10**9; ymax = -10**9
    with open(sys.argv[1]) as f:
        for line in f:
            a, b = line.strip().split(', ')
            if a[0] == 'x':
                x = int(a[2:]); y0, y1 = map(int, b[2:].split('..'))
                for y in range(y0, y1+1): clay.add((x, y))
                xmin = min(xmin, x); xmax = max(xmax, x)
                ymin = min(ymin, y0); ymax = max(ymax, y1)
            else:
                y = int(a[2:]); x0, x1 = map(int, b[2:].split('..'))
                for x in range(x0, x1+1): clay.add((x, y))
                xmin = min(xmin, x0); xmax = max(xmax, x1)
                ymin = min(ymin, y); ymax = max(ymax, y)
    water = set(); settled = set(); stack = [(500, 0)]
    while stack:
        x, y = stack.pop()
        # fall
        while True:
            if y > ymax: break
            water.add((x, y))
            if (x, y+1) in clay or (x, y+1) in settled: break
            y += 1
        if y > ymax: continue
        # spread
        left = x
        while True:
            if (left-1, y) in clay:
                bound_left = True; break
            if (left, y+1) not in clay and (left, y+1) not in settled:
                bound_left = False; break
            left -= 1
        right = x
        while True:
            if (right+1, y) in clay:
                bound_right = True; break
            if (right, y+1) not in clay and (right, y+1) not in settled:
                bound_right = False; break
            right += 1
        if bound_left and bound_right:
            for xx in range(left, right+1): settled.add((xx, y))
            stack.append((x, y-1))
        else:
            for xx in range(left, right+1): water.add((xx, y))
            if not bound_left: stack.append((left, y))
            if not bound_right: stack.append((right, y))
    total = sum(1 for (_, y) in water if y >= ymin)
    total_settled = sum(1 for (_, y) in settled if y >= ymin)
    sys.stdout.write(f"{total} {total_settled}")

if __name__ == '__main__':
    main()