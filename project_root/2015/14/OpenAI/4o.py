import sys

def part1(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    return max(
        r["speed"] * (r["fly_time"] * (1 + ((t - r["fly_time"]) // (r["rest_time"] + r["fly_time"]))) + max(((t - r["fly_time"]) % (r["rest_time"] + r["fly_time"])) - r["rest_time"], 0))
        for r in reindeers.values()
    )

def part2(data):
    reindeers = parse_reindeers(data)
    t = 1000 if len(reindeers) == 2 else 2503
    scores = [0] * len(reindeers)
    
    for s in range(1, t + 1):
        max_dist = 0
        distances = []
        
        for r in reindeers.values():
            dist = r["speed"] * (r["fly_time"] * (1 + ((s - r["fly_time"]) // (r["rest_time"] + r["fly_time"]))) + max(((s - r["fly_time"]) % (r["rest_time"] + r["fly_time"])) - r["rest_time"], 0))
            distances.append(dist)
            max_dist = max(max_dist, dist)
        
        for i, dist in enumerate(distances):
            if dist == max_dist:
                scores[i] += 1

    return max(scores)

def parse_reindeers(data):
    return {
        parts[0]: {"speed": int(parts[3]), "fly_time": int(parts[6]), "rest_time": int(parts[13])}
        for parts in (line.split() for line in data)
    }

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")