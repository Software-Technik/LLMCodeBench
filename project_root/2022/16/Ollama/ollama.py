import networkx as nx
from collections import deque

def part1(data):
    valves, move_cost = parse_data(data)
    most_pressure, queue = 0, deque([("AA", 30, 0)])
    seen = set()

    while queue:
        location, time_left, pressure = queue.pop()
        if (location, time_left) in seen: continue
        seen.add((location, time_left))

        if pressure > most_pressure:
            most_pressure = pressure

        if time_left <= 0: continue

        next_pos = [i for i in valves]
        for np in next_pos:
            cost_time = move_cost[(location, np)]
            flow_rate = valves[np]

            if (time_left - cost_time - 1) * flow_rate <= 0: continue
            current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate
            remaining_pressure = sum((max(0, time_left - nx.shortest_path_length(nx.Graph(move_cost), location, i) - 2)) * valves[i] for i in [j for j in valves if move_cost.get(j) > nx.shortest_path_length(nx.Graph(move_cost), np, j)])
            if remaining_pressure + current_total_pressure < most_pressure: continue

            queue.append((np, time_left - cost_time - 1, current_total_pressure))

    return most_pressure

def part2(data):
    valves, move_cost = parse_data(data)
    most_pressure, queue = 0, deque([("", "AA", 26, 0)])
    seen = set()

    while queue:
        path, location, time_left, pressure = queue.pop()
        if (path + f"({location},{time_left})") in seen: continue
        seen.add(path + f"({location},{time_left})")

        if pressure > most_pressure:
            most_pressure = pressure

        if time_left <= 0: continue

        next_pos = [i for i in valves]
        for np in next_pos + ["AA"]:
            cost_time = move_cost[(location, np)]
            flow_rate = valves.get(np, 0)

            if (time_left - cost_time - 1) * flow_rate <= 0: continue
            current_total_pressure = pressure + (time_left - cost_time - 1) * flow_rate

            queue.append((path+np+"=>", np, time_left - cost_time - 1, current_total_pressure))

    return most_pressure

def parse_data(data):
    valves, g = {}, nx.Graph()

    for line in data:
        tmp1, tmp2 = line.split("; ")
        valve = tmp1.split(" ")[1]
        rate = int(tmp1.split("=")[-1])
        to = [i.replace(",", "") for i in tmp2.split("tunnels lead to valves ")[-1].split(" ")]

        if rate > 0:
            valves[valve] = rate

        g.add_node(valve)

    nx.set_edge_attributes(g, {e: abs(len(nx.shortest_path(graph=g.source, target=e))) for e in g.edges(data=nx.all_pairs_dijkstra_path_length(G))})
    move_cost = dict((nx.get_node_attributes(g, 'distance')[edge]))
    return valves, move_cost

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")