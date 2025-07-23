import sys
from collections import deque
import networkx as nx

def part1(data):
    valves, move_cost = parse_data(data)
    most_pressure = 0
    queue = deque([("AA", 30, 0, frozenset())])
    while queue:
        location, time_left, pressure, opened = queue.pop()
        if pressure > most_pressure:
            most_pressure = pressure
        if time_left <= 0:
            continue
        for np in valves:
            if np in opened:
                continue
            cost_time = move_cost[(location, np)]
            new_time = time_left - cost_time - 1
            if new_time <= 0:
                continue
            new_pressure = pressure + new_time * valves[np]
            new_opened = opened | {np}
            remaining_valves = [v for v in valves if v not in new_opened]
            remaining_pressure = sum((new_time - 2) * valves[v] for v in remaining_valves)
            if remaining_pressure + new_pressure < most_pressure:
                continue
            queue.append((np, new_time, new_pressure, new_opened))
    return most_pressure

def part2(data):
    valves, move_cost = parse_data(data)
    most_pressure = 0
    queue = deque([(frozenset(), (26, "AA"), (26, "AA"), 0)])
    while queue:
        opened, (time1, loc1), (time2, loc2), pressure = queue.pop()
        if pressure > most_pressure:
            most_pressure = pressure
        if time1 <= 0 and time2 <= 0:
            continue
        if time1 > time2:
            time, loc, other_time, other_loc = time1, loc1, time2, loc2
        else:
            time, loc, other_time, other_loc = time2, loc2, time1, loc1
        for np in valves:
            if np in opened:
                continue
            cost_time = move_cost[(loc, np)]
            new_time = time - cost_time - 1
            if new_time <= 0:
                continue
            new_pressure = pressure + new_time * valves[np]
            new_opened = opened | {np}
            remaining_valves = [v for v in valves if v not in new_opened]
            remaining_pressure = sum((new_time - 2) * valves[v] for v in remaining_valves)
            if remaining_pressure + new_pressure < most_pressure:
                continue
            if time1 > time2:
                queue.append((new_opened, (new_time, np), (other_time, other_loc), new_pressure))
            else:
                queue.append((new_opened, (other_time, other_loc), (new_time, np), new_pressure))
    return most_pressure

def parse_data(data):
    valves = {}
    move_cost = {}
    g = nx.Graph()
    for line in data:
        tmp1, tmp2 = line.split("; ")
        tmp3 = tmp1.split(" ")
        valve = tmp3[1]
        rate = int(tmp3[-1].split("=")[1])
        to = [i.replace(",", "") for i in tmp2.split(" ")[4:]]
        if rate > 0:
            valves[valve] = rate
        for v in to:
            g.add_edge(valve, v)
    temp = ["AA"] + list(valves.keys())
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            v1 = temp[i]
            v2 = temp[j]
            t = nx.shortest_path_length(g, v1, v2)
            move_cost[(v1, v2)] = move_cost[(v2, v1)] = t
    return valves, move_cost

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")