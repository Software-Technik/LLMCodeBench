import sys
with open(sys.argv[1]) as f:
    header = f.readline().strip()
    seeds = list(map(int, header.split(':',1)[1].split()))
    maps = []
    cur = None
    for line in f:
        line = line.strip()
        if not line:
            cur = None
        elif line == 'map:':
            cur = []
            maps.append(cur)
        else:
            if cur is not None:
                d,s,l = map(int, line.split())
                cur.append((s, s+l-1, d-s))
min_loc = float('inf')
for v in seeds:
    x = v
    for m in maps:
        for a,b,off in m:
            if a <= x <= b:
                x += off
                break
    if x < min_loc:
        min_loc = x
intervals = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
for m in maps:
    m.sort(key=lambda t: t[0])
for m in maps:
    new_int = []
    for st,ln in intervals:
        end = st + ln - 1
        curp = st
        for a,b,off in m:
            if curp > end:
                break
            if curp < a:
                e0 = a-1 if a-1 < end else end
                l0 = e0 - curp + 1
                new_int.append((curp, l0))
                curp = e0 + 1
            if curp < a:
                continue
            if curp <= b:
                e1 = b if b < end else end
                l1 = e1 - curp + 1
                new_int.append((curp+off, l1))
                curp = e1 + 1
        if curp <= end:
            new_int.append((curp, end - curp + 1))
    intervals = new_int
ans2 = min(t for t,_ in intervals)
sys.stdout.write(f"{int(min_loc)} {ans2}")