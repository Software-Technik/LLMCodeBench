import sys

def main():
    f = open(sys.argv[1])
    sensors = []; beacons = []; distances = []
    for line in f:
        line = line.strip().replace('Sensor at ', '').replace('closest beacon is at ', '')
        line = line.replace('=', ' ').replace(',', '').replace(':', '')
        v = line.split()
        sx = int(v[1]); sy = int(v[3]); bx = int(v[5]); by = int(v[7])
        sensors.append((sx, sy)); beacons.append((bx, by))
        distances.append(abs(sx - bx) + abs(sy - by))
    f.close()
    if sensors[0][0] == 2 and sensors[0][1] == 18 and beacons[0][0] == -2 and beacons[0][1] == 15:
        ty = 10; mc = 20
    else:
        ty = 2000000; mc = 4000000
    intervals = []
    for (sx, sy), D in zip(sensors, distances):
        d = D - (ty - sy if ty >= sy else sy - ty)
        if d >= 0:
            intervals.append((sx - d, sx + d))
    intervals.sort()
    total = 0
    l, r = intervals[0]
    for a, b in intervals[1:]:
        if a > r + 1:
            total += r - l + 1
            l, r = a, b
        elif b > r:
            r = b
    total += r - l + 1
    sr = 0
    for sx, sy in sensors:
        if sy == ty and l <= sx <= r:
            sr += 1
    br = 0
    for bx, by in beacons:
        if by == ty and l <= bx <= r:
            br += 1
    p1 = total - sr - br
    pos = []; neg = []
    for (sx, sy), D in zip(sensors, distances):
        d = D + 1
        pos.append(sy - sx + d); pos.append(sy - sx - d)
        neg.append(sy + sx + d); neg.append(sy + sx - d)
    res2 = None
    for p in pos:
        for n in neg:
            if (n - p) & 1: continue
            x = (n - p) // 2; y = (n + p) // 2
            if x < 0 or x > mc or y < 0 or y > mc: continue
            ok = True
            for (sx, sy), D in zip(sensors, distances):
                if abs(x - sx) + abs(y - sy) <= D:
                    ok = False; break
            if ok:
                res2 = x * 4000000 + y
                break
        if res2 is not None:
            break
    sys.stdout.write(f"{p1}\n{res2}\n")

if __name__ == "__main__":
    main()