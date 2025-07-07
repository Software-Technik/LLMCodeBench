import sys
def main():
    text = open(sys.argv[1]).read()
    parts = text.split("map:\n")
    header = parts[0].splitlines()[0]
    all_seeds = list(map(int, header.partition(':')[2].split()))
    mappings = []
    for block in parts[1:]:
        m = []
        for line in block.splitlines():
            if not line: break
            a,b,c = line.split()
            m.append((int(a),int(b),int(c)))
        if m: mappings.append(m)
    min_loc = None
    for v0 in all_seeds:
        v = v0
        for m in mappings:
            for d,s,l in m:
                if s <= v < s + l:
                    v += d - s
                    break
        if min_loc is None or v < min_loc:
            min_loc = v
    seeds = [(all_seeds[i], all_seeds[i+1]) for i in range(0, len(all_seeds), 2)]
    for m in mappings:
        m_sorted = sorted(m, key=lambda x: x[1])
        new = []
        for istart, il in seeds:
            iend = istart + il - 1
            cur = istart
            for d,s,l in m_sorted:
                se = s + l - 1
                if cur < s:
                    if iend < s:
                        new.append((cur, iend - cur + 1))
                        break
                    new.append((cur, s - cur))
                    cur = s
                if s <= cur <= se:
                    if iend <= se:
                        new.append((cur + d - s, iend - cur + 1))
                        break
                    new.append((cur + d - s, se - cur + 1))
                    cur = se + 1
            else:
                if cur <= iend:
                    new.append((cur, iend - cur + 1))
        seeds = new
    min2 = min(s for s,_ in seeds)
    sys.stdout.write(f"{min_loc} {min2}")
if __name__=='__main__':
    main()