import sys
from hashlib import md5
from bisect import bisect_right
from collections import defaultdict

def find_index(salt, stretch):
    trip_map = {}
    quint_map = defaultdict(list)
    keys = []
    idx = 0
    while True:
        h = md5((salt + str(idx)).encode()).hexdigest()
        if stretch:
            for _ in range(2016):
                h = md5(h.encode()).hexdigest()
        last = ''
        count = 0
        for ch in h:
            if ch == last:
                count += 1
            else:
                last = ch
                count = 1
            if count == 5:
                quint_map[ch].append(idx)
        for i in range(len(h) - 2):
            if h[i] == h[i+1] == h[i+2]:
                trip_map[idx] = h[i]
                break
        work = idx - 1000
        if work >= 0:
            c = trip_map.get(work)
            if c:
                lst = quint_map[c]
                if bisect_right(lst, work) < len(lst):
                    keys.append(work)
                    if len(keys) == 64:
                        return work
            del trip_map[work]
        idx += 1

def main():
    salt = open(sys.argv[1]).read().strip()
    p1 = find_index(salt, False)
    p2 = find_index(salt, True)
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()