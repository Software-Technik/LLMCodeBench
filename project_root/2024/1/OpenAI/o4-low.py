import sys

def main():
    a = []
    counts = {}
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            x, y = map(int, line.split())
            a.append(x)
            counts[y] = counts.get(y, 0) + 1

    part2 = sum(x * counts.get(x, 0) for x in a)

    a.sort()
    b_sorted = []
    for y in sorted(counts):
        b_sorted.extend([y] * counts[y])

    part1 = sum(abs(x - y) for x, y in zip(a, b_sorted))

    print(part1, part2)

if __name__ == "__main__":
    main()