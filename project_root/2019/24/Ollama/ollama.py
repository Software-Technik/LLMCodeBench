import sys

def part1(data):
    level = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}
    layout = stringify(level)
    layouts = {layout}
    while True:
        txt = layout
        if txt in layouts: break
        layouts.add(txt)
        newlevel = {p: ("." if level[p] == "#" and sum(1 for n in neighbors(p, level) if level[n] == "#") != 1 else
                             "#" if level[p] == "." and (sum(1 for n in neighbors(p, level) if level[n] == "#") == 1 or
                                                         sum(1 for n in neighbors(p, level) if level[n] == "#") == 2)
                            else
                          level[p]) for p in level}
        layout = stringify(newlevel)
        level = newlevel

    power, result = 1, 0
    for x, y in sorted(level.keys()):
        if level[x, y] == "#": result += power
        power *= 2
    return result

def part2(data):
    levels = {0: {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}}
    empty_level = {(x, y): "." for y in range(5) for x in range(5)}
    empty_level[(2, 2)] = "?"

    for _ in range(200):
        newlevels = {}
        max_depth = len(levels)
        min_depth = -len(levels)
        for depth in range(min_depth, max_depth):
            if depth not in levels:
                levels[depth] = empty_level.copy()
            current_level = levels[depth]
            level_to_add = {p: ("#" if (current_level[p] == "." and (sum(1 for np in neighbors2(p, depth, current_level) if np == "#") == 1 or
                                                                      sum(1 for np in neighbors2(p, depth, current_level) if np == "#") == 2))
                              else ("." if current_level[p] == "#" and (
                                            sum(1 for np in neighbors2(p, depth, current_level) if np == "#")) != 1
                                    else current_level[p])) for p in current_level}

            newlevels[depth] = level_to_add

        levels = newlevels

    result = sum(
        [len([c for c in lvl.values() if c == "#"]) for dct in levels.values() for lvl in dct])
    return result

def stringify(level):
    return "".join(level.values())

def neighbors(p, level):
    for nx, ny in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)):
        if (nx, ny) in level: yield nx, ny

def neighbors2(p, depth, current_level):
    for nx, ny in ((p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)):
        if (depth + 1) in levels and p == (2, 1):
            yield "."  # Add 8 to A-E
        elif (depth + 1) in levels and p == (2, 3):
            yield "."  # Add 14 to E/J/O/T/Y
        elif p[0] != 4:
            for x in range(5): yield nx, ny

    if depth - 1 in levels:
        if depth %2:
            yield "." if sum([((n in current_level) or (0 <= n[0] < 5 and 0 <= n[1] < 5))
                     for n in ((p[0], p[1] + 1), (p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0] - 1, p[1]))]) <= 2
        else:
            yield "#"
    elif depth %2 and abs(depth) > len(levels):
        for x,y in levels[depth+1].keys(): yield ""
inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.rsplit() for line in f.read().splitlines()]

sys.stdout.write(f"{part1(data)}\n{part2(data)}")