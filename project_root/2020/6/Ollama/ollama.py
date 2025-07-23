import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()

groups = [group.split() for group in data.split("\n\n")]

result1 = sum(len(set(group)) for group in groups)

result2 = sum(
    len(set.intersection(*(set(person) for person in group)))
    for group in groups
)

print(result1, result2)