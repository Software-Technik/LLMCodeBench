import re, sys
clay = set()
min_x = min_y = float('inf')
max_x = max_y = float('-inf')
with open(sys.argv[1]) as f:
    for line in f:
        a, b = line.strip().split(', ')
        m1 = list(map(int, re.findall(r'-?\d+', a)))
        m2 = list(map(int, re.findall(r'-?\d+', b)))
        if a[0] == 'x':
            x = m1[0]
            for y in range(m2[0], m2[1]+1):
                clay.add((x, y))
        else:
            y = m1[0]
            for x in range(m2[0], m2[1]+1):
                clay.add((x, y))
        min_x = min(min_x, *(m1 if a[0]=='x' else m2))
        max_x = max(max_x, *(m1 if a[0]=='x' else m2))
        min_y = min(min_y, *(m2 if a[0]=='x' else m1))
        max_y = max(max_y, *(m2 if a[0]=='x' else m1))
flowing = set()
resting = set()
def scan_left(x, y):
    while True:
        if (x-1, y) in clay:
            return x-1, True
        if (x, y+1) not in clay and (x, y+1) not in resting:
            return x, False
        x -= 1
def scan_right(x, y):
    while True:
        if (x+1, y) in clay:
            return x+1, True
        if (x, y+1) not in clay and (x, y+1) not in resting:
            return x, False
        x += 1
stack = [(500, 0)]
while stack:
    x, y = stack.pop()
    if (x, y) in resting: continue
    if (x, y) in flowing: continue
    cy = y
    while cy <= max_y and (x, cy) not in clay and (x, cy) not in resting:
        flowing.add((x, cy))
        cy += 1
    if cy > max_y: continue
    if (x, cy) in clay or (x, cy) in resting:
        cy -= 1
        l, lw = scan_left(x, cy)
        r, rw = scan_right(x, cy)
        start = l+1 if lw else l
        end = r-1 if rw else r
        for xx in range(start, end+1):
            if lw and rw:
                resting.add((xx, cy))
            else:
                flowing.add((xx, cy))
        if lw and rw:
            stack.append((x, cy-1))
        else:
            if not lw:
                stack.append((l, cy))
            if not rw:
                stack.append((r, cy))
water = sum(1 for (x,y) in flowing|resting if y>=min_y)
retained = sum(1 for (x,y) in resting if y>=min_y)
sys.stdout.write(f"{water} {retained}")