import sys

def parse_reindeers(data):
    lst = []
    for line in data:
        p = line.split()
        speed = int(p[3]); fly = int(p[6]); rest = int(p[13]); cycle = fly + rest
        lst.append((speed, fly, rest, cycle))
    return lst

def part1(reindeers):
    t = 1000 if len(reindeers) == 2 else 2503
    best = 0
    for s, f, r, c in reindeers:
        cycles = t // c
        rem = t % c
        dist = s * (cycles * f + min(f, rem))
        if dist > best: best = dist
    return best

def part2(reindeers):
    t = 1000 if len(reindeers) == 2 else 2503
    n = len(reindeers)
    scores = [0] * n
    for time in range(1, t + 1):
        dists = []
        for s, f, r, c in reindeers:
            cycles = time // c
            rem = time % c
            dists.append(s * (cycles * f + min(f, rem)))
        m = max(dists)
        for i, d in enumerate(dists):
            if d == m: scores[i] += 1
    return max(scores)

with open(sys.argv[1]) as f:
    data = [l.strip() for l in f]
r = parse_reindeers(data)
print(part1(r))
print(part2(r))