import sys

def find_lowest(ips):
    nr_available = 0
    lowest_available = high = the_lowest = int(ips[0][1])
    for low, high in ips:
        if low > lowest_available:
            spaces = low - lowest_available
            nr_available += spaces
            if not the_lowest:
                the_lowest = lowest_available
        lowest_available = max(lowest_available, high + 1)
    return the_lowest, nr_available

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    addresses = (tuple(map(int, address.split('-'))) for address in infile.read().split('\n'))
ips = sorted(addresses)

first, second = find_lowest(ips)
sys.stdout.write(f"{first} {second}")