import sys

def distance_at_time(t, reindeer):
    speed = reindeer["speed"]
    fly_time = reindeer["fly_time"]
    rest_time = reindeer["rest_time"]
    cycle = fly_time + rest_time
    full_cycles = t // cycle
    remaining = t % cycle
    flying_in_remaining = min(remaining, fly_time)
    total_flying = full_cycles * fly_time + flying_in_remaining
    return speed * total_flying

def part1(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    return max(distance_at_time(t, r) for r in reindeers.values())

def part2(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    reindeer_list = list(reindeers.keys())
    scores = [0] * len(reindeer_list)
    for s in range(1, t + 1):
        distances = [distance_at_time(s, reindeers[name]) for name in reindeer_list]
        max_dist = max(distances)
        for i, d in enumerate(distances):
            if d == max_dist:
                scores[i] += 1
    return max(scores)

def parse_reindeers(data):
    reindeers = {}
    for line in data:
        parts = line.split()
        reindeers[parts[0]] = {"speed": int(parts[3]), "fly_time": int(parts[6]), "rest_time": int(parts[13])}
    return reindeers

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")