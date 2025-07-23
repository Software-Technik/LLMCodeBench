import sys
import networkx as nx
from collections import defaultdict

def createLevelFrom(data):
    x, y = 0, 0
    level = dict()
    position = None
    for line in data:
        for c in line:
            if c == "@": 
                position = (x, y)
                level[(x, y)] = '.'
            else:
                level[(x, y)] = c
            x += 1
        x = 0
        y += 1
    return level, position

def createLevelFrom2(data):
    x, y = 0, 0
    level = dict()
    position = None
    for line in data:
        for c in line:
            if c == "@": 
                position = (x, y)
                level[(x, y)] = '.'
            else:
                level[(x, y)] = c
            x += 1
        x = 0
        y += 1

    level[position] = "#"
    level[(position[0] - 1, position[1])] = "#"
    level[(position[0] + 1, position[1])] = "#"
    level[(position[0], position[1] + 1)] = "#"
    level[(position[0], position[1] - 1)] = "#"

    positions = (
        (position[0] - 1, position[1] - 1),
        (position[0] - 1, position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 1, position[1] + 1),
    )
    return level, positions

def neighbors(level, p):
    x, y = p
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] 
            if (x + dx, y + dy) in level and level[(x + dx, y + dy)] != "#"]

def createGameFrom(level, position):
    spaces = set()
    keys = {}
    doors = {}
    curgraph = nx.Graph()

    for p in level:
        c = level[p]
        if c == "#": continue
        if c == ".": spaces.add(p)
        elif c.isupper(): doors[c.lower()] = p
        elif c.islower(): keys[c] = p
        label = "" if c == "." else c
        curgraph.add_node(p, pos=(p[0], -p[1]), label=label)

    for p in level:
        for n in neighbors(level, p):
            if n in curgraph.nodes() and p in curgraph.nodes():
                curgraph.add_edge(p, n, weight=1)

    keepgoing = True
    while keepgoing:
        keepgoing = False
        leaves = [x for x in curgraph.nodes() 
                 if x != position and len(list(curgraph.neighbors(x))) == 1]
        for leaf in leaves:
            c = level[leaf]
            if c == "." or c.isupper():
                keepgoing = True
                curgraph.remove_node(leaf)
                if c == ".": spaces.remove(leaf)
                else: del doors[c.lower()]

    keepgoing = True
    while keepgoing:
        keepgoing = False
        potentials = [x for x in curgraph.nodes() 
                     if len(list(curgraph.neighbors(x))) == 2]
        for pot in potentials:
            others = list(curgraph.neighbors(pot))
            if pot in spaces and len(others) == 2 and pot != position:
                weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
                curgraph.remove_node(pot)
                spaces.remove(pot)
                curgraph.add_edge(others[0], others[1], weight=weight)
    return curgraph, spaces, doors, keys

def part1(data):
    level, position = createLevelFrom(data)
    curgraph, spaces, doors, keys = createGameFrom(level, position)
    allkeys = frozenset(keys.keys())
    alldoors = frozenset(doors.keys())
    states = { (position, frozenset()): 0 }
    
    while True:
        newstates = {}
        for state in states:
            neededKeys = allkeys - state[1]
            closeddoors = alldoors - set(state[1])
            closeddoorspoints = {doors[k] for k in closeddoors}
            targets = [keys[k] for k in neededKeys]
            for t in targets:
                try:
                    weight, path = nx.single_source_dijkstra(curgraph, state[0], t, weight="weight")
                    if not set(path) & closeddoorspoints:
                        newcost = states[state] + weight
                        newpos = path[-1]
                        newkeys = frozenset(state[1] | {level[newpos]})
                        newstate = (newpos, newkeys)
                        if newstate in newstates:
                            if newcost < newstates[newstate]:
                                newstates[newstate] = newcost
                        else:
                            newstates[newstate] = newcost
                except nx.NetworkXNoPath:
                    continue
        states = newstates
        if any(s[1] == allkeys for s in states):
            break
    return min(states.values())

def createGameFrom2(level, positions):
    spaces = set()
    keys = {}
    doors = {}
    curgraph = nx.Graph()

    for p in level:
        c = level[p]
        if c == "#": continue
        if c == ".": spaces.add(p)
        elif c.isupper(): doors[c.lower()] = p
        elif c.islower(): keys[c] = p
        label = "" if c == "." else c
        curgraph.add_node(p, pos=(p[0], -p[1]), label=label)

    for p in level:
        for n in neighbors(level, p):
            if n in curgraph.nodes() and p in curgraph.nodes():
                curgraph.add_edge(p, n, weight=1)

    keepgoing = True
    while keepgoing:
        keepgoing = False
        leaves = [x for x in curgraph.nodes() 
                 if x not in positions and len(list(curgraph.neighbors(x))) == 1]
        for leaf in leaves:
            c = level[leaf]
            if c == "." or c.isupper():
                keepgoing = True
                curgraph.remove_node(leaf)
                if c == ".": spaces.remove(leaf)
                else: del doors[c.lower()]

    keepgoing = True
    while keepgoing:
        keepgoing = False
        potentials = [x for x in curgraph.nodes() 
                     if len(list(curgraph.neighbors(x))) == 2]
        for pot in potentials:
            others = list(curgraph.neighbors(pot))
            if pot in spaces and len(others) == 2 and pot not in positions:
                weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
                curgraph.remove_node(pot)
                spaces.remove(pot)
                curgraph.add_edge(others[0], others[1], weight=weight)
    return curgraph, spaces, doors, keys

def part2(data):
    level, positions = createLevelFrom2(data)
    curgraph, spaces, doors, keys = createGameFrom2(level, positions)
    allkeys = frozenset(keys.keys())
    alldoors = frozenset(doors.keys())
    states = { (positions, frozenset()): 0 }
    midx = min(x for x, _ in positions) + 1
    midy = min(y for _, y in positions) + 1
    
    while True:
        newstates = {}
        for state in states:
            neededKeys = allkeys - state[1]
            closeddoors = alldoors - set(state[1])
            closeddoorspoints = {doors[k] for k in closeddoors}
            for k in neededKeys:
                target = keys[k]
                if target[0] < midx and target[1] < midy: boti = 0
                elif target[0] < midx and target[1] > midy: boti = 1
                elif target[0] > midx and target[1] < midy: boti = 2
                elif target[0] > midx and target[1] > midy: boti = 3
                try:
                    weight, path = nx.single_source_dijkstra(curgraph, state[0][boti], target, weight="weight")
                    if set(path) & closeddoorspoints: continue
                    newcost = states[state] + weight
                    newpos = list(state[0])
                    newpos[boti] = path[-1]
                    newpos = tuple(newpos)
                    newkeys = frozenset(state[1] | {k})
                    newstate = (newpos, newkeys)
                    if newstate in newstates:
                        if newcost < newstates[newstate]:
                            newstates[newstate] = newcost
                    else:
                        newstates[newstate] = newcost
                except nx.NetworkXNoPath:
                    continue
        states = newstates
        if any(s[1] == allkeys for s in states):
            break
    return min(states.values())

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

print(f"{part1(data.copy())} {part2(data)}")