import sys

def part1(lines):
    n, m = len(lines), len(lines[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if lines[i][j] != 'X': continue
            for dx, dy in dirs:
                i1, j1 = i+dx, j+dy
                if not (0<=i1<n and 0<=j1<m and lines[i1][j1]=='M'): continue
                i2, j2 = i1+dx, j1+dy
                if not (0<=i2<n and 0<=j2<m and lines[i2][j2]=='A'): continue
                i3, j3 = i2+dx, j2+dy
                if 0<=i3<n and 0<=j3<m and lines[i3][j3]=='S':
                    ans += 1
    return ans

def part2(lines):
    n, m = len(lines), len(lines[0])
    ans = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if lines[i][j] != 'A': continue
            c1, c2 = lines[i-1][j-1], lines[i+1][j+1]
            if not ((c1=='M' and c2=='S') or (c1=='S' and c2=='M')): continue
            c3, c4 = lines[i-1][j+1], lines[i+1][j-1]
            if (c3=='M' and c4=='S') or (c3=='S' and c4=='M'):
                ans += 1
    return ans

with open(sys.argv[1]) as f:
    lines = [line.rstrip('\n') for line in f]
print(part1(lines), part2(lines))