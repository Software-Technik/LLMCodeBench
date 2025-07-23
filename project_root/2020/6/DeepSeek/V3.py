import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()

groups = data.split("\n\n")

result1 = sum(len(set(group.replace("\n", "").replace(" ", ""))) for group in groups)

result2 = 0
for group in groups:
    ppl = group.splitlines()
    if not ppl:
        continue
    common = set(ppl[0].strip().replace(" ", ""))
    for p in ppl[1:]:
        common.intersection_update(p.strip().replace(" ", ""))
    result2 += len(common)

print(result1, result2)