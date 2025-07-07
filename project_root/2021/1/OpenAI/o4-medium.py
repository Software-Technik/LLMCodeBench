import sys

def main():
    path = sys.argv[1]
    count1 = count2 = 0
    prev = None
    buf = [0, 0, 0]
    k = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = int(line)
            if prev is not None and d > prev:
                count1 += 1
            prev = d
            if k >= 3 and d > buf[k % 3]:
                count2 += 1
            buf[k % 3] = d
            k += 1
    sys.stdout.write(f"{count1} {count2}")

if __name__ == "__main__":
    main()