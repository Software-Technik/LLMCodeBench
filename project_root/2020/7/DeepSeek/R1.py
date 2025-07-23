import os
import sys
from collections import deque

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    lines = data.splitlines()

rev_graph = {}
for line in lines:
    if " bags contain " not in line:
        continue
    parent, rest = line.split(" bags contain ", 1)
    rest = rest.rstrip('.')
    if rest == "no other bags":
        children = []
    else:
        children = []
        parts = rest.split(', ')
        for part in parts:
            words = part.split()
            name = " ".join(words[1:-1])
            children.append(name)
    for child in children:
        if child not in rev_graph:
            rev_graph[child] = []
        rev_graph[child].append(parent)

q = deque(["shiny gold"])
seen = set(["shiny gold"])
while q:
    node = q.popleft()
    if node in rev_graph:
        for parent_bag in rev_graph[node]:
            if parent_bag not in seen:
                seen.add(parent_bag)
                q.append(parent_bag)

result1 = len(seen) - 1

tree2 = {}
for line in lines:
    if " bags contain " not in line:
        continue
    parent, rest = line.split(" bags contain ", 1)
    rest = rest.rstrip('.')
    if rest == "no other bags":
        tree2[parent] = {}
    else:
        children_dict = {}
        parts = rest.split(', ')
        for part in parts:
            words = part.split()
            num = int(words[0])
            name = " ".join(words[1:-1])
            children_dict[name] = num
        tree2[parent] = children_dict

memo = {}
def count_bags(bag):
    if bag in memo:
        return memo[bag]
    children_dict = tree2.get(bag, {})
    if not children_dict:
        memo[bag] = 0
        return 0
    total = 0
    for child, num in children_dict.items():
        total += num * (1 + count_bags(child))
    memo[bag] = total
    return total

result2 = count_bags("shiny gold")
print(result1, result2)