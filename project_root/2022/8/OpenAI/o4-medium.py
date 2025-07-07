import sys
data = [line.strip() for line in open(sys.argv[1])]
h = len(data); w = len(data[0])
grid = [list(map(int, row)) for row in data]
maxL = [[0]*w for _ in range(h)]; maxR = [[0]*w for _ in range(h)]
maxT = [[0]*w for _ in range(h)]; maxB = [[0]*w for _ in range(h)]
for y in range(h):
    m = -1
    for x in range(w):
        maxL[y][x] = m
        v = grid[y][x]
        if v > m: m = v
    m = -1
    for x in range(w-1, -1, -1):
        maxR[y][x] = m
        v = grid[y][x]
        if v > m: m = v
for x in range(w):
    m = -1
    for y in range(h):
        maxT[y][x] = m
        v = grid[y][x]
        if v > m: m = v
    m = -1
    for y in range(h-1, -1, -1):
        maxB[y][x] = m
        v = grid[y][x]
        if v > m: m = v
n = 2*(h+w-2)
for y in range(1, h-1):
    for x in range(1, w-1):
        t = grid[y][x]
        if t > min(maxL[y][x], maxR[y][x], maxT[y][x], maxB[y][x]):
            n += 1
DL = [[0]*w for _ in range(h)]; DR = [[0]*w for _ in range(h)]
DT = [[0]*w for _ in range(h)]; DB = [[0]*w for _ in range(h)]
for y in range(h):
    st = []
    for x in range(w):
        while st and grid[y][st[-1]] < grid[y][x]: st.pop()
        DL[y][x] = x if not st else x-st[-1]
        st.append(x)
    st = []
    for x in range(w-1, -1, -1):
        while st and grid[y][st[-1]] < grid[y][x]: st.pop()
        DR[y][x] = (w-1-x) if not st else st[-1]-x
        st.append(x)
for x in range(w):
    st = []
    for y in range(h):
        while st and grid[st[-1]][x] < grid[y][x]: st.pop()
        DT[y][x] = y if not st else y-st[-1]
        st.append(y)
    st = []
    for y in range(h-1, -1, -1):
        while st and grid[st[-1]][x] < grid[y][x]: st.pop()
        DB[y][x] = (h-1-y) if not st else st[-1]-y
        st.append(y)
s = 0
for y in range(1, h-1):
    for x in range(1, w-1):
        ss = DL[y][x]*DR[y][x]*DT[y][x]*DB[y][x]
        if ss > s: s = ss
sys.stdout.write(f"{n}\n{s}\n")