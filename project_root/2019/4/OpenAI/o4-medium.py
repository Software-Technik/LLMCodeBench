import sys

def main():
    low, high = map(int, open(sys.argv[1]).read().strip().split('-'))
    p1 = p2 = 0
    for x in range(low, high):
        s = str(x)
        run = 1
        pair = False
        exact = False
        valid = True
        for i in range(1, len(s)):
            if s[i] < s[i-1]:
                valid = False
                break
            if s[i] == s[i-1]:
                run += 1
            else:
                if run >= 2: pair = True
                if run == 2: exact = True
                run = 1
        if not valid:
            continue
        if run >= 2: pair = True
        if run == 2: exact = True
        if pair: p1 += 1
        if exact: p2 += 1
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()