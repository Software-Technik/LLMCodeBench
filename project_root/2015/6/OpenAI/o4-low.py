import sys

def part1(data):
    grid = [[0]*1000 for _ in range(1000)]
    for line in data:
        tokens = line.split()
        if tokens[0]=='toggle':
            x1,y1=map(int,tokens[1].split(','))
            x2,y2=map(int,tokens[3].split(','))
            for i in range(x1,x2+1):
                row=grid[i]
                for j in range(y1,y2+1):
                    row[j]^=1
        else:
            x1,y1=map(int,tokens[2].split(','))
            x2,y2=map(int,tokens[4].split(','))
            if tokens[1]=='on':
                v=1
                for i in range(x1,x2+1):
                    row=grid[i]
                    for j in range(y1,y2+1):
                        row[j]=1
            else:
                for i in range(x1,x2+1):
                    row=grid[i]
                    for j in range(y1,y2+1):
                        row[j]=0
    return sum(sum(row) for row in grid)

def part2(data):
    grid = [[0]*1000 for _ in range(1000)]
    for line in data:
        tokens = line.split()
        if tokens[0]=='toggle':
            x1,y1=map(int,tokens[1].split(','))
            x2,y2=map(int,tokens[3].split(','))
            for i in range(x1,x2+1):
                row=grid[i]
                for j in range(y1,y2+1):
                    row[j]+=2
        else:
            x1,y1=map(int,tokens[2].split(','))
            x2,y2=map(int,tokens[4].split(','))
            if tokens[1]=='on':
                for i in range(x1,x2+1):
                    row=grid[i]
                    for j in range(y1,y2+1):
                        row[j]+=1
            else:
                for i in range(x1,x2+1):
                    row=grid[i]
                    for j in range(y1,y2+1):
                        v=row[j]-1
                        row[j]=v if v>0 else 0
    return sum(sum(row) for row in grid)

with open(sys.argv[1]) as f:
    data=[l.strip() for l in f]
print(part1(data))
print(part2(data))