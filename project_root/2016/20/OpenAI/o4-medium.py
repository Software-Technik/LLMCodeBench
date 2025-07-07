import sys

def find_lowest(ips):
    nr_av = 0
    lowest_av = 0
    first = None
    for lo, hi in ips:
        if lo > lowest_av:
            nr_av += lo - lowest_av
            if first is None:
                first = lowest_av
        if hi + 1 > lowest_av:
            lowest_av = hi + 1
    return first, nr_av

with open(sys.argv[1]) as f:
    ips = [tuple(map(int, line.split('-', 1))) for line in f if line]
ips.sort()
first, second = find_lowest(ips)
sys.stdout.write(f"{first} {second}")