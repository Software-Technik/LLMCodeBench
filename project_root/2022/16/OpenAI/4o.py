import sys
from collections import deque

def part1(data):
    valves, move_cost = parse_data(data)

    most_pressure = 0
    queue = deque([("AA", 30, 0, set())])
    while queue:
        location, time_left, pressure, history = queue.pop()

        if pressure > most_pressure:
            most_pressure = pressure

        if time_left <= 0:
            continue

        next_pos = (i for i in valves if i not in history)
        for np in next_pos:
            cost_time = move_cost[(location, np)]
            flow_rate = valves[np]
            current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate

            if current_total_pressure <= most_pressure:
                continue

            queue.append((np, time_left - cost_time - 1, current_total_pressure, history | {np}))

    return most_pressure

def part2(data):
    valves, move_cost = parse_data(data)

    most_pressure = 0
    queue = deque([([(26, "AA"), (26, "AA")], 0, set())])
    while queue:
        location_list, pressure, history = queue.pop()
        time_left, location = location_list.pop(0)

        if pressure > most_pressure:
            most_pressure = pressure

        if time_left <= 0:
            continue

        next_pos = (i for i in valves if i not in history)
        for np in next_pos:
            cost_time = move_cost[(location, np)]
            flow_rate = valves[np]
            next_location_list = location_list + [(time_left - cost_time - 1, np)]
            current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate

            if current_total_pressure <= most_pressure:
                continue

            queue.append((next_location_list, current_total_pressure, history | {np}))

    return most_pressure

def parse_data(data):
    valves = {}
    move_cost = {}
    connections = {}

    for line in data:
        tmp1, tmp2 = line.split("; ")
        tmp3 = tmp1.split(" ")
        valve = tmp3[1]
        rate = int(tmp3[-1].split("=")[1])
        to = [i.replace(",", "") for i in tmp2.split(" ")[4:]]

        if rate > 0:
            valves[valve] = rate

        connections[valve] = to

    temp = ["AA"] + list(valves.keys())
    for v1 in temp:
        for v2 in temp:
            if v1 != v2:
                move_cost[(v1, v2)] = bfs(v1, v2, connections)

    return valves, move_cost

def bfs(start, goal, connections):
    queue = deque([(start, 0)])
    seen = {start}
    
    while queue:
        current, distance = queue.popleft()
        
        if current == goal:
            return distance
        
        for neighbor in connections.get(current, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return float('inf')

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")