import sys

def stringify(level):
    return ''.join(level[(x, y)] for y in range(5) for x in range(5))

def part1(data):
    level = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            level[(x, y)] = c
    
    layouts = set()
    
    while True:
        txt = stringify(level)
        if txt in layouts:
            break
        layouts.add(txt)
        newlevel = {}
        for p in level:
            x, y = p
            ns = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                np = (x + dx, y + dy)
                if np in level:
                    ns.append(level[np])
            bugcount = ns.count('#')
            if level[p] == '#':
                newlevel[p] = '.' if bugcount != 1 else '#'
            else:
                newlevel[p] = '#' if bugcount in (1, 2) else '.'
        level = newlevel
    
    result = 0
    power = 1
    for y in range(5):
        for x in range(5):
            if level[(x, y)] == '#':
                result += power
            power <<= 1
    return result

def part2(data):
    levels = {0: {}}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            levels[0][(x, y)] = c
    
    empty = { (x, y): '.' for y in range(5) for x in range(5) }
    empty[(2, 2)] = '?'
    
    for _ in range(200):
        newlevels = {}
        min_depth = min(levels.keys()) - 1
        max_depth = max(levels.keys()) + 1
        
        for depth in range(min_depth, max_depth + 1):
            current = levels.get(depth, empty.copy())
            newlevel = {}
            newlevels[depth] = newlevel
            
            for p in current:
                if p == (2, 2):
                    newlevel[p] = '?'
                    continue
                
                x, y = p
                ns = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    np = (x + dx, y + dy)
                    if np in current:
                        if np != (2, 2):
                            ns.append(current[np])
                    elif depth + 1 in levels:
                        if np[0] < 0:
                            ns.append(levels[depth + 1][(1, 2)])
                        elif np[0] >= 5:
                            ns.append(levels[depth + 1][(3, 2)])
                        elif np[1] < 0:
                            ns.append(levels[depth + 1][(2, 1)])
                        elif np[1] >= 5:
                            ns.append(levels[depth + 1][(2, 3)])
                if depth - 1 in levels:
                    if p == (2, 1):
                        ns.extend(levels[depth - 1][(x, 0)] for x in range(5))
                    elif p == (2, 3):
                        ns.extend(levels[depth - 1][(x, 4)] for x in range(5))
                    elif p == (1, 2):
                        ns.extend(levels[depth - 1][(0, y)] for y in range(5))
                    elif p == (3, 2):
                        ns.extend(levels[depth - 1][(4, y)] for y in range(5))
                
                bugcount = ns.count('#')
                if current[p] == '#':
                    newlevel[p] = '.' if bugcount != 1 else '#'
                else:
                    newlevel[p] = '#' if bugcount in (1, 2) else '.'
        
        levels = newlevels
    
    return sum(1 for depth in levels for p in levels[depth] if levels[depth][p] == '#')

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

print(f"{part1(data)} {part2(data)}")