from collections import deque, defaultdict
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
        bp = [(int(items[6]), 0, 0, 0), (int(items[12]), 0, 0, 0), (int(items[18]), int(items[21]), 0, 0), (int(items[27]), 0, int(items[30]), 0)]
        blueprints.append(bp)
    return blueprints

def run_blueprints(blueprints, time):
    r = []
    for bp in blueprints:
        max_costs = [max(robot[i] for robot in bp) for i in range(4)]
        states = set()
        states.add(((1,0,0,0), (0,0,0,0)))
        max_geodes = 0
        
        for time_left in range(time, 0, -1):
            next_states = set()
            for (robots, resources) in states:
                ub = resources[3] + robots[3] * time_left + time_left*(time_left-1)//2
                if ub <= max_geodes:
                    continue
                    
                new_resources = (
                    min(resources[0] + robots[0], max_costs[0] * time_left),
                    min(resources[1] + robots[1], max_costs[1] * time_left),
                    min(resources[2] + robots[2], max_costs[2] * time_left),
                    resources[3] + robots[3]
                )
                next_states.add((robots, new_resources))
                
                if all(resources[i] >= bp[3][i] for i in range(4)):
                    new_r = (
                        min(resources[0] - bp[3][0] + robots[0], max_costs[0] * (time_left-1)),
                        min(resources[1] - bp[3][1] + robots[1], max_costs[1] * (time_left-1)),
                        min(resources[2] - bp[3][2] + robots[2], max_costs[2] * (time_left-1)),
                        resources[3] - bp[3][3] + robots[3]
                    )
                    new_robots = (robots[0], robots[1], robots[2], robots[3] + 1)
                    next_states.add((new_robots, new_r))
                    
                if robots[0] < max_costs[0] and all(resources[i] >= bp[0][i] for i in range(4)):
                    new_r = (
                        min(resources[0] - bp[0][0] + robots[0], max_costs[0] * (time_left-1)),
                        min(resources[1] - bp[0][1] + robots[1], max_costs[1] * (time_left-1)),
                        min(resources[2] - bp[0][2] + robots[2], max_costs[2] * (time_left-1)),
                        resources[3] - bp[0][3] + robots[3]
                    )
                    new_robots = (robots[0] + 1, robots[1], robots[2], robots[3])
                    next_states.add((new_robots, new_r))
                    
                if robots[1] < max_costs[1] and all(resources[i] >= bp[1][i] for i in range(4)):
                    new_r = (
                        min(resources[0] - bp[1][0] + robots[0], max_costs[0] * (time_left-1)),
                        min(resources[1] - bp[1][1] + robots[1], max_costs[1] * (time_left-1)),
                        min(resources[2] - bp[1][2] + robots[2], max_costs[2] * (time_left-1)),
                        resources[3] - bp[1][3] + robots[3]
                    )
                    new_robots = (robots[0], robots[1] + 1, robots[2], robots[3])
                    next_states.add((new_robots, new_r))
                    
                if robots[2] < max_costs[2] and all(resources[i] >= bp[2][i] for i in range(4)):
                    new_r = (
                        min(resources[0] - bp[2][0] + robots[0], max_costs[0] * (time_left-1)),
                        min(resources[1] - bp[2][1] + robots[1], max_costs[1] * (time_left-1)),
                        min(resources[2] - bp[2][2] + robots[2], max_costs[2] * (time_left-1)),
                        resources[3] - bp[2][3] + robots[3]
                    )
                    new_robots = (robots[0], robots[1], robots[2] + 1, robots[3])
                    next_states.add((new_robots, new_r))
                    
            states_dict = defaultdict(list)
            for s in next_states:
                robots, res = s
                states_dict[robots].append(res)
                
            next_states = set()
            for robots, res_list in states_dict.items():
                non_dominated = []
                for i in range(len(res_list)):
                    dominated = False
                    for j in range(len(res_list)):
                        if i == j:
                            continue
                        if all(res_list[j][k] >= res_list[i][k] for k in range(4)):
                            dominated = True
                            break
                    if not dominated:
                        non_dominated.append(res_list[i])
                for res in non_dominated:
                    next_states.add((robots, res))
                    
            states = next_states
            
        for (robots, resources) in states:
            if resources[3] > max_geodes:
                max_geodes = resources[3]
        r.append(max_geodes)
    return r

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")