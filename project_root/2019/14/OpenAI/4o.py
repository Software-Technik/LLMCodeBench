import sys
from math import ceil
from collections import defaultdict

def calculate_ore(reactions, fuel_needed):
    needed = { "FUEL": fuel_needed }
    leftovers = defaultdict(int)

    while True:
        if len(needed) == 1 and "ORE" in needed:
            return needed["ORE"]

        newneeded = defaultdict(int)
        if "ORE" in needed:
            newneeded["ORE"] = needed["ORE"]
        
        for n in list(needed):
            if n == "ORE":
                continue
            if needed[n] <= leftovers[n]:
                leftovers[n] -= needed[n]
                continue

            actuallyneeded = needed[n] - leftovers[n]
            del leftovers[n]
            produced, ingredients = reactions[n]
            factor = ceil(actuallyneeded / produced)
            leftovers[n] = produced * factor - actuallyneeded

            for amount, chemical in ingredients:
                newneeded[chemical] += amount * factor

        needed = newneeded

def part1(reactions):
    return calculate_ore(reactions, 1)

def part2(reactions):
    trillion = 1_000_000_000_000
    low, high = 0, trillion

    while low < high:
        mid = (low + high + 1) // 2
        ore = calculate_ore(reactions, mid)
        if ore < trillion:
            low = mid
        else:
            high = mid - 1

    return low

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
    reactions = {}
    for line in data:
        parts = line.split(" => ")
        inputs = [(int(x.split()[0]), x.split()[1]) for x in parts[0].split(", ")]
        output_qty, output_name = parts[1].split()
        reactions[output_name] = (int(output_qty), inputs)

sys.stdout.write(f"{part1(reactions)} {part2(reactions)}")