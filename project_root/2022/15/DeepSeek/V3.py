import sys

def part1(data):
    pairs = []
    for line in data:
        parts = line.split(": ")
        sensor_part = parts[0].replace(",", "").split()[-2:]
        beacon_part = parts[1].replace(",", "").split()[-2:]
        sensor = (int(sensor_part[0][2:]), int(sensor_part[1][2:]))
        beacon = (int(beacon_part[0][2:]), int(beacon_part[1][2:]))
        pairs.append((sensor, beacon))
    
    target_y = 10 if pairs[0] == ((2, 18), (-2, 15)) else 2000000

    x_ranges = []
    for sensor, beacon in pairs:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        diff_x = distance - abs(target_y - sensor[1])
        if diff_x >= 0:
            x_ranges.append((sensor[0] - diff_x, sensor[0] + diff_x))

    x_ranges.sort()
    merged = [x_ranges[0]]
    for current in x_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    sensors_on_line = set()
    beacons_on_line = set()
    for sensor, beacon in pairs:
        if sensor[1] == target_y:
            for r in merged:
                if r[0] <= sensor[0] <= r[1]:
                    sensors_on_line.add(sensor)
                    break
        if beacon[1] == target_y:
            for r in merged:
                if r[0] <= beacon[0] <= r[1]:
                    beacons_on_line.add(beacon)
                    break

    total = 0
    for r in merged:
        total += r[1] - r[0] + 1
    return total - len(sensors_on_line) - len(beacons_on_line)

def part2(data):
    pairs = []
    for line in data:
        parts = line.split(": ")
        sensor_part = parts[0].replace(",", "").split()[-2:]
        beacon_part = parts[1].replace(",", "").split()[-2:]
        sensor = (int(sensor_part[0][2:]), int(sensor_part[1][2:]))
        beacon = (int(beacon_part[0][2:]), int(beacon_part[1][2:]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        pairs.append((sensor, beacon, distance))
    
    target_ys = 20 if pairs[0][0] == (2, 18) and pairs[0][1] == (-2, 15) else 4000000

    for target_y in range(0, target_ys + 1):
        x_ranges = []
        for sensor, _, distance in pairs:
            diff_x = distance - abs(target_y - sensor[1])
            if diff_x >= 0:
                x_ranges.append((sensor[0] - diff_x, sensor[0] + diff_x))
        
        x_ranges.sort()
        merged = [x_ranges[0]]
        for current in x_ranges[1:]:
            last = merged[-1]
            if current[0] <= last[1] + 1:
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                return (current[0] - 1) * 4000000 + target_y

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

print(part1(data))
print(part2(data))