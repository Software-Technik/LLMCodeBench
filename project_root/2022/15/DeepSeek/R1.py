import sys

def main():
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]

    pairs = []
    for line in data:
        parts = line.split()
        s_x = int(parts[2][2:-1])
        s_y = int(parts[3][2:-1])
        b_x = int(parts[8][2:-1])
        b_y = int(parts[9][2:])
        sensor = (s_x, s_y)
        beacon = (b_x, b_y)
        distance = abs(s_x - b_x) + abs(s_y - b_y)
        pairs.append((sensor, beacon, distance))
    
    if pairs[0][0] == (2, 18) and pairs[0][1] == (-2, 15):
        target_y = 10
        target_ys = 20
    else:
        target_y = 2000000
        target_ys = 4000000

    x_ranges_p1 = []
    for (sensor, _, distance) in pairs:
        diff_x = distance - abs(target_y - sensor[1])
        if diff_x >= 0:
            x_min = sensor[0] - diff_x
            x_max = sensor[0] + diff_x
            x_ranges_p1.append((x_min, x_max))
    
    if not x_ranges_p1:
        total_covered = 0
    else:
        x_ranges_p1.sort()
        merged = []
        start, end = x_ranges_p1[0]
        for i in range(1, len(x_ranges_p1)):
            if x_ranges_p1[i][0] <= end + 1:
                end = max(end, x_ranges_p1[i][1])
            else:
                merged.append((start, end))
                start, end = x_ranges_p1[i]
        merged.append((start, end))
        total_covered = 0
        for inter in merged:
            total_covered += inter[1] - inter[0] + 1
        
    sensors_at_y = set()
    beacons_at_y = set()
    for (sensor, beacon, _) in pairs:
        if sensor[1] == target_y:
            sensors_at_y.add(sensor)
        if beacon[1] == target_y:
            beacons_at_y.add(beacon)
    
    count_sensors = 0
    for s in sensors_at_y:
        for inter in merged:
            if inter[0] <= s[0] <= inter[1]:
                count_sensors += 1
                break
    
    count_beacons = 0
    for b in beacons_at_y:
        for inter in merged:
            if inter[0] <= b[0] <= inter[1]:
                count_beacons += 1
                break
    
    part1_ans = total_covered - count_sensors - count_beacons

    part2_ans = None
    for y in range(target_ys + 1):
        x_ranges = []
        for (sensor, _, distance) in pairs:
            diff_x = distance - abs(y - sensor[1])
            if diff_x >= 0:
                x_min = sensor[0] - diff_x
                x_max = sensor[0] + diff_x
                if x_max < 0 or x_min > target_ys:
                    continue
                x_min = max(0, x_min)
                x_max = min(target_ys, x_max)
                x_ranges.append((x_min, x_max))
        
        if not x_ranges:
            continue
            
        x_ranges.sort()
        if x_ranges[0][0] > 0:
            part2_ans = y
            break
            
        coverage = x_ranges[0]
        found_gap = False
        for i in range(1, len(x_ranges)):
            if x_ranges[i][0] <= coverage[1] + 1:
                coverage = (coverage[0], max(coverage[1], x_ranges[i][1]))
            else:
                found_gap = True
                break
                
        if found_gap:
            part2_ans = (coverage[1] + 1) * 4000000 + y
            break
            
        if coverage[1] < target_ys:
            part2_ans = (coverage[1] + 1) * 4000000 + y
            break
            
    sys.stdout.write(f"{part1_ans}\n{part2_ans}\n")

if __name__ == "__main__":
    main()