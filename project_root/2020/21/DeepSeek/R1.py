import sys

input_path = sys.argv[1]
if "s" in sys.argv:
    input_file = "input_small.txt"
else:
    input_file = input_path

try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

def line_transform(line):
    left, right = line.split(" (contains ")
    right = right[:-1]
    return left.split(" "), right.split(", ")

lines = [line_transform(line) for line in lines]

candidates = {}
for left, right in lines:
    ingredients = set(left)
    for allergen in right:
        if allergen in candidates:
            candidates[allergen] &= ingredients
        else:
            candidates[allergen] = set(ingredients)

queue = []
for allergen, s in candidates.items():
    if len(s) == 1:
        queue.append(allergen)

while queue:
    allergen = queue.pop(0)
    if len(candidates[allergen]) != 1:
        continue
    ing = next(iter(candidates[allergen]))
    for other in candidates:
        if other == allergen:
            continue
        if ing in candidates[other]:
            candidates[other].discard(ing)
            if len(candidates[other]) == 1:
                queue.append(other)

dangerous_gibberish = set()
for s in candidates.values():
    dangerous_gibberish |= s

tot = 0
for left, _ in lines:
    for gib in left:
        if gib not in dangerous_gibberish:
            tot += 1

s = sorted(candidates.keys())
s = [next(iter(candidates[k])) for k in s]
s = ",".join(s)

print(tot, s)