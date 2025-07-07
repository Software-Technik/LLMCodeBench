import sys
with open(sys.argv[1]) as f: lines = f.read().splitlines()
rock = set(); maxy = 0
for line in lines:
    parts = line.split(' -> ')
    x1,y1 = map(int, parts[0].split(','))
    if y1 > maxy: maxy = y1
    for t in parts[1:]:
        x2,y2 = map(int, t.split(','))
        if y2 > maxy: maxy = y2
        if x1 == x2:
            if y1 > y2: y1,y2 = y2,y1
            for y in range(y1, y2+1): rock.add((x1,y))
        else:
            if x1 > x2: x1,x2 = x2,x1
            for x in range(x1, x2+1): rock.add((x,y1))
        x1,y1 = x2,y2
sx,sy = 500,0
def part1():
    blocked = rock.copy(); cnt = 0; abyss = maxy
    while True:
        x,y = sx,sy
        while True:
            if y >= abyss: return cnt
            if (x,y+1) not in blocked:
                y += 1; continue
            if (x-1,y+1) not in blocked:
                x -= 1; y += 1; continue
            if (x+1,y+1) not in blocked:
                x += 1; y += 1; continue
            break
        blocked.add((x,y)); cnt += 1
def part2():
    blocked = rock.copy(); cnt = 0; floor = maxy + 2
    while (sx,sy) not in blocked:
        x,y = sx,sy
        while True:
            if y+1 < floor and (x,y+1) not in blocked:
                y += 1; continue
            if y+1 < floor and (x-1,y+1) not in blocked:
                x -= 1; y += 1; continue
            if y+1 < floor and (x+1,y+1) not in blocked:
                x += 1; y += 1; continue
            break
        blocked.add((x,y)); cnt += 1
    return cnt
print(part1(), part2(), sep='\n')