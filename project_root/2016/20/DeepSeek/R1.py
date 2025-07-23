import sys

def find_lowest(ips):
    nr_available = 0
    lowest_available = 0
    the_lowest = 0

    for (low, high) in ips:
        if low > lowest_available:
            nr_available += low - lowest_available
            if not the_lowest:
                the_lowest = lowest_available
        lowest_available = max(lowest_available, high + 1)
    return the_lowest, nr_available

ips = []
with open(sys.argv[1], 'r') as infile:
    for line in infile:
        parts = line.split('-')
        a = int(parts[0])
        b = int(parts[1])
        ips.append((a, b))
ips.sort()

first, second = find_lowest(ips)
sys.stdout.write(f"{first} {second}")