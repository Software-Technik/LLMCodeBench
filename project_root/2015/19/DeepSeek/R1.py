import sys

def part1(data):
    replacements_list = []
    for replacement in data[:-2]:
        a, b = replacement.split(" => ")
        replacements_list.append((a, b))
    molecule = data[-1]
    new_molecules = set()
    
    for (a, b) in replacements_list:
        n = len(a)
        i = 0
        while i < len(molecule) - n + 1:
            j = molecule.find(a, i)
            if j == -1:
                break
            new_molecule = molecule[:j] + b + molecule[j+n:]
            new_molecules.add(new_molecule)
            i = j + 1
            
    return len(new_molecules)

def part2(data):
    replacements_dict = {}
    for line in data[:-2]:
        a, b = line.split(" => ")
        replacements_dict[b] = a
    molecule = data[-1]
    count = 0
    
    while molecule != "e":
        chosen_rep = None
        max_index = -1
        found_e = False
        for rep in replacements_dict:
            if replacements_dict[rep] == "e":
                if rep == molecule:
                    chosen_rep = rep
                    found_e = True
                    break
                else:
                    continue
            idx = molecule.rfind(rep)
            if idx != -1:
                if idx >= max_index:
                    max_index = idx
                    chosen_rep = rep
                    
        if chosen_rep is None:
            break
            
        if found_e:
            molecule = "e"
        else:
            n = len(chosen_rep)
            molecule = molecule[:max_index] + replacements_dict[chosen_rep] + molecule[max_index+n:]
        count += 1
        
    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")