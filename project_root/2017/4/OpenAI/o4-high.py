import sys

def main():
    first = second = 0
    with open(sys.argv[1]) as f:
        for line in f:
            words = line.split()
            seen = set()
            seen_an = set()
            ok1 = ok2 = True
            for w in words:
                if w in seen:
                    ok1 = False
                else:
                    seen.add(w)
                sw = ''.join(sorted(w))
                if sw in seen_an:
                    ok2 = False
                else:
                    seen_an.add(sw)
            first += ok1
            second += ok2
    print(first)
    print(second)

if __name__ == '__main__':
    main()