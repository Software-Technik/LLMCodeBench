import sys
def main():
    p1 = p2 = 0
    with open(sys.argv[1]) as f:
        for L in f:
            a,b,c,d = map(int, L.replace('-', ' ').replace(',', ' ').split())
            if (a-c)*(b-d) <= 0: p1 += 1
            if c <= a <= d or a <= c <= b: p2 += 1
    sys.stdout.write(f"{p1}\n{p2}\n")
if __name__ == "__main__":
    main()