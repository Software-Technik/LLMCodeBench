import sys
from collections import deque
import networkx as nx

def bfs(valves, move_cost, start, total_time):
    n = len(valves)
    valve_list = list(valves.keys())
    valve_to_index = {valve: idx for idx, valve in enumerate(valve_list)}
    global_best = 0
    best_by_mask = {}
    cache = {}
    queue = deque()
    start_state = (start, total_time, 0, 0)
    queue.append(start_state)
    cache[(start, total_time, 0)] = 0
    
    while queue:
        current, time_left, mask, pressure = queue.pop()
        if pressure > best_by_mask.get(mask, -10**9):
            best_by_mask[mask] = pressure
        if pressure > global_best:
            global_best = pressure
        if time_left <= 0:
            continue
        for np in valve_list:
            if mask & (1 << valve_to_index[np]):
                continue
            cost = move_cost[(current, np)]
            if time_left - cost - 1 <= 0:
                continue
            new_time = time_left - cost - 1
            new_pressure = pressure + new_time * valves[np]
            new_mask = mask | (1 << valve_to_index[np])
            state_key = (np, new_time, new_mask)
            if state_key in cache and cache[state_key] >= new_pressure:
                continue
            remaining_valves = []
            for v in valve_list:
                if v == np:
                    continue
                if mask & (1 << valve_to_index[v]):
                    continue
                remaining_valves.append(v)
            remaining_pressure = 0
            for v in remaining_valves:
                remaining_pressure += (time_left - cost - 3) * valves[v]
            total_estimate = new_pressure + remaining_pressure
            if total_estimate < global_best:
                continue
            cache[state_key] = new_pressure
            queue.append((np, new_time, new_mask, new_pressure))
    return best_by_mask

def part1(data):
    valves, move_cost = parse_data(data)
    best_by_mask = bfs(valves, move_cost, "AA", 30)
    return max(best_by_mask.values()) if best_by_mask else 0

def part2(data):
    valves, move_cost = parse_data(data)
    best_by_mask = bfs(valves, move_cost, "AA", 26)
    n = len(valves)
    if n == 0:
        return 0
    dp_arr = [-10**9] * (1 << n)
    for mask, value in best_by_mask.items():
        if value > dp_arr[mask]:
            dp_arr[mask] = value
    total_mask = (1 << n) - 1
    ans = 0
    for i in range(1 << n):
        if dp_arr[i] < 0:
            continue
        rest = total_mask ^ i
        j = rest
        while True:
            if dp_arr[j] >= 0:
                total_pressure = dp_arr[i] + dp_arr[j]
                if total_pressure > ans:
                    ans = total_pressure
            if j == 0:
                break
            j = (j - 1) & rest
    return ans

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
        for j in range(i+1, len(temp)):
            v1 = temp[i]
            v2 = temp[j]
            t = nx.shortest_path_length(g, v1, v2)
            move_cost[(v1, v2)] = t
            move_cost[(v2, v1)] = t
    return valves, move_cost

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")