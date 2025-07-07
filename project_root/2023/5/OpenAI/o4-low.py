import sys

def part1(text):
    header, *blocks = text.split("map:\n")
    seeds = list(map(int, header.split(":",1)[1].split()))
    mappings = []
    for b in blocks:
        m = [tuple(map(int, line.split())) for line in b.splitlines() if line]
        if m: mappings.append(m)
    best = None
    for v in seeds:
        x = v
        for m in mappings:
            for d,s,l in m:
                if s <= x < s+l:
                    x += d-s
                    break
        if best is None or x < best: best = x
    return best

def get_ranges(i0,l,m):
    r=[]
    i1=i0+l-1
    for d,s,len_ in m:
        e=s+len_-1
        if i0< s:
            if i1< s:
                r.append((i0,i1-i0+1)); return r
            r.append((i0,s-i0)); i0=s
        if s<=i0<=e:
            ns=i0+(d-s)
            if i1<=e:
                r.append((ns,i1-i0+1)); return r
            r.append((ns,e-i0+1)); i0=e+1
    r.append((i0,i1-i0+1))
    return r

def part2(text):
    header, *blocks = text.split("map:\n")
    a=list(map(int, header.split(":",1)[1].split()))
    seeds=[(a[i],a[i+1]) for i in range(0,len(a),2)]
    mappings = []
    for b in blocks:
        m=[tuple(map(int,line.split())) for line in b.splitlines() if line]
        if m:
            m.sort(key=lambda x:x[1])
            mappings.append(m)
    for m in mappings:
        ns=[]
        for i0,l in seeds:
            ns.extend(get_ranges(i0,l,m))
        seeds=ns
    return min(i for i,_ in seeds)

t = open(sys.argv[1]).read()
sys.stdout.write(f"{part1(t)} {part2(t)}")