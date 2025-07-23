import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

def ans(answer):
    pass

def line_transform(line):
    parent = line.split(" bags")[0]
    children = line.split("contain")[1].split(",")
    children = [child.strip() for child in children]
    children = [" ".join(child.split(" ")[1:-1]) for child in children]
    return (parent, [] if children == ["other"] else children)

lines = [line_transform(line) for line in lines]

tree = {}
for parent, children in lines:
    tree[parent] = children

def traverse1(parent, memo={}):
    if parent in memo:
        return memo[parent]
    children = tree[parent]
    if "shiny gold" in children:
        memo[parent] = True
        return True
    memo[parent] = any(traverse1(child, memo) for child in children)
    return memo[parent]

tot = sum(1 for p in tree if traverse1(p))
ans(tot)
result1 = tot

def line_transform2(line):
    parent = line.split(" bags")[0]
    children = line.split("contain")[1].split(",")
    children = [child.strip() for child in children]
    if children[0].startswith("no other"):
        return (parent, {})
    amounts = [int(c.split(" ")[0]) for c in children]
    names = [" ".join(c.split(" ")[1:-1]) for c in children]
    return (parent, dict(zip(names, amounts)))

tree = {}
for parent, children in map(line_transform2, data.splitlines()):
    tree[parent] = children

def inside(parent_name, memo={}):
    if parent_name in memo:
        return memo[parent_name]
    children = tree[parent_name]
    if not children:
        memo[parent_name] = 0
        return 0
    total = sum(amount * (1 + inside(name, memo)) for name, amount in children.items())
    memo[parent_name] = total
    return total

result2 = inside("shiny gold")
print(result1, result2)