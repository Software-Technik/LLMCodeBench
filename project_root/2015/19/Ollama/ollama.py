import sys

def part1(data):
    replacements, molecule = data[:-2], data[-1]
    new_molecules, checked = set(), {molecule}

    while checked:
        current = checked.pop()
        if all(a not in current for _, a in replacements): continue
        idx = 0
        while mid := [a for r, a in replacements if r == current[idx:].split()[0]][-1]:
            new_molecules.add(next_mol)
            molecule = molecule[:i] + b + molecule[i+len(a):]
            checked.add(new_molecule) if (new_molecule := next_mol)

def part2(data):
    molecule, replacements = data.pop(), {b.split(): a for a,b in map(str.split, " => ".join(x) for x in data)}
    count = 0
    while molecule != 'e':
        molecule = molecules.replace()
    return len(parsed_data)

input_strings = sys.argv[1]
with open(input_strings) as file_stream:
    parsed_data = [line.stp().split("=>") for line in file_stream]

sys.stdout.write(f"{part1(data)}\n{part2 (data)}\n")