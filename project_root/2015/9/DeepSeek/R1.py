import re
from itertools import permutations
import sys

min_ans = None
max_ans = None

def parse_data(data):
    locations = set()
    distances = {}
    for line in data:
        loc1, loc2, dist_str = re.findall(r"(.*?)\sto\s(.*?)\s=\s(\d+)", line)[0]
        dist = int(dist_str)
        locations.add(loc1)
        locations.add(loc2)
        distances[(loc1, loc2)] = dist
        distances[(loc2, loc1)] = dist
    return locations, distances

def min_max_distances(locations, distances):
    n = len(locations)
    min_val = float('inf')
    max_val = float('-inf')
    for route in permutations(locations):
        d = 0
        for i in range(n-1):
            d += distances[(route[i], route[i+1])]
        if d < min_val:
            min_val = d
        if d > max_val:
            max_val = d
    return min_val, max_val

def part1(data):
    global min_ans
    return min_ans

def part2(data):
    global max_ans
    return max_ans

if __name__ == '__main__':
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = [line.strip() for line in f]
    locations, distances = parse_data(data)
    min_ans, max_ans = min_max_distances(locations, distances)
    sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")