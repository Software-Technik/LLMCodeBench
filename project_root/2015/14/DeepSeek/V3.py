import sys

def part1(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    max_dist = 0
    for r in reindeers.values():
        cycle = r["fly_time"] + r["rest_time"]
        full_cycles = t // cycle
        remaining = t % cycle
        distance = r["speed"] * (full_cycles * r["fly_time"] + min(remaining, r["fly_time"]))
        if distance > max_dist:
            max_dist = distance
    return max_dist

def part2(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    scores = [0] * len(reindeers)
    positions = [0] * len(reindeers)
    for s in range(1, t + 1):
        max_dist = 0
        for i, r in enumerate(reindeers.values()):
            cycle = r["fly_time"] + r["rest_time"]
            full_cycles = s // cycle
            remaining = s % cycle
            distance = r["speed"] * (full_cycles * r["fly_time"] + min(remaining, r["fly_time"]))
            positions[i] = distance
            if distance > max_dist:
                max_dist = distance
        for i in range(len(reindeers)):
            if positions[i] == max_dist:
                scores[i] += 1
    return max(scores)

def parse_reindeers(data):
    reindeers = {}
    for line in data:
        parts = line.split()
        reindeers[parts[0]] = {"speed": int(parts[3]), "fly_time": int(parts[6]), "rest_time": int(parts[13])}
    return reindeers

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")