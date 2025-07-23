import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()

groups = data.split("\n\n")
total1 = 0
total2 = 0

for group in groups:
    s = group.strip().replace("\n", "").replace(" ", "")
    total1 += len(set(s))
    
    people = group.splitlines()
    common_set = None
    for p in people:
        cleaned = p.strip().replace("\n", "").replace(" ", "")
        s_set = set(cleaned)
        if common_set is None:
            common_set = s_set
        else:
            common_set &= s_set
    total2 += len(common_set) if common_set is not None else 0

print(total1, total2)