from hashlib import md5
import sys

def solve(data, stretch):
    hashes = {}
    def get_hash(i):
        if i in hashes: return hashes[i]
        h = md5((data+str(i)).encode()).hexdigest()
        if stretch:
            for _ in range(2016): h = md5(h.encode()).hexdigest()
        hashes[i] = h
        return h

    triplets = {c: [] for c in '0123456789abcdef'}
    valid = set()
    i = 0
    while True:
        h = get_hash(i)
        # find triplet
        trip_c = None
        for a,b,c in zip(h, h[1:], h[2:]):
            if a==b==c:
                trip_c = a
                break
        if trip_c:
            triplets[trip_c].append(i)
        # find quintets
        found = set()
        for a,b,c,d,e in zip(h, h[1:], h[2:], h[3:], h[4:]):
            if a==b==c==d==e and a not in found:
                found.add(a)
                for idx in triplets[a]:
                    if idx < i <= idx+1000:
                        valid.add(idx)
        if len(valid) >= 64 and i > max(valid)+1000:
            return sorted(valid)[63]
        i += 1

data = open(sys.argv[1]).read().strip()
r1 = solve(data, False)
r2 = solve(data, True)
sys.stdout.write(f"{r1} {r2}")