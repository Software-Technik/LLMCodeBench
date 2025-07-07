import sys
ADJ = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
DIRS = (
    (((-1,-1),(-1,0),(-1,1)),(-1,0)),
    (((1,-1),(1,0),(1,1)),(1,0)),
    (((-1,-1),(0,-1),(1,-1)),(0,-1)),
    (((-1,1),(0,1),(1,1)),(0,1)),
)
def part1(data):
    elves = {(i,j) for i,line in enumerate(data) for j,c in enumerate(line) if c=='#'}
    p = 0
    for _ in range(10):
        proposals = {}
        counts = {}
        elvs = elves
        for r,c in elvs:
            for dr,dc in ADJ:
                if (r+dr,c+dc) in elvs:
                    break
            else:
                continue
            for k in range(4):
                checks,move = DIRS[(p+k)&3]
                for dr,dc in checks:
                    if (r+dr,c+dc) in elvs:
                        break
                else:
                    nr,nc = r+move[0],c+move[1]
                    proposals[(r,c)] = (nr,nc)
                    counts[(nr,nc)] = counts.get((nr,nc),0)+1
                    break
        new_elves = set()
        for r,c in elvs:
            tgt = proposals.get((r,c))
            if tgt and counts[tgt]==1:
                new_elves.add(tgt)
            else:
                new_elves.add((r,c))
        elves = new_elves
        p = (p+1)&3
    min_r = min(r for r,c in elves)
    max_r = max(r for r,c in elves)
    min_c = min(c for r,c in elves)
    max_c = max(c for r,c in elves)
    return (max_r-min_r+1)*(max_c-min_c+1) - len(elves)
def part2(data):
    elves = {(i,j) for i,line in enumerate(data) for j,c in enumerate(line) if c=='#'}
    p = 0
    round = 1
    while True:
        proposals = {}
        counts = {}
        elvs = elves
        for r,c in elvs:
            for dr,dc in ADJ:
                if (r+dr,c+dc) in elvs:
                    break
            else:
                continue
            for k in range(4):
                checks,move = DIRS[(p+k)&3]
                for dr,dc in checks:
                    if (r+dr,c+dc) in elvs:
                        break
                else:
                    nr,nc = r+move[0],c+move[1]
                    proposals[(r,c)] = (nr,nc)
                    counts[(nr,nc)] = counts.get((nr,nc),0)+1
                    break
        if not proposals:
            return round
        new_elves = set()
        for r,c in elvs:
            tgt = proposals.get((r,c))
            if tgt and counts[tgt]==1:
                new_elves.add(tgt)
            else:
                new_elves.add((r,c))
        elves = new_elves
        p = (p+1)&3
        round += 1
if __name__=='__main__':
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    print(part1(data))
    print(part2(data))