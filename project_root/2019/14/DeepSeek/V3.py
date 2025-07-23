import sys
from math import ceil, floor
from collections import defaultdict

def part1(reactions):
    needed = {"FUEL": 1}
    leftovers = defaultdict(int)
    
    while True:
        if len(needed) == 1 and "ORE" in needed:
            break
        
        newneeded = {}
        if "ORE" in needed:
            newneeded["ORE"] = needed["ORE"]
        
        for chem in needed:
            if chem == "ORE":
                continue
            for rkey in reactions:
                if rkey[1] == chem:
                    actuallyneeded = max(0, needed[chem] - leftovers[chem])
                    leftovers[chem] -= (needed[chem] - actuallyneeded)
                    if actuallyneeded == 0:
                        continue
                    
                    produced, chem_name = rkey
                    factor = ceil(actuallyneeded / produced)
                    ingredients = reactions[rkey]
                    surplus = (produced * factor) - actuallyneeded
                    leftovers[chem] += surplus
                    
                    for amt, ing in ingredients:
                        newneeded[ing] = newneeded.get(ing, 0) + amt * factor
        needed = newneeded
    return needed["ORE"]

def solveFor(reactions, fuelNeeded):
    needed = {"FUEL": fuelNeeded}
    leftovers = defaultdict(int)
    
    while True:
        if len(needed) == 1 and "ORE" in needed:
            break
        
        newneeded = {}
        if "ORE" in needed:
            newneeded["ORE"] = needed["ORE"]
        
        for chem in needed:
            if chem == "ORE":
                continue
            for rkey in reactions:
                if rkey[1] == chem:
                    actuallyneeded = max(0, needed[chem] - leftovers[chem])
                    leftovers[chem] -= (needed[chem] - actuallyneeded)
                    if actuallyneeded == 0:
                        continue
                    
                    produced, chem_name = rkey
                    factor = ceil(actuallyneeded / produced)
                    ingredients = reactions[rkey]
                    surplus = (produced * factor) - actuallyneeded
                    leftovers[chem] += surplus
                    
                    for amt, ing in ingredients:
                        newneeded[ing] = newneeded.get(ing, 0) + amt * factor
        needed = newneeded
    return needed

def part2(reactions):
    trillion = 1_000_000_000_000
    low = 0
    high = trillion
    best = 0
    
    while low <= high:
        mid = (low + high) // 2
        needed = solveFor(reactions, mid)
        ore = needed["ORE"]
        if ore <= trillion:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = f.read().splitlines()
    reactions = {}
    for line in data:
        parts = line.split(" => ")
        inputs = []
        for i in parts[0].split(","):
            spl = i.split()
            inputs.append((int(spl[0]), spl[1].strip()))
        outparts = parts[1].strip().split()
        output = (int(outparts[0]), outparts[1])
        reactions[output] = inputs

sys.stdout.write(f"{part1(reactions)} {part2(reactions)}")