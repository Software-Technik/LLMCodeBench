import sys

def part1(data):
    pairs = [((int(line.split()[3].replace('x=', '')),
               int(line.split()[4][:-1].replace('y=', ''))),
              (int(line.split()[-3].replace('x=', '')),
               int(line.split()[-2][:-1].replace('y=', '')))) for line in data]
    target_y = 10 if pairs[0] == ((2, 18), (-2, 15)) else 2000000

    empty = set()
    sensors = (s[0][0] for s in pairs if s[0][1] == target_y)
    beacons = (b[0] for b in filter(lambda p: p[1][1] == (target_y,), pairs))
    num_sensors = len(set(sensors))
    num_beacons = len(set(beacons))

    x_ranges = sorted((x - abs(target_y - y) for (x, y), d in pairs))
    return sum(len(range(x_range[0], max(x_range[-1]) + 1)) for x_range in range(num_sensors)) - num_beacons - len(empty)

def part2(data):
    pairs = [(sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])) for sensor, beacon in [((int(line.split()[3].replace('x=', '')),
                int(line.split()[4][:-1].replace('y=', ''))),
              (int(line.split()[-3].replace('x=', '')),
               int(line.split()[-2][:-1].replace('y=', '')))) for line in data]]
    target_ys = 20 if pairs[0] == ((2, 18), (-2, 15)) else 4000000

    for y in range(target_ys+1):
        x_ranges = sorted((x - abs(y - sensor_y) for (sensor_x, _), d in filter(lambda p: p[0][1] == (y,), pairs)))
        if len(x_ranges):
            return next(sum([sum(r[0]) if i > 0 else sum(range(len(l[0]), l[-1][l]))] for r, l = x_range(sorted((x - abs(y-sensor_y) for p in p, pairs))))) - len(empty)

input_file: str = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")