import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()

groups = data.split("\n\n")
result1 = sum(len(set(ans.replace("\n", "").replace(" ", ""))) for ans in groups)

result2 = sum(len(set.intersection(*(set(p) for p in group.splitlines()))) for group in groups)

print(result1, result2)