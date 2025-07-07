import sys

input_file = sys.argv[1]
with open(input_file) as f:
    lines = [l.strip() for l in f]
n = len(lines)
m = len(lines[0])
start_x, start_y = n//2, m//2
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
grid1 = {}
grid2 = {}
for i,row in enumerate(lines):
    for j,c in enumerate(row):
        if c=='#':
            grid1[(i,j)] = 1
            grid2[(i,j)] = 2

def part1():
    g = grid1.copy()
    x,y = start_x, start_y
    d = 0
    inf = 0
    for _ in range(10000):
        s = g.get((x,y),0)
        if s==0:
            d = (d-1)&3
            g[(x,y)] = 1
            inf+=1
        else:
            d = (d+1)&3
            g[(x,y)] = 0
        dx,dy = dirs[d]
        x+=dx; y+=dy
    return inf

def part2():
    g = grid2.copy()
    x,y = start_x, start_y
    d = 0
    inf = 0
    for _ in range(10000000):
        s = g.get((x,y),0)
        if s==0:
            d = (d-1)&3
        elif s==1:
            inf+=1
        elif s==2:
            d = (d+1)&3
        else:
            d = (d+2)&3
        g[(x,y)] = (s+1)&3
        dx,dy = dirs[d]
        x+=dx; y+=dy
    return inf

print(part1())
print(part2())