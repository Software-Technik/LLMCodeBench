import sys
from collections import Counter

def main():
    two = three = 0
    lines = []
    with open(sys.argv[1]) as f:
        for line in f:
            s = line.strip()
            vals = Counter(s).values()
            if 2 in vals: two += 1
            if 3 in vals: three += 1
            lines.append(s)
    checksum = two * three
    common = ""
    if lines:
        L = len(lines[0])
        for i in range(L):
            seen = set()
            for s in lines:
                key = s[:i] + s[i+1:]
                if key in seen:
                    common = key
                    break
                seen.add(key)
            if common:
                break
    sys.stdout.write(f"{checksum} {common}")

if __name__ == "__main__":
    main()