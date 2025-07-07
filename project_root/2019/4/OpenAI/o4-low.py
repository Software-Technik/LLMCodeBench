import sys

def main():
    lower, upper = map(int, open(sys.argv[1]).read().splitlines()[0].split('-'))
    p1 = p2 = 0
    for x in range(lower, upper):
        s = str(x)
        inc = True
        run = 1
        has1 = has2 = False
        for i in range(1, 6):
            if s[i] < s[i-1]:
                inc = False
                break
            if s[i] == s[i-1]:
                run += 1
            else:
                if run >= 2: has1 = True
                if run == 2: has2 = True
                run = 1
        if not inc: continue
        if run >= 2: has1 = True
        if run == 2: has2 = True
        if has1: p1 += 1
        if has2: p2 += 1
    sys.stdout.write(f"{p1} {p2}")

if __name__ == "__main__":
    main()