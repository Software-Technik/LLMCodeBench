import sys

def part1(lines):
    n = len(lines); m = len(lines[0]); ans = 0
    for i in range(n):
        row = lines[i]
        for j in range(m-3):
            if row[j]=='X' and row[j+1]=='M' and row[j+2]=='A' and row[j+3]=='S':
                ans += 1
        for j in range(3, m):
            if row[j]=='X' and row[j-1]=='M' and row[j-2]=='A' and row[j-3]=='S':
                ans += 1
    for i in range(n-3):
        r0, r1, r2, r3 = lines[i], lines[i+1], lines[i+2], lines[i+3]
        for j in range(m):
            if r0[j]=='X' and r1[j]=='M' and r2[j]=='A' and r3[j]=='S':
                ans += 1
        for j in range(m-3):
            if r0[j]=='X' and r1[j+1]=='M' and r2[j+2]=='A' and r3[j+3]=='S':
                ans += 1
        for j in range(3, m):
            if r0[j]=='X' and r1[j-1]=='M' and r2[j-2]=='A' and r3[j-3]=='S':
                ans += 1
    for i in range(3, n):
        r0, r1, r2, r3 = lines[i], lines[i-1], lines[i-2], lines[i-3]
        for j in range(m):
            if r0[j]=='X' and r1[j]=='M' and r2[j]=='A' and r3[j]=='S':
                ans += 1
        for j in range(m-3):
            if r0[j]=='X' and r1[j+1]=='M' and r2[j+2]=='A' and r3[j+3]=='S':
                ans += 1
        for j in range(3, m):
            if r0[j]=='X' and r1[j-1]=='M' and r2[j-2]=='A' and r3[j-3]=='S':
                ans += 1
    return ans

def part2(lines):
    n = len(lines); m = len(lines[0]); ans = 0
    for i in range(1, n-1):
        row = lines[i]; up = lines[i-1]; down = lines[i+1]
        for j in range(1, m-1):
            if row[j] == 'A':
                upleft = up[j-1]; downright = down[j+1]
                upright = up[j+1]; downleft = down[j-1]
                if ((upleft=='M' and downright=='S') or (upleft=='S' and downright=='M')) and ((upright=='M' and downleft=='S') or (upright=='S' and downleft=='M')):
                    ans += 1
    return ans

with open(sys.argv[1]) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))