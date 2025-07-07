import sys

def main():
    with open(sys.argv[1]) as f:
        deltas = [int(line) for line in f if line]
    total = sum(deltas)
    seen = {0}
    freq = 0
    while True:
        for d in deltas:
            freq += d
            if freq in seen:
                sys.stdout.write(f"{total} {freq}")
                return
            seen.add(freq)

if __name__ == "__main__":
    main()