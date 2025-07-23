import sys

def find_lowest(ips):
    nr_available = 0
    lowest_available = 0
    the_lowest = 0

    for low, high in ips:
        if low > lowest_available:
            nr_available += low - lowest_available
            if not the_lowest:
                the_lowest = lowest_available
        if high + 1 > lowest_available:
            lowest_available = high + 1
    return the_lowest, nr_available

with open(sys.argv[1], 'r') as infile:
    addresses = infile.read().splitlines()

ips = sorted(tuple(map(int, address.split('-'))) for address in addresses if address)

first, second = find_lowest(ips)

sys.stdout.write(f"{first} {second}")