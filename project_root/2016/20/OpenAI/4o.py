import sys

def find_lowest(ips):
    nr_available = 0
    the_lowest = None
    lowest_available = 0

    for low, high in ips:
        if low > lowest_available:
            nr_available += low - lowest_available
            if the_lowest is None:
                the_lowest = lowest_available
        lowest_available = max(lowest_available, high + 1)

    return the_lowest if the_lowest is not None else lowest_available, nr_available


with open(sys.argv[1], 'r') as infile:
    ips = sorted(tuple(map(int, line.split('-'))) for line in infile if line.strip())

first, second = find_lowest(ips)

sys.stdout.write(f"{first} {second}")