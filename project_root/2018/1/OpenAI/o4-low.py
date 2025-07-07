#!/usr/bin/env python3
import sys
def main():
    mods = list(map(int, open(sys.argv[1]).read().split()))
    total = sum(mods)
    seen = {0}
    freq = 0
    i = 0
    n = len(mods)
    while True:
        freq += mods[i]
        if freq in seen:
            break
        seen.add(freq)
        i = (i + 1) % n
    sys.stdout.write(f"{total} {freq}")
if __name__ == "__main__":
    main()