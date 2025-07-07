import sys
from itertools import permutations

def main():
    data = [line.strip() for line in open(sys.argv[1])]
    locations = set()
    d = {}
    for line in data:
        a, _, b, _, dist = line.split()
        dist = int(dist)
        locations.add(a); locations.add(b)
        d[a, b] = dist
        d[b, a] = dist
    mn = float('inf')
    mx = 0
    for route in permutations(locations):
        s = 0
        for i in range(len(route) - 1):
            s += d[route[i], route[i+1]]
        if s < mn: mn = s
        if s > mx: mx = s
    sys.stdout.write(f"{mn}\n{mx}\n")

if __name__ == '__main__':
    main()