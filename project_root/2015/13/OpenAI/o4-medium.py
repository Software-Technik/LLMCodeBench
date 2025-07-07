import sys
from itertools import permutations

def main():
    lines = [l.strip() for l in open(sys.argv[1])]
    M = {}
    names = set()
    for line in lines:
        parts = line.split()
        A = parts[0]
        B = parts[10][:-1]
        v = int(parts[3]) * (1 if parts[2] == 'gain' else -1)
        M[(A, B)] = v
        names.add(A)
        names.add(B)
    names = sorted(names)
    idx = {name: i for i, name in enumerate(names)}
    n1 = len(names)
    H1 = [[0] * n1 for _ in range(n1)]
    for (A, B), v in M.items():
        H1[idx[A]][idx[B]] = v

    def calc(n, H):
        people = list(range(n))
        first = people[0]
        best = -10**18
        for perm in permutations(people[1:]):
            arr = (first,) + perm
            s = 0
            for i, v in enumerate(arr):
                s += H[v][arr[i - 1]] + H[v][arr[(i + 1) % n]]
            if s > best:
                best = s
        return best

    part1 = calc(n1, H1)
    n2 = n1 + 1
    H2 = [row + [0] for row in H1]
    H2.append([0] * n2)
    part2 = calc(n2, H2)
    sys.stdout.write(f"{part1}\n{part2}\n")

if __name__ == '__main__':
    main()