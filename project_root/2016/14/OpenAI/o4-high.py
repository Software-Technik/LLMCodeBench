from hashlib import md5
import sys

def find_key(salt, stretch):
    m = md5
    trip = {}
    ks = set()
    mk = -1
    i = 0
    while True:
        h = m((salt+str(i)).encode()).hexdigest()
        for _ in range(stretch):
            h = m(h.encode()).hexdigest()
        sq = set()
        j = 0
        while j < 28:
            c = h[j]
            if h[j+1]==c and h[j+2]==c and h[j+3]==c and h[j+4]==c:
                sq.add(c)
            j += 1
        if sq:
            for c in sq:
                if c in trip:
                    for t in trip[c]:
                        if i <= t + 1000:
                            if t not in ks:
                                ks.add(t)
                                if t > mk: mk = t
        c3 = None
        j = 0
        while j < 30:
            c = h[j]
            if h[j+1]==c and h[j+2]==c:
                c3 = c
                break
            j += 1
        if c3:
            trip.setdefault(c3, []).append(i)
        if len(ks) >= 64 and i > mk + 1000:
            break
        i += 1
    return sorted(ks)[63]

f = sys.argv[1]
s = open(f).read().strip()
p1 = find_key(s, 0)
p2 = find_key(s, 2016)
sys.stdout.write(f"{p1} {p2}")