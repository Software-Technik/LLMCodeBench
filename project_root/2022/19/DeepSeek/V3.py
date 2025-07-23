from collections import deque
from math import prod
import sys

def part1(data):
    blueprints = parse_data(data)
    r = run_blueprints(blueprints, 24)
    return sum((i + 1) * v for i, v in enumerate(r))

def part2(data):
    blueprints = parse_data(data)[:3]
    r = run_blueprints(blueprints, 32)
    return prod(r)

def parse_data(data):
    blueprints = []
    for line in data:
        items = line.split()
        bp = [
            (int(items[6]), 0, 0, 0),
            (int(items[12]), 0, 0, 0),
            (int(items[18]), int(items[21]), 0, 0),
            (int(items[27]), 0, int(items[30]), 0)
        ]
        blueprints.append(bp)
    return blueprints

def run_blueprints(blueprints, time):
    r = []
    for bp in blueprints:
        max_reserves = [max(i) * 2 for i in zip(*bp)]
        max_reserves[3] = float('inf')
        
        max_geodes = 0
        queue = deque()
        initial_state = (1, 0, 0, 0, 0, 0, 0, 0, time)
        queue.append(initial_state)
        seen = set()

        while queue:
            ore_r, clay_r, obs_r, geo_r, ore, clay, obs, geo, t = queue.popleft()
            
            if t == 0:
                if geo > max_geodes:
                    max_geodes = geo
                continue
            
            if geo > max_geodes:
                max_geodes = geo
            
            if geo + geo_r * t + t * (t - 1) // 2 <= max_geodes:
                continue
            
            key = (ore_r, clay_r, obs_r, geo_r, ore, clay, obs, geo, t)
            if key in seen:
                continue
            seen.add(key)
            
            new_ore = min(ore + ore_r, max_reserves[0])
            new_clay = min(clay + clay_r, max_reserves[1])
            new_obs = min(obs + obs_r, max_reserves[2])
            new_geo = geo + geo_r
            
            if ore >= bp[3][0] and obs >= bp[3][2]:
                queue.append((
                    ore_r, clay_r, obs_r, geo_r + 1,
                    new_ore - bp[3][0], new_clay, new_obs - bp[3][2], new_geo, t - 1
                ))
                continue
            
            if ore_r < max_reserves[0] and ore >= bp[0][0]:
                queue.append((
                    ore_r + 1, clay_r, obs_r, geo_r,
                    new_ore - bp[0][0], new_clay, new_obs, new_geo, t - 1
                ))
            
            if clay_r < max_reserves[1] and ore >= bp[1][0]:
                queue.append((
                    ore_r, clay_r + 1, obs_r, geo_r,
                    new_ore - bp[1][0], new_clay, new_obs, new_geo, t - 1
                ))
            
            if obs_r < max_reserves[2] and ore >= bp[2][0] and clay >= bp[2][1]:
                queue.append((
                    ore_r, clay_r, obs_r + 1, geo_r,
                    new_ore - bp[2][0], new_clay - bp[2][1], new_obs, new_geo, t - 1
                ))
            
            queue.append((
                ore_r, clay_r, obs_r, geo_r,
                new_ore, new_clay, new_obs, new_geo, t - 1
            ))
        
        r.append(max_geodes)
    return r

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")