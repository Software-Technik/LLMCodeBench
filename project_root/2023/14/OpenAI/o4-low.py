import sys
def part1(text):
    lines = text.split()
    h = len(lines); w = len(lines[0])
    platform = [list(line) for line in lines]
    weight = 0
    for y in range(h):
        row = platform[y]
        for x in range(w):
            if row[x]=='O':
                platform[y][x]='.'
                i=y-1
                while i>=0 and platform[i][x]=='.': i-=1
                drop=h-i-1
                platform[i+1][x]='O'
                weight+=drop
    return weight

def part2(text):
    lines = text.split()
    h = len(lines); w = len(lines[0])
    platform = [list(line) for line in lines]
    direction=0; cycles=0; states={}
    target=10**9
    while True:
        if direction&1==0:
            if direction==2:
                platform.reverse()
            else:
                if states is not None:
                    key=tuple(sorted((x,y) for y,row in enumerate(platform) for x,c in enumerate(row) if c=='O'))
                    if key in states:
                        prev=states[key]
                        rem=(target-cycles)%(cycles-prev)
                        cycles=target-rem
                        states=None
                    else:
                        states[key]=cycles
            for y in range(h):
                for x in range(w):
                    if platform[y][x]=='O':
                        platform[y][x]='.'
                        i=y-1
                        while i>=0 and platform[i][x]=='.': i-=1
                        platform[i+1][x]='O'
            if direction==2: platform.reverse()
        elif direction==1:
            for x in range(w):
                for y in range(h):
                    if platform[y][x]=='O':
                        platform[y][x]='.'
                        i=x-1
                        while i>=0 and platform[y][i]=='.': i-=1
                        platform[y][i+1]='O'
        else:
            for x in range(w-1,-1,-1):
                for y in range(h):
                    if platform[y][x]=='O':
                        platform[y][x]='.'
                        i=x+1
                        while i<w and platform[y][i]=='.': i+=1
                        platform[y][i-1]='O'
            cycles+=1
            if cycles==target:
                return sum(h-y for y,row in enumerate(platform) for c in row if c=='O')
        direction=(direction+1)&3

text = open(sys.argv[1]).read().strip()
print(part1(text), part2(text))