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
        locations.update([loc1, loc2])
        distances[(loc1, loc2)] = distances[(loc2, loc1)] = int(dist)

    locations = list(locations)
    travel_distances = []
    for route in permutations(locations):
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[(route[i], route[i + 1])]
        travel_distances.append(distance)
    return travel_distances

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")