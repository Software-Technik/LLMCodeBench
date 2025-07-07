import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.readline().strip().split(',')
    counts = [0] * 9
    for x in data:
        counts[int(x)] += 1
    part1 = None
    for day in range(256):
        zero = counts[0]
        for i in range(8):
            counts[i] = counts[i+1]
        counts[8] = zero
        counts[6] += zero
        if day == 79:
            part1 = sum(counts)
    part2 = sum(counts)
    sys.stdout.write(f"{part1} {part2}")

if __name__ == "__main__":
    main()