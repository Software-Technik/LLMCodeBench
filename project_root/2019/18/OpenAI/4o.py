import sys
import networkx as nx

def createLevel(data, is_part2=False):
    x, y = 0, 0
    level = {}
    for line in data:
        for c in line:
            if c == "@":
                position = (x, y)
            level[(x, y)] = '.' if c == "@" else c
            x += 1
        x = 0
        y += 1
    if is_part2:
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
    return level, position

def neighbors(level, p):
    return [x for x in [
        (p[0] + 1, p[1]),
        (p[0] - 1, p[1]),
        (p[0], p[1] + 1),
        (p[0], p[1] - 1),
    ] if x in level and level[x] != "#"]

def createGame(level, positions):
    spaces, keys, doors = set(), {}, {}
    curgraph = nx.Graph()
    for p in level:
        if level[p] == "#": continue
        if level[p] == ".": spaces.add(p)
        if level[p].isupper(): doors[level[p].lower()] = p
        if level[p].islower(): keys[level[p]] = p
        curgraph.add_node(p, pos=(p[0], -p[1]))
    for p in level:
        for n in neighbors(level, p):
            if n in curgraph.nodes() and p in curgraph.nodes():
                curgraph.add_edge(p, n, weight=1)
    keepgoing = True
    while keepgoing:
        keepgoing = False
        leaves = [x for x in curgraph.nodes() if x not in positions and len(list(curgraph.neighbors(x))) == 1]
        for leaf in leaves:
            if level[leaf] in (".", level[leaf].isupper()):
                keepgoing = True
                curgraph.remove_node(leaf)
                if level[leaf] == ".": spaces.remove(leaf)
                else: del doors[level[leaf].lower()]
    potentials = [x for x in curgraph.nodes() if len(list(curgraph.neighbors(x))) == 2]
    for pot in potentials:
        others = list(curgraph.neighbors(pot))
        if pot in spaces and len(others) == 2 and pot not in positions:
            weight = curgraph.edges[others[0], pot]['weight'] + curgraph.edges[others[1], pot]['weight']
            curgraph.remove_node(pot)
            spaces.remove(pot)
            curgraph.add_edge(others[0], others[1], weight=weight)
    return curgraph, spaces, doors, keys

def solve(data, is_part2=False):
    level, positions = createLevel(data, is_part2)
    curgraph, spaces, doors, keys = createGame(level, positions if is_part2 else [positions])
    allkeys, alldoors = frozenset(keys.keys()), frozenset(doors.keys())
    states = { (tuple(positions) if is_part2 else positions, frozenset()): 0 }
    midx, midy = None, None
    if is_part2:
        midx = min([x for x, _ in positions]) + 1
        midy = min([y for _, y in positions]) + 1
    while True:
        newstates = {}
        for state in states:
            neededKeys = allkeys - state[1]
            closeddoors = alldoors - set(state[1])
            closeddoorspoints = {doors[k] for k in closeddoors}
            for target in [keys[k] for k in keys if k in neededKeys]:
                boti = 0
                if is_part2:
                    if target[0] < midx and target[1] < midy: boti = 0
                    elif target[0] < midx and target[1] > midy: boti = 1
                    elif target[0] > midx and target[1] < midy: boti = 2
                    elif target[0] > midx and target[1] > midy: boti = 3
                weight, path = nx.single_source_dijkstra(curgraph, state[0][boti] if is_part2 else state[0], target, weight="weight")
                if set(path) & closeddoorspoints: continue
                newcost = states[state] + weight
                if is_part2:
                    newpos = list(state[0])
                    newpos[boti] = path[-1]
                    newpos = tuple(newpos)
                else:
                    newpos = path[-1]
                newkeys = frozenset(state[1] | { level[path[-1]] })
                newstate = (newpos, newkeys)
                newstates[newstate] = min(newcost, newstates[newstate]) if newstate in newstates else newcost
        states = newstates
        if any(s[1] == allkeys for s in states): break
    return min(states.values())

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{solve(data.copy())} {solve(data, is_part2=True)}")