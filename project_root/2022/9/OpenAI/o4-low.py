import sys

def simulate(data, knots_num):
    dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
    knots = [[0, 0] for _ in range(knots_num)]
    seen = set()
    seen.add((0, 0))
    for d, cnt in data:
        dx0, dy0 = dirs[d]
        for _ in range(cnt):
            knots[0][0] += dx0; knots[0][1] += dy0
            for i in range(knots_num - 1):
                x0, y0 = knots[i]; x1, y1 = knots[i+1]
                w = x0 - x1; h = y0 - y1
                if abs(w) == 2 or abs(h) == 2:
                    knots[i+1][0] += (w > 0) - (w < 0)
                    knots[i+1][1] += (h > 0) - (h < 0)
            seen.add((knots[-1][0], knots[-1][1]))
    return len(seen)

with open(sys.argv[1]) as f:
    data = [(line[0], int(line[2:])) for line in f]
print(simulate(data, 2))
print(simulate(data, 10))