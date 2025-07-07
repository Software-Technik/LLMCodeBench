import re
import sys

def part1(data):
    return min(calc_possible_distances(data))

def part2(data):
    return max(calc_possible_distances(data))

def calc_possible_distances(data):
    locations = set()
    distances = {}

    for line in data:
        loc1, loc2, dist = re.findall(r"(.*?)\sto\s(.*?)\s=\s(\d+)", line)[0]
        locations.add(loc1)
        locations.add(loc2)
        dist = int(dist)
        distances[(loc1, loc2)] = dist
        distances[(loc2, loc1)] = dist

    locations = list(locations)
    n = len(locations)
    min_distance, max_distance = float('inf'), 0

    def permute(route, depth, current_distance):
        nonlocal min_distance, max_distance
        if depth == n:
            min_distance = min(min_distance, current_distance)
            max_distance = max(max_distance, current_distance)
            return
        for i in range(depth, n):
            locations[depth], locations[i] = locations[i], locations[depth]
            if depth > 0:
                next_dist = current_distance + distances[(route[depth - 1], locations[depth])]
            else:
                next_dist = current_distance
            permute(route, depth + 1, next_dist)
            locations[depth], locations[i] = locations[i], locations[depth]

    permute(locations, 0, 0)
    return min_distance, max_distance

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

min_dist, max_dist = calc_possible_distances(data)
sys.stdout.write(f"{min_dist}\n{max_dist}\n")