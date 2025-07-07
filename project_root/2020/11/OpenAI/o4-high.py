import sys
FL,EM,OC = 0,1,2
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def simulate(grid, neighbors, threshold):
    rows = len(grid); cols = len(grid[0]) if rows else 0
    cur = [row[:] for row in grid]
    while True:
        changed = False
        new = [row[:] for row in cur]
        for i in range(rows):
            for j in range(cols):
                v = cur[i][j]
                if v == FL: continue
                cnt = 0
                for a,b in neighbors[i][j]:
                    if cur[a][b] == OC:
                        cnt += 1
                        if cnt >= threshold: break
                if v == EM and cnt == 0:
                    new[i][j] = OC; changed = True
                elif v == OC and cnt >= threshold:
                    new[i][j] = EM; changed = True
        if not changed: break
        cur = new
    s = 0
    for row in cur:
        for cell in row:
            if cell == OC: s += 1
    return s

def main():
    with open(sys.argv[1]) as f:
        lines = [l.rstrip('\n') for l in f]
    rows = len(lines); cols = len(lines[0]) if rows else 0
    grid = [[FL if c == '.' else EM for c in line] for line in lines]
    neighbors1 = [[[] for _ in range(cols)] for _ in range(rows)]
    neighbors2 = [[[] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == FL: continue
            for dy,dx in dirs:
                ni = i + dy; nj = j + dx
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != FL:
                    neighbors1[i][j].append((ni,nj))
                ni = i + dy; nj = j + dx
                while 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] != FL:
                        neighbors2[i][j].append((ni,nj)); break
                    ni += dy; nj += dx
    print(simulate(grid, neighbors1, 4), simulate(grid, neighbors2, 5))

if __name__ == '__main__':
    main()