import sys

def parse(data):
    pairs = []
    for line in data:
        nums = list(map(int, line.replace("=", " ").replace(",", " ").replace(":", " ").split()))
        sx, sy, bx, by = nums[1], nums[3], nums[5], nums[7]
        d = abs(sx - bx) + abs(sy - by)
        pairs.append((sx, sy, bx, by, d))
    return pairs

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    cur_start, cur_end = ranges[0]
    total = 0
    for s, e in ranges[1:]:
        if s <= cur_end:
            if e > cur_end: cur_end = e
        else:
            total += cur_end - cur_start + 1
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    total += cur_end - cur_start + 1
    merged.append((cur_start, cur_end))
    return merged, total

def part1(pairs, n):
    target_y = 10 if n < 15 else 2000000
    ranges = []
    for sx, sy, bx, by, d in pairs:
        dy = abs(target_y - sy)
        dx = d - dy
        if dx >= 0:
            ranges.append((sx-dx, sx+dx))
    merged, total = merge_ranges(ranges)
    sensors = set(sx for sx, sy, bx, by, _ in pairs if sy == target_y and any(sx>=a and sx<=b for a,b in merged))
    beacons = set(bx for sx, sy, bx, by, _ in pairs if by == target_y and any(bx>=a and bx<=b for a,b in merged))
    return total - len(sensors) - len(beacons)

def part2(pairs, n):
    limit = 20 if n < 15 else 4000000
    for y in range(limit+1):
        ranges = []
        for sx, sy, bx, by, d in pairs:
            dy = abs(y - sy)
            dx = d - dy
            if dx >= 0:
                l = sx-dx
                r = sx+dx
                if r < 0 or l > limit: continue
                ranges.append((max(0, l), min(limit, r)))
        merged, _ = merge_ranges(ranges)
        if len(merged) > 1:
            x = merged[0][1] + 1
            return x * 4000000 + y

data = [line.strip() for line in open(sys.argv[1])]
pairs = parse(data)
n = len(data)
print(part1(pairs, n))
print(part2(pairs, n))