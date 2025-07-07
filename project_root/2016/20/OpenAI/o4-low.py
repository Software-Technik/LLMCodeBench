import sys

def main():
    with open(sys.argv[1]) as f:
        ips = [tuple(map(int, line.split('-', 1))) for line in f if line]
    ips.sort()
    lowest_available = 0
    the_lowest = None
    nr_available = 0
    for low, high in ips:
        if low > lowest_available:
            nr_available += low - lowest_available
            if the_lowest is None:
                the_lowest = lowest_available
        if high + 1 > lowest_available:
            lowest_available = high + 1
    print(the_lowest, nr_available)

if __name__ == "__main__":
    main()