import sys
from math import ceil, floor

def calculateNeeds(needed, reactions):
    new_needed = {}
    while 'ORE' not in needed or len(needed) > 1:
        for n, amount in list(needed.items()):
            if n == "ORE":
                continue
            for rkey, rvalue in reactions.items():
                if rkey[1] == n:
                    needed_fuel = max(0, needed[n])
                    produced = rkey[0]
                    factor = (needed_fuel + produced - 1) // produced
                    req_ore = [x * factor for x in rvalue]
                    ore_key = "ORE"
                    if ore_key not in new_needed:
                        new_needed[ore_key] = sum(x[0] for x in req_ore if x[1] == ore_key)
                    else:
                        new_needed[ore_key] += sum(x[0] for x in req_ore if x[1] == ore_key)
                    remaining_fuel = factor * produced - needed[n]
                    del needed[n]
                    needed[n] = remaining_fuel
        needed.update(new_needed)
    return sum(amount for n, amount in needed.items() if n == "ORE")

def part2(reactions):
    trillion = 1_000_000_000_000
    fuel1 = 1
    fuel2 = 2 * fuel1
    while fuel2 - fuel1 > 1:
        mid_fuel = (fuel1 + fuel2) // 2
        if calculateNeeds({"FUEL": mid_fuel}, reactions) <= trillion:
            fuel1 = mid_fuel
        else:
            fuel2 = mid_fuel
    return fuel1

inout_strings = sys.argv[1]
data = open(inout_strings).read().splitlines()
reactions = dict()

for line in data:
    parts = line.split(" => ")
    inputs = []
    for i in parts[0].split(","):
        spl = i.split()
        inputs.append((int(spl[0]), spl[1].strip()))
    outparts = parts[1].strip().split()
    output = (int(outparts[0]), outparts[1])
    reactions[output] = inputs

sys.stdout.write(f"{calculateNeeds({'FUEL': 1}, reactions)} {part2(reactions)}")