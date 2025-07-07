import sys
def main():
    with open(sys.argv[1]) as f:
        rows = f.read().strip().split("\n")
    grid = [list(r) for r in rows]
    n = len(grid); m = len(grid[0])
    comp_id = [[0]*m for _ in range(n)]
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    comp_size = []
    cid = 0; ans1 = 0
    for i in range(n):
        for j in range(m):
            if comp_id[i][j] == 0:
                cid += 1
                c = grid[i][j]
                stack = [(i,j)]
                comp_id[i][j] = cid
                sz = 0; p1 = 0
                while stack:
                    x,y = stack.pop()
                    sz += 1
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if nx<0 or nx>=n or ny<0 or ny>=m or grid[nx][ny] != c:
                            p1 += 1
                        elif comp_id[nx][ny] == 0:
                            comp_id[nx][ny] = cid
                            stack.append((nx,ny))
                comp_size.append(sz)
                ans1 += sz * p1
    comp_p2 = [0]*cid
    for i in range(-1, n):
        for j in range(-1, m):
            x0,y0 = i,j; x1,y1 = i,j+1; x2,y2 = i+1,j; x3,y3 = i+1,j+1
            ids = set()
            if 0<=x0<n and 0<=y0<m: ids.add(comp_id[x0][y0])
            if 0<=x1<n and 0<=y1<m: ids.add(comp_id[x1][y1])
            if 0<=x2<n and 0<=y2<m: ids.add(comp_id[x2][y2])
            if 0<=x3<n and 0<=y3<m: ids.add(comp_id[x3][y3])
            for k in ids:
                b0 = 1 if 0<=x0<n and 0<=y0<m and comp_id[x0][y0]==k else 0
                b1 = 1 if 0<=x1<n and 0<=y1<m and comp_id[x1][y1]==k else 0
                b2 = 1 if 0<=x2<n and 0<=y2<m and comp_id[x2][y2]==k else 0
                b3 = 1 if 0<=x3<n and 0<=y3<m and comp_id[x3][y3]==k else 0
                if b0 and b3 and not b1 and not b2:
                    comp_p2[k-1] += 2
                elif b1 and b2 and not b0 and not b3:
                    comp_p2[k-1] += 2
                else:
                    s = b0+b1+b2+b3
                    if s==1 or s==3:
                        comp_p2[k-1] += 1
    ans2 = 0
    for idx in range(cid):
        ans2 += comp_size[idx] * comp_p2[idx]
    print(ans1, ans2)
if __name__ == '__main__':
    main()