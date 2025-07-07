import sys
from collections import defaultdict
def main():
    sizes=defaultdict(int)
    sizes[()]=0
    prefixes=[()]
    in_ls=False
    with open(sys.argv[1]) as f:
        for line in f:
            line=line.rstrip('\n')
            if line.startswith('$'):
                in_ls=False
                if line.startswith('$ cd '):
                    t=line[5:]
                    if t=='/':
                        prefixes=[()]
                    elif t=='..':
                        prefixes.pop()
                    else:
                        p=prefixes[-1]+(t,)
                        prefixes.append(p)
                        sizes[p]=sizes[p]
                elif line.startswith('$ ls'):
                    in_ls=True
            elif in_ls:
                if line.startswith('dir '):
                    p=prefixes[-1]+(line[4:],)
                    sizes[p]=sizes[p]
                else:
                    s=int(line.split(' ',1)[0])
                    for p in prefixes:
                        sizes[p]+=s
    part1=sum(v for v in sizes.values() if v<=100000)
    used=sizes[()]
    unused=70000000-used
    need=30000000-unused
    part2=min(v for v in sizes.values() if v>=need)
    sys.stdout.write(f"{part1}\n{part2}\n")
if __name__=='__main__':
    main()