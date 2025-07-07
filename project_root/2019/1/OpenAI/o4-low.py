import sys

def main():
    p1 = p2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            m = int(line)
            v = m // 3 - 2
            p1 += v
            while v > 0:
                p2 += v
                v = v // 3 - 2
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()