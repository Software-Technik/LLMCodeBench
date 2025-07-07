import sys

setup = {"red": 12, "green": 13, "blue": 14}
data = open(sys.argv[1]).read().splitlines()
total1 = 0
total2 = 0
for i, line in enumerate(data, 1):
    rest = line[line.find(":") + 1:]
    possible = True
    max_counts = {}
    for game_set in rest.split(";"):
        for cube in game_set.split(","):
            part = cube.strip().split(maxsplit=1)
            n = int(part[0]); color = part[1]
            if possible and n > setup[color]:
                possible = False
            prev = max_counts.get(color)
            if prev is None or n > prev:
                max_counts[color] = n
    if possible:
        total1 += i
    prod = 1
    for v in max_counts.values():
        prod *= v
    total2 += prod
sys.stdout.write(f"{total1} {total2}")