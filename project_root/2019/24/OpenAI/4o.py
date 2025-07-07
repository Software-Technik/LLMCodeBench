import sys

def stringify(level):
    return ''.join(level.values())

def neighbors(level, p):
    x, y = p
    return [(nx, ny) for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if (nx, ny) in level]

def part1(data):
    level = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}
    
    layouts = set()
    while True:
        txt = stringify(level)
        if txt in layouts:
            break
        layouts.add(txt)
        
        newlevel = {}
        for p in level:
            bugcount = sum(1 for n in neighbors(level, p) if level[n] == '#')
            if level[p] == '#' and bugcount != 1:
                newlevel[p] = '.'
            elif level[p] == '.' and bugcount in (1, 2):
                newlevel[p] = '#'
            else:
                newlevel[p] = level[p]
        level = newlevel

    return sum(1 << (y * 5 + x) for (x, y), val in level.items() if val == '#')

def neighbors2(levels, rec, p):
    x, y = p
    current = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    if rec + 1 in levels:  # upper level
        if y == 0:
            current.append((2, 1))
        if y == 4:
            current.append((2, 3))
        if x == 0:
            current.append((1, 2))
        if x == 4:
            current.append((3, 2))
    
    if rec - 1 in levels:  # lower level
        if p == (2, 1):
            current.extend((i, 0) for i in range(5))
        if p == (1, 2):
            current.extend((0, i) for i in range(5))
        if p == (3, 2):
            current.extend((4, i) for i in range(5))
        if p == (2, 3):
            current.extend((i, 4) for i in range(5))
    
    return [levels[rec].get(np, '.') for np in current if np != (2, 2)]

def createlevel2(data):
    return {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}
  
def part2(data):
    levels = {0: createlevel2(data)}
    empty = createlevel2(['....', '....', '..?..', '....', '....'])

    for minutes in range(200):
        newlevels = {}
        for depth in range(-minutes-1, minutes+2):
            if depth not in levels:
                levels[depth] = empty.copy()

            newlevel = {}
            newlevels[depth] = newlevel
            for p in levels[depth]:
                bugcount = sum(1 for n in neighbors2(levels, depth, p) if n == '#')
                if levels[depth][p] == '#' and bugcount != 1:
                    newlevel[p] = '.'
                elif levels[depth][p] == '.' and bugcount in (1, 2):
                    newlevel[p] = '#'
                else:
                    newlevel[p] = levels[depth][p]
        levels = newlevels

    return sum(sum(1 for p in level if level[p] == '#') for level in levels.values())

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")