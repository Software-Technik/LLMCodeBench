import sys
from collections import Counter
def main():
    with open(sys.argv[1]) as f:
        first=f.readline().rstrip('\n')
        if not first:
            sys.stdout.write(' ')
            return
        m=len(first)
        cnts=[Counter() for _ in range(m)]
        for i,ch in enumerate(first): cnts[i][ch]+=1
        for line in f:
            line=line.rstrip('\n')
            for i,ch in enumerate(line): cnts[i][ch]+=1
    part1=''.join(max(c.items(), key=lambda x: x[1])[0] for c in cnts)
    part2=''.join(min(c.items(), key=lambda x: x[1])[0] for c in cnts)
    sys.stdout.write(f"{part1} {part2}")
if __name__=='__main__':
    main()