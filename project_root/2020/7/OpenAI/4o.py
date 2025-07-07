import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

def line_transform(line):
    parent = line.split(" bags")[0]
    children = line.split("contain")[1].split(",")
    children = list(map(str.strip, children))
    children = [" ".join(child.split(" ")[1:-1]) for child in children]
    return [parent, children if children != ["other"] else []]

lines = [line_transform(line) for line in lines]

tree = {parent: children for parent, children in lines}

def traverse1(parent):
    if "shiny gold" in tree[parent]:
        return True
    return any(traverse1(child) for child in tree[parent])

result1 = sum(traverse1(p) for p in tree)

def line_transform2(line):
    parent = line.split(" bags")[0]
    children = line.split("contain")[1].split(",")
    children = list(map(str.strip, children))
    if children[0].startswith("no other"):
        return (parent, {})
    amounts = [int(c.split(" ")[0]) for c in children]
    names = [" ".join(c.split(" ")[1:-1]) for c in children]
    return [parent, dict(zip(names, amounts))]

tree = {parent: children for parent, children in map(line_transform2, data.splitlines())}

def inside(parent_name):
    return sum(amount + amount * inside(name) for name, amount in tree[parent_name].items())

result2 = inside("shiny gold")
print(result1, result2)