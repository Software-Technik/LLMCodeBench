import sys

def main():
    p1 = p2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            a, b, c = map(int, line.split('x'))
            ab = a * b
            bc = b * c
            ac = a * c
            p1 += 2 * (ab + bc + ac) + min(ab, bc, ac)
            total = a + b + c
            p2 += 2 * (total - max(a, b, c)) + a * b * c
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()