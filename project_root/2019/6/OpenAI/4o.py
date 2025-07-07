import sys
import networkx

def part1(data):
    orbits = {}
    for line in data:
        a, b = line.split(")")
        orbits[b] = a

    total_orbits = 0
    for planet in orbits:
        while planet in orbits:
            total_orbits += 1
            planet = orbits[planet]

    return total_orbits

def part2(data):
    orbits = {}
    for line in data:
        a, b = line.split(")")
        orbits[b] = a

    you_path = set()
    san_path = set()
    
    def path_to_com(planet, path_set):
        while planet in orbits:
            planet = orbits[planet]
            path_set.add(planet)

    path_to_com('YOU', you_path)
    path_to_com('SAN', san_path)

    return len(you_path.symmetric_difference(san_path))

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
sys.stdout.write(f"{part1(data)} {part2(data)}")