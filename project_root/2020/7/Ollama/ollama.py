import sys

input_path = sys.argv[1]

def line_transform(line):
    parent, rest = line.split(" bags contain ")
    if "no other" in rest:
        return (parent, [])
    children = []
    for child in rest.strip('.').split(', '):
        amount = int(child.split()[0])
        name = " ".join(child.split()[1:-1])
        children.append((name, amount))
    return (parent, children)

with open(input_path) as f:
    lines = f.read().strip().split('\n')
    tree = dict(line_transform(line) for line in lines)

def traverse1(parent):
    if "shiny gold" in [child[0] for child in tree.get(parent, [])]:
        return True
    return any(traverse1(child[0]) for child in tree.get(parent, []))

result1 = sum(traverse1(parent) for parent in tree)

def inside(parent_name):
    children = tree[parent_name]
    if not children:
        return 0
    return sum(amount * (1 + inside(name)) for name, amount in children)

result2 = inside("shiny gold")
print(result1, result2)