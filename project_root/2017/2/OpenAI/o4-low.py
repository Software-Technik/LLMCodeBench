import sys

def part1(sheet):
    return sum(max(r)-min(r) for r in sheet)

def part2(sheet):
    total=0
    for r in sheet:
        r_sorted=sorted(r,reverse=True)
        n=len(r_sorted)
        found=False
        for i in range(n):
            ai=r_sorted[i]
            for j in range(i+1,n):
                aj=r_sorted[j]
                if ai%aj==0:
                    total+=ai//aj
                    found=True
                    break
            if found: break
    return total

def parse_input(path):
    with open(path) as f:
        return [list(map(int,l.split())) for l in f if l.strip()]

data=parse_input(sys.argv[1])
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")