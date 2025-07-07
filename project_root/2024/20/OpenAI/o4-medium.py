import sys
dd = [(1,0),(0,1),(-1,0),(0,-1)]
offsets2 = [(dx1+dx2,dy1+dy2) for dx1,dy1 in dd for dx2,dy2 in dd]
input_path = sys.argv[1]
with open(input_path) as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]
N = len(grid)
for i in range(N):
    for j in range(N):
        if grid[i][j]=='S': si,sj = i,j
        elif grid[i][j]=='E': ei,ej = i,j
path = [(si,sj)]
while path[-1]!=(ei,ej):
    i,j = path[-1]
    for dx,dy in dd:
        ii,jj = i+dx, j+dy
        if 0<=ii<N and 0<=jj<N and grid[ii][jj]!='#' and (len(path)<2 or (ii,jj)!=path[-2]):
            path.append((ii,jj)); break
og = len(path)-1
times = {coord: og-t for t,coord in enumerate(path)}
ans1 = 0
for t,(i,j) in enumerate(path):
    for dx,dy in offsets2:
        ii, jj = i+dx, j+dy
        if 0<=ii<N and 0<=jj<N and grid[ii][jj]!='#' and (ii,jj) in times:
            if og - (t + times[(ii,jj)] + 2) >= 100:
                ans1 += 1
ans2 = 0
max_len = 20
for t,(i,j) in enumerate(path):
    for dx in range(-max_len, max_len+1):
        ii = i+dx
        if ii<0 or ii>=N: continue
        bound = max_len - abs(dx)
        for dy in range(-bound, bound+1):
            jj = j+dy
            if jj<0 or jj>=N or grid[ii][jj]=='#' or (ii,jj) not in times: continue
            if og - (t + times[(ii,jj)] + abs(dx)+abs(dy)) >= 100:
                ans2 += 1
print(ans1, ans2)