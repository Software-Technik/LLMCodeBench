import re
from itertools import permutations
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
        d = int(dist)
        if loc1 not in distances:
            distances[loc1] = {}
        distances[loc1][loc2] = d
        distances.setdefault(loc2, {})[loc1] = d

    possible_routes = list(permutations(locations))

    travel_distances = [sum(distances[a][b] for a, b in zip(route[:-1], route[1:])) for route in possible_routes]
    return travel_distances

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")