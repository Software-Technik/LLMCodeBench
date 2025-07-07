import sys

def main():
    grid = [list(line) for line in open(sys.argv[1]).read().splitlines()]
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "S":
                si, sj = i, j
            elif grid[i][j] == "E":
                ei, ej = i, j
    dd = [(1,0),(0,1),(-1,0),(0,-1)]
    path = [(si, sj)]
    vis = set(path)
    while path[-1] != (ei, ej):
        i, j = path[-1]
        for di, dj in dd:
            ii, jj = i+di, j+dj
            if 0<=ii<N and 0<=jj<N and (ii,jj) not in vis and grid[ii][jj] != "#":
                path.append((ii, jj))
                vis.add((ii, jj))
                break
    og = len(path) - 1
    times = {coord: og - t for t, coord in enumerate(path)}
    ans1 = 0
    for t, (i, j) in enumerate(path):
        for ii, jj in path:
            if abs(ii-i)+abs(jj-j)==2:
                v = og - (t + times[(ii, jj)] + 2)
                if v >= 100:
                    ans1 += 1
    max_len = 20
    ans2 = 0
    for t, (i, j) in enumerate(path):
        for ii, jj in path:
            time_used = abs(ii-i)+abs(jj-j)
            if time_used <= max_len:
                v = og - (t + times[(ii, jj)] + time_used)
                if v >= 100:
                    ans2 += 1
    print(ans1, ans2)

if __name__ == "__main__":
    main()