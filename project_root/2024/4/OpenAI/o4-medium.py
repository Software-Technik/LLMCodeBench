import sys
def main():
    lines = open(sys.argv[1]).read().splitlines()
    n = len(lines); m = len(lines[0])
    dd = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    p1 = 0
    for i in range(n):
        row = lines[i]
        for j, ch in enumerate(row):
            if ch != 'X': continue
            for dx, dy in dd:
                i1 = i + dx; j1 = j + dy
                if 0 <= i1 < n and 0 <= j1 < m and lines[i1][j1] == 'M':
                    i2 = i + dx*2; j2 = j + dy*2
                    if 0 <= i2 < n and 0 <= j2 < m and lines[i2][j2] == 'A':
                        i3 = i + dx*3; j3 = j + dy*3
                        if 0 <= i3 < n and 0 <= j3 < m and lines[i3][j3] == 'S':
                            p1 += 1
    p2 = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if lines[i][j] != 'A': continue
            a = lines[i-1][j-1]; b = lines[i+1][j+1]
            if not ((a=='M' and b=='S') or (a=='S' and b=='M')): continue
            c = lines[i-1][j+1]; d = lines[i+1][j-1]
            if not ((c=='M' and d=='S') or (c=='S' and d=='M')): continue
            p2 += 1
    print(p1, p2)

if __name__ == '__main__':
    main()