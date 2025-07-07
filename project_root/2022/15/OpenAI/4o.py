import sys

def part1(data):
    pairs = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
    target_y = 10 if pairs[0] == ((2, 18), (-2, 15)) else 2000000

    x_ranges = []
    for pair in pairs:
        distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        diff_x = distance - abs(target_y - pair[0][1])
        if diff_x >= 0:
            x_ranges.append((pair[0][0] - diff_x, pair[0][0] + diff_x))

    x_ranges.sort()

    coverage_start, coverage_end = x_ranges[0]
    empty = 0
    for start, end in x_ranges[1:]:
        if start <= coverage_end:
            coverage_end = max(coverage_end, end)
        else:
            empty += start - coverage_end - 1
            coverage_start, coverage_end = start, end

    num_sensors = len(set(sensor[0] for sensor, beacon in pairs if sensor[1] == target_y and coverage_start <= sensor[0] <= coverage_end))
    num_beacons = len(set(beacon[0] for sensor, beacon in pairs if beacon[1] == target_y and coverage_start <= beacon[0] <= coverage_end))

    return (coverage_end - coverage_start + 1) - num_sensors - num_beacons - empty

def part2(data):
    pairs_temp = [tuple(map(lambda item: tuple(map(lambda x: int(x[2:]), item.replace(",", "").split()[-2:])), line.split(": "))) for line in data]
    pairs = [(sensor, beacon, abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])) for sensor, beacon in pairs_temp]
    target_ys = 20 if pairs[0][:2] == ((2, 18), (-2, 15)) else 4000000

    for target_y in range(target_ys + 1):
        x_ranges = []
        for sensor, _, distance in pairs:
            diff_x = distance - abs(target_y - sensor[1])
            if diff_x >= 0:
                x_ranges.append((sensor[0] - diff_x, sensor[0] + diff_x))

        x_ranges.sort()

        coverage_start, coverage_end = x_ranges[0]
        for start, end in x_ranges[1:]:
            if start <= coverage_end:
                coverage_end = max(coverage_end, end)
            else:
                return (coverage_end + 1) * 4000000 + target_y
            
input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")