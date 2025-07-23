import sys

def parse_reindeers(data):
    return [{**{"index": i}, **dict(zip(["name", "speed", "fly_time", "rest_time"], [parts[0], int(parts[3]), int(parts[6]), int(parts[13])]))} for i, line in enumerate(data) for parts in [line.split()]]

def calculate_distance(reindeer, t):
    cycle_dist = reindeer["speed"] * reindeer["fly_time"]
    full_cycles = (t - reindeer["fly_time"]) // (reindeer["rest_time"] + reindeer["fly_time"])
    partial_cycle_left = max((t % (reindeer["rest_time"] + reindeer["fly_time"])) - reindeer["rest_time"], 0)
    return cycle_dist * full_cycles + min(partial_cycle_left, reindeer["speed"]) * reindeer["fly_time"]

def part1(data):
    t = 2503 if len(data) > 2 else 1000
    distances = [calculate_distance(reindeer, t) for reindeer in parse_reindeers(data)]
    return max(distances)

def part2(data):
    t = 2503 if len(data) > 2 else 1000
    scores = [0] * len(parse_reindeers(data))
    for s in range(1, t + 1):
        distances = [(reindeer["speed"] * min((s % (reindeer["rest_time"] + reindeer["fly_time"])), reindeer["fly_time"]), reindeer["index"]) for reindeer in parse_reindeers(data)]
        max_dist = max(distances)
        for _, index in filter(lambda d: d[0] == max_dist[0], distances):
            scores[index] += 1
    return max(scores)

input_strings = sys.argv[1]
with open(input_strings) as f:
   data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}")