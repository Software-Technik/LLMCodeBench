import sys

def main():
    first = second = 0
    with open(sys.argv[1]) as f:
        for line in f:
            words = line.split()
            seen = set()
            seen_sorted = set()
            ok1 = ok2 = True
            for w in words:
                if ok1:
                    if w in seen:
                        ok1 = False
                    else:
                        seen.add(w)
                if ok2:
                    s = ''.join(sorted(w))
                    if s in seen_sorted:
                        ok2 = False
                    else:
                        seen_sorted.add(s)
                if not ok1 and not ok2:
                    break
            if ok1:
                first += 1
            if ok2:
                second += 1
    print(first)
    print(second)

if __name__ == "__main__":
    main()