import sys
from collections import defaultdict

def get_ore_required(fuel_amount, reaction_for):
    needed = defaultdict(int)
    needed['FUEL'] = fuel_amount
    leftovers = defaultdict(int)
    
    while True:
        non_ore_chemicals = [chem for chem in needed if chem != 'ORE' and needed[chem] > 0]
        if not non_ore_chemicals:
            break
            
        new_needed = defaultdict(int)
        if 'ORE' in needed and needed['ORE'] > 0:
            new_needed['ORE'] = needed['ORE']
            
        for chem in non_ore_chemicals:
            amount = needed[chem]
            if leftovers[chem] > 0:
                use_left = min(amount, leftovers[chem])
                amount -= use_left
                leftovers[chem] -= use_left
            if amount <= 0:
                continue
                
            output_qty, inputs = reaction_for[chem]
            n = (amount + output_qty - 1) // output_qty
            produced = n * output_qty
            surplus = produced - amount
            leftovers[chem] += surplus
            
            for inp_amt, inp_chem in inputs:
                new_needed[inp_chem] += inp_amt * n
                
        needed = new_needed
        
    return needed['ORE']

def part1(reaction_for):
    return get_ore_required(1, reaction_for)

def part2(reaction_for):
    trillion = 1000000000000
    low_bound = 1
    high_bound = 1
    while get_ore_required(high_bound, reaction_for) <= trillion:
        low_bound = high_bound
        high_bound *= 2
    lo, hi = low_bound, high_bound
    while lo < hi:
        mid = (lo + hi + 1) // 2
        ore_mid = get_ore_required(mid, reaction_for)
        if ore_mid <= trillion:
            lo = mid
        else:
            hi = mid - 1
    return lo

if __name__ == '__main__':
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read().splitlines()
        reaction_for = {}
        for line in data:
            parts = line.split(" => ")
            inputs = []
            for i in parts[0].split(","):
                spl = i.split()
                inputs.append((int(spl[0]), spl[1].strip()))
            outparts = parts[1].strip().split()
            output_amt = int(outparts[0])
            output_chem = outparts[1].strip()
            reaction_for[output_chem] = (output_amt, inputs)
            
    part1_ans = part1(reaction_for)
    part2_ans = part2(reaction_for)
    sys.stdout.write(f"{part1_ans} {part2_ans}")